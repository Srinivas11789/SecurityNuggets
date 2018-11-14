### Fuzz, Scale and Memory Tests

# Python Library Import
import sys, json, random, base64, hashlib, pytest

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

########## Fuzz Inputs - Targeted Fuzzing

### Fuzz Logic --->
# * A basic fuzzer logic implemented in the given duration to fuzz the inputs. A minimal implementation of a fuzzing logic

# Poet - Craft the inputs based on the criteria of selection
# * 1. Message being a object differing to the json object such that json loads fails
# * 2. A Json object with irrelevant fields data

# Courier
# The provision from the program to access the messaging service object would be the courier to deliver the payload

# Oracle
# * Decision based on the output received

# BUG7 - Malformed input or irrelevant input
# A json debugger exception is thrown, based on the parser of the json module, in such cases the internals of the program are thrown as exception leading due visibility of possible design and function or library usages, which could be a possible cause of discovering any vulnerabilities or instabilities.
def test_message_service_malformed_input():
    with pytest.raises(Exception) as e:
       message_service = MessageService()
       message = {"name":"Query"}
       message_service.enqueue(message)
    assert "ValueError" in str(e)

# BUG7 - Malformed or irrelevant input
def test_message_service_malformed_input2():
    with pytest.raises(Exception) as e:
       message_service = MessageService()
       message = {"name":"Query"}
       message_service.enqueue(str(message))
    assert "ValueError" in str(e)

# BUG9 - Hangs the python interpreter for 100000000000, Also tried with the raw interpreter as well, seems to be a pythonic issue of overflow
def test_message_service_malformed_key():
    message_service = MessageService()
    key = "A"*100000#100000000000
    message = {key:"Qadiui"}
    message_service.enqueue(json.dumps(message))
    assert json.loads(message_service.next(4))[key] == "Qadiui"

# CASE - empty message object
def test_message_service_empty_input():
    message_service = MessageService()
    message = {}
    message_service.enqueue(json.dumps(message))
    assert json.loads(message_service.next(4)) == {}

# CASE - Non existing queue - negative
# BUG8 - Non exising queue, when greater than 5 is specified raises indexError (expected) but lesser than 0 is not checked
def test_message_service_nonexisting_queue():
    with pytest.raises(Exception) as e:
      message_service = MessageService()
      message = {"_name":"Www"}
      message_service.enqueue(json.dumps(message))
      message_service.next(-5)
    assert "IndexError" in str(e)

"""
########## MEMORY
########## Memory Errors ---> BUG10

# transformation engine - For some transformation conditions like, Query string reverse and numbers, a separate dictionary is replicated each time even though parsed dictionary is already present. When message objects gets larger this might consume much of the memory in a production environment as they are replicated for each message entering the queue. This might exhaust the memory and cause memory hogging and exhaustion.

# Occurence at,

    def reverse_strings_with_Query(self, parsed_json):
        transformed_json = OrderedDict()
        for k, v in parsed_json.items():
            if not is_private_field(k) and isinstance(v, str) and "Query" in v:
                transformed_json[k] = v[::-1]
            else:
                transformed_json[k] = v
        return transformed_json

    def bitwise_negation(self, parsed_json):
        transformed_json = OrderedDict()
        for k, v in parsed_json.items():
            if not is_private_field(k) and isinstance(v, int):
                transformed_json[k] = ~ v
            else:
                transformed_json[k] = v
        return transformed_json
"""
############ SCALE Cases ---> Reduced the scale cases as they take time to execute

### Fill the message buffer with numerous messages and very large messages

# * A simple implementation of very large message, passes but takes quite long time
def test_large_messages():
    message_service = MessageService()
    message = {}
    message["_spl"] = "Query"
    for i in range(1000):
        o = random.randint(65,90)
        key = chr(o)*10000 #chr((60+i)%256)*100000
        value = chr(o+1)*10000
        message[key] = value
    message_service.enqueue(json.dumps(message))
    assert json.loads(message_service.next(4))["_spl"] == "Query"

# * A simple implementation of numerous messages which are sufficiently large as well

def test_large_quantity_large_messages():
    message_service = MessageService()
    for j in range(1000):
       message = {}
       message["_spl"] = "Query"
       for i in range(1000):
          o = random.randint(65,90)
          key = chr(o)*100000 #chr((60+i)%256)*100000
          value = chr(o+1)*100000
          message[key] = value
       message_service.enqueue(json.dumps(message))
    for k in range(1000):
       assert json.loads(message_service.next(4))["_spl"] == "Query"
