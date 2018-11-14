# Test transformation num - bitwise negation

# Python Library Import
import sys, json, random

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

# CASE: basic test for integer
def test_basic_case_of_any_number():
     message = {}
     message_service = MessageService()
     message["num"] = random.randint(1,10000)
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(3))["num"] == ~message["num"]

# CASE: long integer occurrence - possible python2 bug if the tool is run in python2
# There is no long integer in python3, the same case would fail for python 2
def test_large_int_bounds():
     n = 6000000000000000000000000000001
     message = {}
     message_service = MessageService()
     message["num"] = n
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(3))["num"] == ~message["num"]

# CASE: negative integer occurrence
def test_negative_int():
     message = {}
     message_service = MessageService()
     message["num"] = -random.randint(1,10000)
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(3))["num"] == ~message["num"]
    
# CASE: Sceanrio of already negated number
def test_bitwise_negated_number():
     message = {}
     message_service = MessageService()
     message["num"] = ~random.randint(1,10000)
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(3))["num"] == ~message["num"]

# CASE: Test for floating point numbers
def test_float():
     message = {}
     message_service = MessageService()
     message["num"] = 10000.00000
     message_service.enqueue(json.dumps(message))
     assert json.loads(message_service.next(4))["num"] == message["num"]

# BUG13
# CASE: test for infinite numbers
def test_infinity_int():
    n = float('inf')
    message = {}
    message_service = MessageService()
    message["num"] = n
    message_service.enqueue(json.dumps(message))
    assert json.loads(message_service.next(4))["num"] == message["num"]

# CASE: multiple occurrence of a number
def test_multiple_occurences():
    n = 100
    message = {}
    message_service = MessageService()
    for i in range(n):
    	message["num"+str(i)] = random.randint(1,1000000000000)
    message_service.enqueue(json.dumps(message))
    received_message = message_service.next(3)
    for i in range(n):
    	assert json.loads(received_message)["num"+str(i)] == ~message["num"+str(i)]



