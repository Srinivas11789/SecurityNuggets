########## Multi Threading

# Python Library Import
import sys, json, random, base64, hashlib, threading

# Path Setting
if sys.path[0]:
    sys.path.insert(0,sys.path[0]+'/../')
else:
    sys.path.insert(0, '/../')

# Custom Module Import
from q.message_service import MessageService

# BUG12 in design - Multi threading - Queue Empty received
# Based on the documentation of the queue module, the implementation of queue in the library is kept thread safe, even though the design leverages the library for such a condition, there should be a probably safe locks or semaphores included to keep the program safe

###### CASE: Thread trigger for enqueue and dequeue in separate threads
def continuous_message_enqueue(message_service, number):
    for i in range(number):
        message = {}
        message["num"] = random.randint(0,1000000)
        message["_check"] = "Thread"
        message_service.enqueue(json.dumps(message))

def continuous_message_dequeue(message_service, number):
    for i in range(number):
        message = message_service.next(3)
        assert json.loads(message)["_check"] == "Thread"

def test_send_receive_separate_threads():

    message_service = MessageService()

    # Creating Threads
    thread1 = threading.Thread(target=continuous_message_enqueue, args=(message_service, 1000,))
    thread2 = threading.Thread(target=continuous_message_dequeue, args=(message_service, 1000,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("!!!")

##### CASE: enqueue/dequeue multiple messages in multiple threads
def continuous_send_receive1(message_service, number):
    for i in range(number):
        message = {}
        message["num"] = random.randint(0,1000000)
        message["name"] = "Query"
        message["_check"] = "Thread"
        message_service.enqueue(json.dumps(message))
    for i in range(number):
        message = message_service.next(2)
        assert json.loads(message)["_check"] == "Thread"
        assert json.loads(message)["name"] == "yreuQ"

def continuous_send_receive2(message_service,number):
    for i in range(number):
        message = {}
        message["num"] = random.randint(0,1000000)
        message["_check"] = "Thread"
        message_service.enqueue(json.dumps(message))
        received = message_service.next(3)
        assert json.loads(received)["_check"] == "Thread"

def test_multi_send_receive_separate_threads():
    message_service = MessageService()

    # Creating Threads
    thread1 = threading.Thread(target=continuous_send_receive1, args=(message_service, 100000,))
    thread2 = threading.Thread(target=continuous_send_receive2, args=(message_service, 100000,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("!!!")

##### CASE: Threaded enqueue and main thread dequeue execution
def test_thread_send_main_receive():
    message_service = MessageService()

    # Creating Threads
    thread1 = threading.Thread(target=continuous_message_enqueue, args=(message_service, 100000,))

    thread1.start()
    for i in range(100000):
        message = message_service.next(3)
        assert json.loads(message)["_check"] == "Thread"

    print("!!!")

### Driver
#def main():
#     #test_send_receive_separate_threads()
#     #test_multi_send_receive_separate_threads()
#     test_thread_send_main_receive()

#main()
