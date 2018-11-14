# Challenge
### Information about the bugs and enhancements are mentioned at the tail end of this document.

### Name : Srinivas Piskala Ganesh Babu

### The Problem:
* Asses a Message queue for any security vulnerability/bugs.
* The message queue accepts a message json, applies some transformation rules and adds properties to the message object, dispatches the message in various queue depending on some properties.
**What can go wrong?**

### The Problem Outline: Detailed overview

* Implement a message service queue, that takes input -> performs transformation -> filters using dispatch rules -> respective message queue -> output

* Parts:
  * **Input** -> Enqueue(msg <JSON String>)
  * **Transformation Rules** ->
    * String reverse - <value> == Any `Query` string
    * Bitwise negate - <value> == Any integer
    * Hashing(value) - <key>   ==  _hash - base64(sha256(unicode(value)))
    * Ignore fields  - <key>   == _string_ private fields
    * Sequence/Part  - <k,v>   == arrange properly in queue
  * **Displatch Rules** ->
    * Queue 0 = <key>   == special
    * Queue 1 = <key>   == _hash
    * Queue 2 = <value> == rev(`Query`)
    * Queue 3 = <value> == integer
    * Queue 4 = <k,v>   == Other
    * Sequence/Part - <k,v> == seq(0) rules should apply
  * **Output** -> next(queue number 0-4) for the message

### Project Design:
    <notes.pdf> - random idea sketch in notes.pdf included in the folder.

### Paranoia -> Thoughts on the testcases or what can go wrong:

    ** * Spot vulnerable points based on the requirement:**

    * Input:
        * empty input scenario
        * threaded input feed
        * improper ordering of sequence/ part messages
    * key/value pair cases:
    	* string reverse of a large string or any string containing `Query`
    	* string reverse of `Query` string with potential reserved keys like hash
    	* bitwise negation - number like float and large numbers outside the integer range
    	* hashing - string or integer + already encoded string
    	* sequence/part - message broken into large tiny ones - same seq diff parts, same parts diff sequence
    	* special key existence
    * Flow based cases:
        * dispatcher
          * improper ordering of sequences
          * improper ordering of parts
          * hierarchical ordering - sequential dispatching cases for existence of top layer like special vs int
          * dispatching vs enqueue in parallel to access the queue elements (locks)
    * output cases:
        * exception of empty queue gracefully
        * accessing empty queue at the same time - thread condition
        * unknown queue number
        * sequential/ part messages

### Code Flow and Understanding:
    <notes.pdf> - has abstracted description of functionality of each files
    * tranformation_engine.py
      * validate message object
      * function provision to reverse `query` string included
      * function provision to bitwise negate the integer
      * function provision to segregate private fields without modification
      * function provision to handle sequence/parts logic using priority queue
    * dispatcher.py
      * Rules of dispatch applied in order _special, hash, reverse, integer, others
      * function provisions to check for the rules and apply the queue number
    * helper.py
      * Segregate the private and the normal fields
      * Filter the private fields when necessary
    * messaging_service.py
      * driver for transform and dispatch functions
      * implements the enqueue and next functionality
    * solution.py
      * performs a driver for the whole app, returns the messaging service object

### Analysis + Paranoia -> Filtered and more legit Thoughts on the testcases or what can go wrong:
    * Memory        : Message object copied more than once for an operation in transformation <tranform: reverse, num>, which could lead to memory exhaustion
    * Security      : Input is not sanitized/filtered properly, trust of the input should be questioned and proper exception handlers and filter should be added before processing
    * MultiThreading: A single queue is operated for both message enqueue and dequeue which might cause race condition when numerous messages are exchanged in a multi processing environment.
                      Safety locks or minimal semaphores of stop/wait or lock/unlock logic for the queue should be constructed
    * Functionality :
      - Dispatch Rule => only reverse("Query") is checked for the dispatch rule rather than checking for substring "yreuQ" in the full string
      - Dispatch rule for Private fields not applied for integer rule

