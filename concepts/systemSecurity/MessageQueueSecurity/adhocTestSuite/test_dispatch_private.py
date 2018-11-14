# Adhoc test of dispatch rule <private>

# Python Library Import
import sys, json, random, base64, hashlib

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

## BUG2 - dispatch rule must ignore the private field values

# CASE: Evaluate integer values in the private fields
## BUG2 - Fail
def test_private_num_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["_num"] = int("123")
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["_num"] == message["_num"]

# CASE: Evaluate Query string values in the private fields
def test_private_name_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["_name"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(4)
     assert json.loads(received)["_name"] == message["_name"]

# CASE: Evaluate private fields with hash type fields
def test_private_hash_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["__hash"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(4)
     assert json.loads(received)["__hash"] == message["__hash"]

# CASE: Evaluate a random private field existence
def test_private_custom_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["_dash"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(4)
     assert json.loads(received)["_dash"] == message["_dash"]
