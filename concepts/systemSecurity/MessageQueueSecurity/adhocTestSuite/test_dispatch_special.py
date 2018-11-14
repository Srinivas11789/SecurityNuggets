# Adhoc test of dispatch rule <_special>

# Python Library Import
import sys, json, random, base64, hashlib

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

# CASE: Special field only
def test_only_special_field():
     message = {}
     message_service = MessageService()
     message["_special"] = "Special Field!!!!"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(0))["_special"] == message["_special"]

# CASE: special field with preceiding and post rules

def test_special_field_with_num():
     message = {}
     message_service = MessageService()
     message["_special"] = random.randint(1,10000)
     message["num"] = random.randint(1,10000)
     message_service.enqueue(json.dumps(message))
     received = message_service.next(0)
     assert json.loads(received)["_special"] == message["_special"]
     assert json.loads(received)["num"] == ~message["num"]

def test_special_field_with_Query_string():
     message = {}
     message_service = MessageService()
     message["_special"] = "Query Inc"
     message["name"] = "Query Inc"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(0)
     assert json.loads(received)["_special"] == message["_special"]
     assert json.loads(received)["name"] == message["name"][::-1]

def test_special_field_with_hash():
     message = {}
     message_service = MessageService()
     message["_special"] = "Query Inc"
     message["_hash"] = "This is Query Corporation"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_special"] == message["_special"]
