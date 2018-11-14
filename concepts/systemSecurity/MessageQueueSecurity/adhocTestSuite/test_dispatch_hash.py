# Adhoc test of dispatch rule <hash>

# Python Library Import
import sys, json, random, base64, hashlib

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

# CASE: Evaluate hash only fields
def test_only_hash_field():
     message = {}
     message_service = MessageService()
     message["hash"] = "Special Field!!!!"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(1))["hash"] == message["hash"]

# CASE: Evaluate hash field with preceding rules
def test_hash_field_with_preceding_rules():
     message = {}
     message_service = MessageService()
     message["_special"] = random.randint(1,10000)
     message["_hash"] = str(random.randint(1,10000))
     message_service.enqueue(json.dumps(message))
     received = message_service.next(0)
     assert json.loads(received)["_special"] == message["_special"]
     assert json.loads(received)["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')

# CASE: Evaluate hash field with post rules
def test_hash_field_with_post_rules():
     message = {}
     message_service = MessageService()
     message["num"] = random.randint(1,10000)
     message["_hash"] = str(random.randint(1,10000))
     message_service.enqueue(json.dumps(message))
     received = message_service.next(1)
     assert json.loads(received)["num"] == ~message["num"]
     assert json.loads(received)["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')

# CASE: Evaluate hash field with different data types
def test_hash_field_with_different_data_type():
     message = {}
     message_service = MessageService()
     message["_hash"] = str(random.randint(1,10000))
     message_service.enqueue(json.dumps(message))
     received = message_service.next(1)
     assert json.loads(received)["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')







    

