# Test private field => _private type fields undergo no transformation

# Python Library Import
import sys, json, random, pytest

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

### CASE: initial functional verification of private fields behavior
def test_basic_case_of_a_private_field():
     message = {}
     message_service = MessageService()
     message["_any"] = "Hi"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["_any"] == message["_any"]

### CASE: private field with Query string
def test_private_field_with_Query():
     message = {}
     message_service = MessageService()
     message["_name"] = "Query Inc"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["_name"] == message["_name"]

### CASE: private field with integer value
def test_private_field_with_num():
     message = {}
     message_service = MessageService()
     message["_num"] = random.randint(1,10000)
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["_num"] == message["_num"]

### CASE: private field with possible hash values
def test_private_field_with_double_hash():
     message = {}
     message_service = MessageService()
     message["__hash"] = "DoubleUnderScoreHash"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["__hash"] == message["__hash"]

### CASE: private field with malformed data
# dictionary within "_hash" key
def test_private_field_with_hash_dictionary():
     with pytest.raises(Exception) as e:
     	message = {}
     	message_service = MessageService()
     	message["__hash"] = {}
     	message["__hash"]["hash"] = "DoubleUnderScoreHash"
     	message_service.enqueue(json.dumps(message))
     assert "ValueError" in str(e)