### Automation:
    * Framework - resorting to default python libraries and framework - <unittest> and <pytest>
    * blackBoxTestSuite: Automation Framework Used --> Unittest
      - Without looking at the code and functions, designed some testcases based on the README instructions.
      - Smoke or Sanity - Full workflow testbed logic <input => tranform => dispatch => output> --> to perform basic checks based on the functionality perceived from the readme
      - File => blackBoxTestSuite.py  
    * adhocTestSuite: Automation Framework Used --> pytest
      - Analysis of the code, design and more detailed instructions from the readme to write specific cases for each of the criteria
      - Each rule in the README has a seprate file for transformation and dispatch
        - Transformation Engine
          * test_transform_reverse - "`Query`" string reverse
          * test_transform_num     - bitwise negation
          * test_transform_private - private fields should not undergo any change
          * test_transform_hash    - hash the value of "_hash" and a new hash fields to be generated
          * test_transform_dispatch_sequence_parts - check sequence/parts of a message ordered correctly
          * test_transform_multiple - check multiple transformations in a message
        - Dispatch Rules
          * test_dispatch_reverse - dispatch rule for `Query` reverse string
          * test_dispatch_num - dispatch rule for integer existence
          * test_dispatch_private - dispatch rule for private fields
          * test_dispatch_hash - dispatch rule for hashes present
          * test_dispatch_special - dispatch rule for special fields
          * test_dispatch_rule_order - dispatch rule ordering (precedence or priority as in the readme)
        - Sequence/Part test
          * test_transform_dispatch_sequence_parts - sequence/part tests
        - Fuzz, Scale, Hacky/Negative tests
          * test_fuzz_and_memory.py - repetitive copying of the message can lead to memory exhaust, exception handler missing and input not sanitized properly
          * test_multi_threading.py - check for multi threading errors (no locks or semaphores were used and operations were performed in same queue)

    * Running the testSuite ->
      * The test suite assumes there is a q/ folder holding all the application files
      * blackBoxTestSuite.py ==> python3 blackBoxTestSuite.py
      * adhocTestSuite/      ==> python3 -m pytest adhocTestSuite/

