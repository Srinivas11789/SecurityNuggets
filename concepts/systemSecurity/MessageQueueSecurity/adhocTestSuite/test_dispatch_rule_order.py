# Dispatch Rule - Order of Execution Test

# Python Library Import
import sys, json, hashlib, base64

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

## Order of execution

# CASE: multiple transformation and dispatch scenario - routing to queue 0
def test_transform_multiple():
     message = {}
     message_service = MessageService()
     message["_hash"] = "Query Inc."
     message["_private"] = "Query Inc."
     message["name"] = "Query Inc."
     message["num"] = 1234
     message["_special"] = "Wwww"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
     assert received["name"] == message["name"][::-1]
     assert received["num"] == ~message["num"]
     assert received["_private"] == message["_private"]
     assert received["_special"] == message["_special"]

# CASE: multiple transformation and dispatch scenario - routing to queue 1
def test_transform_multiple_1():
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

# CASE: multiple transformation and dispatch scenario - routing to queue 2
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

# CASE: multiple transformation and dispatch scenario - routing to queue 3
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

# CASE: multiple transformation and dispatch scenario - routing to queue 4
# BUG2 - private field with integer should not be considered for dispatch
def test_transform_multiple_4():
     message = {}
     message_service = MessageService()
     message["_private"] = "Query Inc."
     message["_name"] = "Qadiium Inc."
     message["_num"] = 1234
     message[" _"] = "______"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(4))
     assert received["_name"] == message["_name"]
     assert received["_num"] == message["_num"]
     assert received["_private"] == message["_private"]
     assert received[" _"] == message[" _"]

# CASE: All the queue filled at a particular instant scenario
# BUG2 Failure
## All queue filled
def test_all_queue_filled():
     message = {}
     message_service = MessageService()
     message["_hash"] = "Query Inc."
     message["_private"] = "Query Inc."
     message["name"] = "Query Inc."
     message["num"] = 1234
     message["_special"] = "Wwww"

     message1 = {}
     message1["_hash"] = "Query Inc."
     message1["_private"] = "Query Inc."
     message1["name"] = "Query Inc."
     message1["num"] = 1234

     message2 = {}
     message2["_private"] = "Query Inc."
     message2["name"] = "Query"
     message2["num"] = 1234
     message2["__hash"] = "Query Inc."

     message3 = {}
     message3["_private"] = "Query Inc."
     message3["_name"] = "Qadiium Inc."
     message3["_num"] = 1234
     message3[" _"] = "______"

     message4 = {}
     message4["_private"] = "Query Inc."
     message4["_name"] = "Qadiium Inc."
     message4["num"] = 1234
     message4[" _"] = "______"

     message_service.enqueue(json.dumps(message))
     message_service.enqueue(json.dumps(message1))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message4))

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
     assert received["name"] == message["name"][::-1]
     assert received["num"] == ~message["num"]
     assert received["_private"] == message["_private"]
     assert received["_special"] == message["_special"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]

     received = json.loads(message_service.next(2))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]

     received = json.loads(message_service.next(4))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]

     received = json.loads(message_service.next(3))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
