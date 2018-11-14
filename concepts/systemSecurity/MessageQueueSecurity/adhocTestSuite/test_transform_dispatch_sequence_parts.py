# Test Sequence/Parts in message ==> full workflow from transform ---> dispatch

# Python Library Import
import sys, json, hashlib, base64, pytest

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

"""
## Idea for sequence/parts => Different sequences
# Same sequence different order
# differnet seq diff order
# different seq same order
# same sequence - multiple same parts- duplicate
# one after zero part number
"""

### Initialize Function : creates same sequence message with five parts and returns them
def init_same_sequence_five_parts(sequence):

     # Same sequence with upto 5 parts

     # Sequence - "Q1"; Parts - 0
     message0 = {}
     message0["_sequence"] = sequence
     message0["_part"] = 0
     message0["_hash"] = "This is Query Corporation"
     message0["name"] = "Query Inc"

     # Sequence - "Q1"; Parts - 1
     message1 = {}
     message1["_hash"] = "Query Inc."
     message1["_private"] = "Query Inc."
     message1["name"] = "Query Inc."
     message1["num"] = 1234
     message1["_special"] = "Wwww"
     message1["_sequence"] = sequence
     message1["_part"] = 1

     # Sequence - "Q1"; Parts - 2
     message2 = {}
     message2["_private"] = "Query Inc."
     message2["name"] = "Query"
     message2["num"] = 1234
     message2["__hash"] = "Query Inc."
     message2["_sequence"] = sequence
     message2["_part"] = 2

     # Sequence - "Q1"; Parts - 3
     message3 = {}
     message3["_private"] = "Query Inc."
     message3["_name"] = "Qadiium Inc."
     message3["_num"] = 1234
     message3[" _"] = "______"
     message3["_sequence"] = sequence
     message3["_part"] = 3

     # Sequence - "Q1"; Parts - 4
     message4 = {}
     message4["_private"] = "Query Inc."
     message4["_name"] = "Qadiium Inc."
     message4["num"] = 1234
     message4[" _"] = "______"
     message4["_sequence"] = sequence
     message4["_part"] = 4

     return message0,message1,message2,message3,message4

### CASE: same sequence message with various parts orderly
def test_with_same_sequence_various_parts():

     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message1))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message4))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

### CASE: same sequence message with different order of parts
def test_same_sequence_different_order_of_parts():

     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

### CASE: same sequence message with different order of parts, with initial message present at the last
# BUG3 => First message being sent re-ordered for a sequence fails
def test_same_sequence_different_order_of_zero():

     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message1))
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message0))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