### BUGS Encountered ->

    * BUG 1 => Dispatch rule is not applied for "yreuQ" as a substring
      - Description  : * Dispatch rule for "yreuQ" should check for any "yreuQ" included in the string eg. <"yreuQ"> or <"yreuQ cnI">
      - Steps        : * Create a field with value "`Query` Inc" in the message, enqueue the message and obtain the output from the queue
      - Expected     : * Any value with "yreuQ" included in the string should be routed to queue 2
      - Status       : Failed - "yreuQ" is only checked as a value in the list and not chceked when present in the sub string
      - Severity     : High

    * BUG 2 => Dispatch rule for private fields with integer is processed as well
      - Description  : * Dispatch rule should not be applied to private fields with underscore, for integer check in value, this check doesn't occur
      - Steps        : * Create a field with integer value and private key "_num", enqueue and expect to view in queue 4 as output.  
      - Expected     : * Any private field should not be applied any transformation rules and sent to queue 4 as they are private
      - Status       : Failed - private field with integer value is dispatched to queue 3 rather than 4
      - Severity     : High

    * BUG 3 => Sequence 0 message sent finally after other sequences 1,2,3.. causes program crash
      - Description  : * When the 0th part message of a sequence is sent later then any other message parts, then the program crahses
      - Steps        : * Send the messages part 1,2,3,4 first and then send part 0 <initial sequence>, dequeue based on initial part 0 message
      - Expected     : * The program should not crash, the behavior should be based on waiting either for initial message 0 in a group of messages or following the initial message in the group <least part value like part 1>.
      - Status       : Failed - The logic in the transform/dispatcher is based on assumption to have the initial part 0 message before other messages hence while accessing the corresponding priority the operation fails and program crashes
      - Severity     : High

    * BUG 4 => Parts with different data-type - A part field with string rather than Integer
      - Description  : * Part fields with string ids cause the program to break
      - Input        : * Construct a few messages with sequence/parts, and use string identifiers like "a","b","c"... for part fields. Enqueue the messages
      - Expected     : * The behavior could be concluded 2 ways, 1. throwing error for messages with string ids as the README suggests to have only integer for parts. 2. To explicitly convert the strings to numbers and use them
      - Status       : Failed - Crashes the program and fails
      - Severity     : Medium

    * BUG 5 => Initial part of the message not present, first sequence/part having value other than 0
      - Description  : When zero part message is not present the program fails
      - Input        : Construct group of messages with parts 1,2,3,4 without the part 0 and perform enqueue and dequeue
      - Expected     : The messages could follow the initial message being the least part message like "1" in this scenario rather than assuming "0" is present and failing
      - Status       : Failed - Program crashes. The code is hardcoded to "0" integer being the initial message rather than the least part value to be the initial message. For instance in a group of messages with 1,2,3,4 with no zero. The program fails
      - Severity     : High - as a security threat for collapsing the application

    * BUG 6 => Duplicate Initial Message <Part 0>, in a group of messages as well as between few group of messages
      - Description  : Duplicate "0" or initial part message in a group of messages causes the program to stick with the initial message sent at the beginning.
      - Input        : Create a set of message with parts 0,1,2 and another set of messages with 0,3,4, perform enqueue and dequeue
      - Expected     : The message part 0 obtaining at the beginning is taken into account. This can be argued as the new initial message with part 0 and same sequence again should have privilege and corresponding changes should be effected, but the message seems to have no effect
      - Status       : Failed - As of now, behavior sticks to the part0 message sent at the beginning, this behavior can be argued for priority of another part0 same sequence message sent to affect new changes
      - Severity     : Medium

    * BUG 7 => Malformed input - dict object or string input for a json message crashes the program
      - Description  : * When malformed input like a dictionary itself or a string is used rather than properly encoded json, the program crashes with Json decode error
      - Steps        : * Use a dictionary or any string as input and enqueue message
      - Expected     : * The input should be properly sanitized, before json decoding. As a security measure, the trust of the input should be questioned. The input should be properly filtered with exception handler and error messages before using it for processing. A trace like "Json decoding failed" and traceback of a list of errors would reveal internals of the application to the attacker. Such a long traceback should be handled.
      - Status       : Failed - A large error traceback is thrown with respect to json decoding failed allowing malicious user to perform social engineering of the application, library and internals used, that could be a source of vulnerability assessment.
      - Severity     : Medium

    * BUG 8 => Non-Existing Queue - Lesser than 0 is not handled, but values greater than 5 are handled and errors are thrown
      - Description  : * The non-existing queue check in messaging_service checks only for ">= 5" in range(0-5).It does not check for negative ranges of queue numbers
      - Steps        : * Provide a negative range number for queue number selection, which dequeue is performed.
      - Expected     : * Error message should be thrown that the corresponding queue does not exist similar to the index error thrown when queue number is ">=5"
      - Status       : Failed - No error message is thrown rather "Queue is empty" error is thrown considering the queue number being valid.
      - Severity     : Low

    * BUG 9 => String overflow hangs the messaging service
      - Description  : When a very very large string is used as a key or value in the message object, a large quantity of such a message leads to overflow errors. Such errors are not handled or identified. Of course this also occurs in the raw python interpreter as well.
      - Steps        : Create a message with very large string for keys and values and large quantity of such messages to be used in the app
      - Expected     : The messages if causes overflow errors within the app, should be handled and corresponding error should be thrown rather than crash or hang
      - Status       : Failed - Causes the app to hang and crash
      - Severity     : Low

    * BUG 10 => Possible Memory Issue due to duplication of message object
      - Description  : A number of message object copies are made using ordered dictionaries, especially at transformation_engine - <reverse_string_with_`Query`> and <bitwise_negation> which causes replica of already existing message object
      - Steps        : Create a message object, enqueue the object and look at the output. Performing this at a large scale might exhaust memory
      - Expected     : A single message object should be used and corresponding transformation should be performed rather than having replicas of the object
      - Status       : Failed - Might exhaust memory at a faster scale in production environments when a large scale users and messages exist for processing
      - Severity     : Low

    * BUG 11 => As readme suggests, "_hash" field value should be another field in the message object - This is not obeyed
      - Description  : The readme suggests, "The value of `_hash` will be the name of another field", this check is not evaluated nor a new field with the value is created
      - Input        : Create a message object with "_hash"  and perform transform/dispatch
      - Expected     : As readme suggests, a check should exist for the value of the _hash being another field or a new field is created corressponding to the value of the _hash field
      - Status       : Failed - No such check exists or a new field is created
      - Severity     : Low

    * BUG 12 => Possible Multi Threading Issue
      - Description  : Even though Queue library takes care of multi threading by default and a block=False check exists in the program,  sufficient locks or semaphores are not explicitly implemented in the program. When large traffic and processing occurs there might be chances of slipping into an multi threading issue
      - Input        : Create large amount of messages and enqueue+dequeue them
      - Expected     : No race condition should occur or no chances of any race condition should exist in the application. Rather than depending on the thread safety of a third party library, a minimal implementation of handling threads should exist within the application
      - Status       : Failed - No thread safety implemented in the code
      - Severity     : Low

    * BUG 13 => Float value being accepted
      - Description  : Float values being accepted even though the README mentions nothing about allowing float values
      - Input        : Create message object with float values and enqueue through the application
      - Expected     : Error is rasied as unknown data type as float values need not be handled by the application
      - Status       : Failed - No error raised for float values existence
      - Severity     : Low

