# Messaging Service Queue Tests - BlackBox

# Module Imports

# * Framework
import unittest

import json, queue, hashlib, base64

# This program wont work unless there is a message service program
# * Message Service
from query.message_service import MessageService

# Test the outlined functionality or work flow - Smoke or Sanity - Positive test - basic work flow cases - input->transformation->dispatch->output

class TestBasicUseCase(unittest.TestCase):

    # Test setup
    def setUp(self):
        self.message = {}
       	self.message_service = MessageService()

    # Basic test case 1:
    # Description -
    # * Query in value of a message should be reversed and placed in queue 2
    # Expected -
    # * Query value should be reversed and available at queue2
    ## BUG1
    def test_transformation_reverse(self):
        self.message["name"] = "This is Query Corporation"
        self.message_service.enqueue(json.dumps(self.message))
        try:
           self.assertEqual(json.loads(self.message_service.next(2))["name"], self.message["name"][::-1])
        except:
           self.fail("message_service raised empty queue exception for rule: string_reverse(Query) == queue(2)")

    # =====> Failure - Bug1 ==> the message is available at queue 4 rather than queue 2

    # Basic test case 2:
    # Description -
    # * Integer in the value of the message, should be bit negated and dispatched at queue 3
    # Expected -
    # * Integer in the value should be equal to bit negated and available at queue 3
    def test_transformation_integer(self):
        self.message["num"] = 200
        self.message_service.enqueue(json.dumps(self.message))
        try:
           self.assertEqual(json.loads(self.message_service.next(3))["num"], ~self.message["num"])
        except:
           self.fail("message_service raised empty queue exception for rule: int(num) == ~num")

    # Basic test case 3:
    # Description -
    # * Hash field should hash the value and dispatch in queue 1
    # Expected -
    # * hash(value) should be present in the field with key: _hash and dispatched at queue 1
    def test_transformation_hash(self):
        self.message["_hash"] = "srinivas"
        self.message_service.enqueue(json.dumps(self.message))
        try:
           self.assertEqual(json.loads(self.message_service.next(1))["hash"], base64.b64encode(hashlib.sha256(self.message["_hash"].encode('utf-8')).digest()).decode('utf-8'))
        except:
           self.fail("message_service raised empty queue exception for rule: _hash:value == _hash:base64(sha256(utf8(value)))")

    # Basic test case 4:
    # Description -
    # * Special values should start with "_" && not be applied any transformation && dispatched at queue 0
    # Expected -
    # * special fields should not be applied any transformation, start with "_" and dispatched at queue 0
    def test_transformation_special(self):
        self.message["_special"] = "srinivas"
        self.message_service.enqueue(json.dumps(self.message))
        try:
            self.assertEqual(json.loads(self.message_service.next(0))["_special"], self.message["_special"])
        except:
           self.fail("message_service raised empty queue exception for rule: _special == no transformation")

    # Basic test case 5:
    # Description -
    # * Sequence of messages should be output correspondingly
    # Expected -
    # * sequence of messages - seq 0 tranformation should be applied and dispatch at seq0 queue in order should be obtained
    def test_transformation_sequence(self):
        self.message1 = {}
        self.message2 = {}
        self.message["sequence"] = 0
        self.message["num"] = 123
        self.message1["sequence"] = 1
        self.message1["num"] = 345
        self.message2["sequence"] = 0
        self.message2["num"] = 678
        self.message_service.enqueue(json.dumps(self.message))
        self.message_service.enqueue(json.dumps(self.message1))
        self.message_service.enqueue(json.dumps(self.message2))
        try:
            self.assertEqual(json.loads(self.message_service.next(3))["num"], ~self.message["num"])
            self.assertEqual(json.loads(self.message_service.next(3))["num"], ~self.message2["num"])
            self.assertEqual(json.loads(self.message_service.next(3))["num"], ~self.message1["num"])
        except:
            self.fail("message_service raised empty queue exception for rule: _special == no transformation")

    # Basic test case 6:
    # Description -
    # * Part of messages should be output correspondingly
    # Expected -
    # * Part of messages - part 0 seq0 tranformation should be applied and dispatch at seq0 queue in order should be obtained
    def test_transformation_parts(self):
        self.message1 = {}
        self.message2 = {}
        self.message["_sequence"] = 0
        self.message["_part"] = 0
        self.message["num"] = 123
        self.message1["_sequence"] = 0
        self.message1["_part"] = 1
        self.message1["num"] = 345
        self.message2["_sequence"] = 0
        self.message2["_part"] = 2
        self.message2["num"] = 678
        self.message_service.enqueue(json.dumps(self.message))
        self.message_service.enqueue(json.dumps(self.message1))
        self.message_service.enqueue(json.dumps(self.message2))
        try:
            self.assertEqual(json.loads(self.message_service.next(3))["_part"], self.message["_part"])
            self.assertEqual(json.loads(self.message_service.next(3))["_part"], self.message1["_part"])
            self.assertEqual(json.loads(self.message_service.next(3))["_part"], self.message2["_part"])
        except:
            self.fail("message_service raised empty queue exception for rule: parts")

    # Test tear down
    def tearDown(self):
        self.message = {}
        self.message_service = None


if __name__ == '__main__':
    unittest.main()
