# Test Transform <Hash> Rule

# Python Library Import
import sys, json, hashlib, base64, pytest

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

### CASE: basic test with a string for hash value
def test_with_simple_string():
     message = {}
     message_service = MessageService()
     message["_hash"] = "This is Query Corporation"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]

### CASE: hash value as another field based on the readme
# BUG11 - Read me suggests that, for the "_hash":"value" pair, the value should be hashed and placed with a new hash while the value should exists as s separate field as well which doesnt happen.
def test_for_value_as_a_field():
     message = {}
     message_service = MessageService()
     message["_hash"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
     assert message["_hash"] in received

### CASE: Hash with different data type
## Hash with integer or diff type
def test_for_value_as_a_int():
     with pytest.raises(Exception) as e:
     	message = {}
     	message_service = MessageService()
     	message["_hash"] = 12345
     	message_service.enqueue(json.dumps(message))
     	received = json.loads(message_service.next(1))

### CASE: hash for different encoded string
## hash with already encoded string
def test_with_already_encoded_string():
     message = {}
     message_service = MessageService()
     message["_hash"] = "{'(`This is Query Corporation`)'}"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]

### CASE: multiple key value pairs with hash
def test_for_all_key_values():
     message = {}
     message_service = MessageService()
     message["_hash"] = "name"
     message["name"] = "Query"
     message["num"] = 1312313
     message["_num"] = 123
     message["_name"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
     assert received["name"] == message["name"][::-1]
     assert received["num"] == ~message["num"]
     assert received["_num"] == message["_num"]
     assert received["_name"] == message["_name"]

### CASE: multiple messages with HASH values - possible performace measure
def test_for_multiple_instances():
     import os
     n = 10000
     message_service = MessageService()
     for i in range(n):
         message = {}
         message["_hash"] = str(os.urandom(64))
         message["name"] = base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
         message_service.enqueue(json.dumps(message))
     for i in range(n):
          received = json.loads(message_service.next(1))
          assert received["hash"] == received["name"]

### CASE: already existing hash field
def test_for_already_existing_hash_field():
     message = {}
     message_service = MessageService()
     message["_hash"] = "name"
     message["hash"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message["_hash"]