### Possible Fixes + Ideas + Point of fixes -> PATCH

    * BUG 1 =>
      - Fix: Dispatch Rule - with string "yreuQ" ==> should be checked as a substring rather than a key. <"yreuQ" in value> then dispatch to corresponding queue
      - Status: Fixed in patch ==> patch_dispatcher.py

    * BUG 2 =>
      - Fix: Dispatch Rule - with integer values ==> should be checked for a private field before dispatching them into integer queue. helper.is_private_field should be called before processing
      - Status: Fixed in patch ==> patch_dispatcher.py

    * BUG 7 =>
      - Fix: transformation - Malformed input should be sanitized and exception should be thrown or the error should be supressed for unaffected function. An exception handler added to supress
      - Status: Fixed in patch ==> patch_transformation_engine.py

    * BUG 8 =>
      - Fix: MessaginService - negative queue values ==> negative ranges of queue numbers should be handled and error should be thrown, extend the range to negative numbers for exception
      - Status: Fixed in patch ==> patch_messaging_service.py

    * BUG 10 =>
      - Fix: Transformation - replicas of the message object should be avoided. A single message object should be maintained and changes should be performed
      - Status: Fixed in patch ==> patch_transformation_engine.py


### FRAMEWORK - Improvement in the design and implementation of the application

* Security as a concern ==>
  * Trust of the message object should be questioned. The input could have been sanitized or filtered properly to avoid a number of JSON bugs. The message should also be sanitized for scripted inputs or possible malicious inputs, which could introduce drastic effects when the application is expaneded with more features

* Error Handling ==>
  * Proper exception handling at critical input handling function should be constructed for graceful exit or error of the program so that not much of the internals are revealed as well as the program doesnt crash

* Sequence/Part logic ==>
  * The sequence or part logic could be implemented better with consideration of a number of edge cases, An easy hack of blocking the initial message or altering the order of the initial message breaks or crashes the program.

* Memory ==>
  * Message objects, creating replicas while processing would cause memory exhaustion when operated on a very larger scale. A single object could be mutated and maintained to reduce memory consumption.

* Thread ==>
  * Even though queue library are thread safe, a proper custom locks/semaphores for read/write access could be implemented in the program which would be race condition proof as a single queue is maintained while operations are performed.

### Conclusion:
Thus, the assessment is performed and the report is provided for the `Query` Queue project. The code quality was nice to catch hold of any corner scenarios with a very few misses. The corresponding files provide further information.
 * ---> NOTES      - notes.pdf
 * ---> AdhocTests - adhocTestSuite/
 * ---> blackBoxTestSuite - blackBoxTestSuite.py
 * ---> Fixes at patch - patch/
