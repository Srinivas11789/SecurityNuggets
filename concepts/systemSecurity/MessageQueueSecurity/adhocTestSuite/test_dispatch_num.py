# Adhoc test of dispatch rule <num>

# Python Library Import
import sys, json, random, base64, hashlib

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

# CASE: Evaluate integer only field
def test_only_num_field():
     message = {}
     message_service = MessageService()
     message["num"] = int("123")
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(3))["num"] == ~message["num"]

# CASE: Evaluate integer type field with float values
def test_num_float_field():
     message = {}
     message_service = MessageService()
     message["num"] = 22.22
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["num"] == message["num"]

# CASE: Evaluate integer field with preceding dispatch rules
## Fails due to BUG1
def test_num_field_with_other_preceding_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["name"] = "QQuery"
     message["num"] = 123131
     message_service.enqueue(json.dumps(message))
     received = message_service.next(2)
     assert json.loads(received)["num"] == ~message["num"]
     assert json.loads(received)["name"] == message["name"][::-1]

# CASE: Evaluate integer firlds with post dispatch rules
def test_num_field_with_other_post_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["num"] = 10000
     message["name"] = "Quuery"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(3)
     assert json.loads(received)["name"] == message["name"]
     assert json.loads(received)["num"] == ~message["num"]
