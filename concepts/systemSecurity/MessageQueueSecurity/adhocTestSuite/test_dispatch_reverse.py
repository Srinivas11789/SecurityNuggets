# Adhoc test of dispatch rule <Query reversing>

# Python Library Import
import sys, json, random, base64, hashlib

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService


# BUG1 - dispatch checks for rev("Query") in list of values hence it will only match rev("Query") found but not a big string with Query
# CASE: Query string value only
def test_only_Query_field():
     message = {}
     message_service = MessageService()
     message["name"] = "Query - look into the internet - Query"
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(2))["name"] == message["name"][::-1]

# CASE: Query string as value with preceding rules
def test_Query_field_with_other_preceding_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["_special"] = "Query"
     message["name"] = "Query - look into the internet - Query"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(0)
     assert json.loads(received)["name"] == message["name"][::-1]
     assert json.loads(received)["_special"] == message["_special"]

# CASE: Query string as value with post rules
def test_Query_field_with_other_preceding_dispatch_rule():
     message = {}
     message_service = MessageService()
     message["num"] = 10000
     message["name"] = "Query"
     message_service.enqueue(json.dumps(message))
     received = message_service.next(2)
     assert json.loads(received)["name"] == message["name"][::-1]
     assert json.loads(received)["num"] == ~message["num"]
