# Test tranforma for multiple rules together

# Python Library Import
import sys, json, hashlib, base64

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService


### CASE: test transformation rule ending up at queue 1
def test_transform_multiple():
     message = {}
     message_service = MessageService()
     message["_hash"] = "Query Inc."
     message["_private"] = "Query Inc."
     message["name"] = "Query Inc."
     message["num"] = 1234
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
     assert received["name"] == message["name"][::-1]
     assert received["num"] == ~message["num"]
     assert received["_private"] == message["_private"]

### CASE: test transformation rule ending up at queue 2
def test_transform_multiple_2():
     message = {}
     message_service = MessageService()
     message["__hash"] = "Query Inc."
     message["_private"] = "Query Inc."
     message["name"] = "Query"
     message["num"] = 1234
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     assert received["__hash"] == message["__hash"]
     assert received["name"] == message["name"][::-1]
     assert received["num"] == ~message["num"]
     assert received["_private"] == message["_private"]

### CASE: test transformation rule ending up at queue 3
def test_transform_multiple_3():
     message = {}
     message_service = MessageService()
     message["_private"] = "Query Inc."
     message["name"] = "Qadiium Inc."
     message["num"] = 1234
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(3))
     assert received["name"] == message["name"]
     assert received["num"] == ~message["num"]
     assert received["_private"] == message["_private"]