### CASE: Different sequence message with different parts
def test_different_sequence_different_order_different_queue():

     message_service = MessageService()
     # Same sequence with upto 5 parts

     message00, message01, message02, message03, message04 = init_same_sequence_five_parts("Q1")
     message10, message11, message12, message13, message14 = init_same_sequence_five_parts("Q2")

     # changing queue
     message10, message11 = message11, message10
     message10["_part"] = 0
     message11["_part"] = 1

     # Sending all the messages

     message_service.enqueue(json.dumps(message00))
     message_service.enqueue(json.dumps(message04))
     message_service.enqueue(json.dumps(message03))
     message_service.enqueue(json.dumps(message10))
     message_service.enqueue(json.dumps(message12))
     message_service.enqueue(json.dumps(message11))
     message_service.enqueue(json.dumps(message02))
     message_service.enqueue(json.dumps(message01))
     message_service.enqueue(json.dumps(message14))
     message_service.enqueue(json.dumps(message13))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message00["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message00["_hash"]
     assert received["name"] == message00["name"][::-1]
     assert received["_sequence"] == message00["_sequence"]
     assert received["_part"] == message00["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message01["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message01["_hash"]
     assert received["name"] == message01["name"][::-1]
     assert received["num"] == ~message01["num"]
     assert received["_private"] == message01["_private"]
     assert received["_special"] == message01["_special"]
     assert received["_sequence"] == message01["_sequence"]
     assert received["_part"] == message01["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message02["__hash"]
     assert received["name"] == message02["name"][::-1]
     assert received["num"] == ~message02["num"]
     assert received["_private"] == message02["_private"]
     assert received["_sequence"] == message02["_sequence"]
     assert received["_part"] == message02["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message03["_name"]
     assert received["_num"] == message03["_num"]
     assert received["_private"] == message03["_private"]
     assert received["_sequence"] == message03["_sequence"]
     assert received["_part"] == message03["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message04["_name"]
     assert received["num"] == ~message04["num"]
     assert received["_private"] == message04["_private"]
     assert received[" _"] == message04[" _"]
     assert received["_sequence"] == message04["_sequence"]
     assert received["_part"] == message04["_part"]

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message10["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message10["_hash"]
     assert received["name"] == message10["name"][::-1]
     assert received["_sequence"] == message10["_sequence"]
     assert received["_part"] == message10["_part"]

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message11["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message11["_hash"]
     assert received["name"] == message11["name"][::-1]
     assert received["_sequence"] == message11["_sequence"]
     assert received["_part"] == message11["_part"]

     received = json.loads(message_service.next(0))
     assert received["__hash"] == message12["__hash"]
     assert received["name"] == message12["name"][::-1]
     assert received["num"] == ~message12["num"]
     assert received["_private"] == message12["_private"]
     assert received["_sequence"] == message12["_sequence"]
     assert received["_part"] == message12["_part"]

     received = json.loads(message_service.next(0))
     assert received["_name"] == message13["_name"]
     assert received["_num"] == message13["_num"]
     assert received["_private"] == message13["_private"]
     assert received["_sequence"] == message13["_sequence"]
     assert received["_part"] == message13["_part"]

     received = json.loads(message_service.next(0))
     assert received["_name"] == message14["_name"]
     assert received["num"] == ~message14["num"]
     assert received["_private"] == message14["_private"]
     assert received[" _"] == message14[" _"]
     assert received["_sequence"] == message14["_sequence"]
     assert received["_part"] == message14["_part"]

### CASE: Duplicate parts of the message handling
# Duplicate messages of same priority
def test_duplicate_same_parts_messages():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message3))
     message3["_num"] = 3456
     message_service.enqueue(json.dumps(message3))
     message3["_num"] = 7890
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == 1234
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == 3456
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]


### CASE: Parts of messages sent after a brief break
def test_dont_wait():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

### CASE: different sequence, differnt parts ending up in the same queue
# Same queue, different seq, different parts
def test_same_queue_different_seq_and_parts():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message00, message01, message02, message03, message04 = init_same_sequence_five_parts("Q1")
     message10, message11, message12, message13, message14 = init_same_sequence_five_parts("Q2")

     # Sending all the messages

     message_service.enqueue(json.dumps(message00))
     message_service.enqueue(json.dumps(message04))
     message_service.enqueue(json.dumps(message03))
     message_service.enqueue(json.dumps(message10))
     message_service.enqueue(json.dumps(message12))
     message_service.enqueue(json.dumps(message11))
     message_service.enqueue(json.dumps(message02))
     message_service.enqueue(json.dumps(message01))
     message_service.enqueue(json.dumps(message14))
     message_service.enqueue(json.dumps(message13))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message00["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message00["_hash"]
     assert received["name"] == message00["name"][::-1]
     assert received["_sequence"] == message00["_sequence"]
     assert received["_part"] == message00["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message10["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message10["_hash"]
     assert received["name"] == message10["name"][::-1]
     assert received["_sequence"] == message10["_sequence"]
     assert received["_part"] == message10["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message01["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message01["_hash"]
     assert received["name"] == message01["name"][::-1]
     assert received["num"] == ~message01["num"]
     assert received["_private"] == message01["_private"]
     assert received["_special"] == message01["_special"]
     assert received["_sequence"] == message01["_sequence"]
     assert received["_part"] == message01["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message11["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message11["_hash"]
     assert received["name"] == message11["name"][::-1]
     assert received["_sequence"] == message11["_sequence"]
     assert received["_part"] == message11["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message02["__hash"]
     assert received["name"] == message02["name"][::-1]
     assert received["num"] == ~message02["num"]
     assert received["_private"] == message02["_private"]
     assert received["_sequence"] == message02["_sequence"]
     assert received["_part"] == message02["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message12["__hash"]
     assert received["name"] == message12["name"][::-1]
     assert received["num"] == ~message12["num"]
     assert received["_private"] == message12["_private"]
     assert received["_sequence"] == message12["_sequence"]
     assert received["_part"] == message12["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message03["_name"]
     assert received["_num"] == message03["_num"]
     assert received["_private"] == message03["_private"]
     assert received["_sequence"] == message03["_sequence"]
     assert received["_part"] == message03["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message13["_name"]
     assert received["_num"] == message13["_num"]
     assert received["_private"] == message13["_private"]
     assert received["_sequence"] == message13["_sequence"]
     assert received["_part"] == message13["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message04["_name"]
     assert received["num"] == ~message04["num"]
     assert received["_private"] == message04["_private"]
     assert received[" _"] == message04[" _"]
     assert received["_sequence"] == message04["_sequence"]
     assert received["_part"] == message04["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message14["_name"]
     assert received["num"] == ~message14["num"]
     assert received["_private"] == message14["_private"]
     assert received[" _"] == message14[" _"]
     assert received["_sequence"] == message14["_sequence"]
     assert received["_part"] == message14["_part"]

################# SCENARIO: Negative or Hacky Edge cases

### CASE: Sequence data type change
def test_sequence_data_type_change():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts(1)

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

# CASE: part data type change
# BUG4: part data type change
def test_part_data_type_change():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     message0["_part"] = "a"
     message1["_part"] = "b"
     message2["_part"] = "c"
     message3["_part"] = "d"
     message4["_part"] = "e"

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(1))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]

# CASE: no initial message found
# BUG5: No first sequence or 1 being the first sequence
def test_no_first_sequence():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(0))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(0))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(0))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]


### CASE: Duplicate initial message occurrence
## BUG6 - Duplicate initial sequence -  can go both ways
# Duplicate 0 sequence
# same case with dont wait
def test_duplicate_zero():
     message_service = MessageService()
     # Same sequence with upto 5 parts

     message0, message1, message2, message3, message4 = init_same_sequence_five_parts("Q1")

     # Sending all the messages

     message_service.enqueue(json.dumps(message0))
     message0["_special"] = "Hi"
     message_service.enqueue(json.dumps(message4))
     message_service.enqueue(json.dumps(message3))
     message_service.enqueue(json.dumps(message0))
     message_service.enqueue(json.dumps(message2))
     message_service.enqueue(json.dumps(message1))

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]
     assert received["_special"] == message0["_special"]

     received = json.loads(message_service.next(1))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message0["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message0["_hash"]
     assert received["name"] == message0["name"][::-1]
     assert received["_sequence"] == message0["_sequence"]
     assert received["_part"] == message0["_part"]

     received = json.loads(message_service.next(0))
     assert received["hash"] == base64.b64encode(hashlib.sha256(message1["_hash"].encode('utf-8')).digest()).decode('utf-8')
     assert received["_hash"] == message1["_hash"]
     assert received["name"] == message1["name"][::-1]
     assert received["num"] == ~message1["num"]
     assert received["_private"] == message1["_private"]
     assert received["_special"] == message1["_special"]
     assert received["_sequence"] == message1["_sequence"]
     assert received["_part"] == message1["_part"]

     received = json.loads(message_service.next(0))
     assert received["__hash"] == message2["__hash"]
     assert received["name"] == message2["name"][::-1]
     assert received["num"] == ~message2["num"]
     assert received["_private"] == message2["_private"]
     assert received["_sequence"] == message2["_sequence"]
     assert received["_part"] == message2["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message3["_name"]
     assert received["_num"] == message3["_num"]
     assert received["_private"] == message3["_private"]
     assert received["_sequence"] == message3["_sequence"]
     assert received["_part"] == message3["_part"]

     received = json.loads(message_service.next(1))
     assert received["_name"] == message4["_name"]
     assert received["num"] == ~message4["num"]
     assert received["_private"] == message4["_private"]
     assert received[" _"] == message4[" _"]
     assert received["_sequence"] == message4["_sequence"]
     assert received["_part"] == message4["_part"]
