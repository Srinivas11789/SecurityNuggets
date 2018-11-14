# Test Query string reverse

# Python Library Import
import sys, json

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

### CASE: Query in substring
# BUG 1
def test_sentence_with_Query_substring():
     message = {}
     message_service = MessageService()
     message["name"] = "This is Query Corporation"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(2))["name"] == message["name"][::-1]

### CASE: multiple occurences of Query string
def test_large_occurences_of_Query_in_different_keys():
     n = 10000
     message = {}
     message_service = MessageService()
     message["name"] = "This is Query Corporation"
     for i in range(n):
         name = "name"+str(i)
         if name not in message:
            message[name] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     for i in range(n):
     	assert received["name"+str(i)] == message["name"+str(i)][::-1]

### CASE: Reverse string included with Query
# Due to BUG1
def test_string_including_string_reverse_within():
     message = {}
     message_service = MessageService()
     message["name"] = "QueryyreuQ"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     assert received["name"] == message["name"][::-1]

### CASE: Large string with Query sub string
# Due to BUG1
def test_very_long_string_with_Query():
     message = {}
     message_service = MessageService()
     message["name"] = "A"*1000000+""*100000+"Query"+"Q"*1000
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     assert received["name"] == message["name"][::-1]

### CASE: lower case Query occurrence
def test_lower_case_Query_substring():
     message = {}
     message_service = MessageService()
     message["name"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(4))
     assert received["name"] == message["name"]

### CASE: Malformed Query string existence
# Due to BUG1
def test_string_with_quotes1():
     message = {}
     message_service = MessageService()
     message["name"] = "'Query'"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     assert received["name"] == message["name"][::-1]

### CASE: Malformed Query string existence
# Due to BUG1
def test_string_with_quotes2():
     message = {}
     message_service = MessageService()
     message["name"] = "`Query`"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(2))
     assert received["name"] == message["name"][::-1]

### CASE: private field with Query
def test_string_with_private_field():
     message = {}
     message_service = MessageService()
     message["_name"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = json.loads(message_service.next(4))
     assert received["_name"] == message["_name"]
