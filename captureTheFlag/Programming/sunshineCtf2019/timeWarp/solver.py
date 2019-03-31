import sys
import time
try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def fast_send(connection, data):
    # I guess we should do something with this data and send it back!
    # return processed_data
    #c1 = remote(address, port)
    connection.recvuntil("Repeat")
    #connection.sendline(" ".)join(data)
    #for d in data:
        #try:
    #    connection.sendline(d)
    #    print connection.recvline()
        #except:
        #    c1.interactive()
    #c1.interactive()
    #c1.close()

def talk(address, port, key):
    numbers = []

    #numbers = ['39', '61', '267', '475', '178', '760', '660', '257', '897', '994', '610', '639', '813', '495', '832', '647', '228', '74', '474', '215', '523', '905', '65', '741', '814', '742', '787', '58', '917', '548', '465', '309', '609', '733', '784', '140', '493', '444', '397', '391', '790', '359', '382', '956', '854', '566', '603', '435', '640', '429', '650', '163', '335', '716', '256', '149', '458', '396', '559', '375', '944', '24', '684', '905', '757', '820', '397', '251', '264', '794', '994', '407', '506', '728', '363', '360', '294', '318', '795', '286', '747', '446', '801', '434', '514', '410', '935', '972', '806', '494', '699', '102', '519', '736', '359', '276', '908', '757', '879', '525', '903', '225', '932', '409', '953', '647', '122', '599', '965', '917', '237', '712', '363', '39', '147', '877', '801', '82', '201', '607', '929', '253', '61', '448', '341', '772', '724', '249', '529', '604', '774', '785', '181', '58', '546', '135', '705', '668', '86', '670', '586', '324', '735', '301', '715', '234', '531', '516', '316', '732', '123', '245', '337', '536', '45', '678', '308', '770', '280', '190', '726', '406', '975', '907', '465', '521', '394', '170', '190', '481', '841', '128', '805', '576', '429', '520', '162', '960', '36', '478', '45', '511', '76', '382', '399', '473', '413', '707', '243', '693', '897', '321', '99', '224', '581', '916', '98', '975', '87', '288', '456', '280', '416', '613', '208', '197', '485', '370', '158', '873', '200', '203', '384', '628', '937', '135', '102', '350', '843', '697', '395', '92', '19', '847', '669', '600', '763', '767', '927', '202', '55', '736', '482', '823', '701', '690', '20', '187', '60', '530', '60', '613', '85', '797', '241', '23', '932', '343', '725', '127', '41', '121', '220', '412', '320', '241', '364', '83', '8', '291', '286', '63', '379', '120']
    response = ""
    #fast_send(address, port, numbers)
    #sys.exit()
    
    while "sun" not in response:
        #print "Starting with " + str(numbers)
        #print "Start with new" + str(numbers[-1])
        #time.sleep(5)
        connection = remote(address, port)
        #i = 0
        i = len(numbers)
        #fast_send(connection, numbers)
        error = False
        while 1:

            # Receive Logic
            try:
               response = connection.recvuntil("\n")
               #response = connection.recv(4096)
               #print response
               #print "----"
               response = response.split("\n")
               if "sun" in response[0]:
                   print response
                   sys.exit()
               #numbers.append(response[-1])
            except:
               print "End Connection...."
               if "sun" in response:
                   print response
                   sys.exit()
               print response
               #fast_send(address, port, numbers)
               #connection.interactive()
               #print connection.recvall()
               connection.close() 
               print i
               break
            
            print response
            #if response[0].isdigit() and response[0] not in numbers:
            #       numbers.append(response[0])

            if "Repeat" in response[0] or "going to give you some numbers" not in response[0] or response[0].isdigit():

                if response[0].isdigit():# and response[0] not in numbers:
                   #if not numbers or (numbers and response[0] != numbers[-1]):
                        #print response[0] + "Yikes"
                    if error:
                        numbers.append(response[0])
                else:
                    try:
                        # Send Logic
                        if i < len(numbers):
                            print "Sending "+ numbers[i]
                            connection.sendline(numbers[i])
                            i += 1
                        else:
                            print "Sending 10000"
                            error = True
                            connection.sendline("10000")
                    except: 
                        print "sendloop!"

def talk2(address, port, key):
    numbers = []
    response = ""
    while "sun" not in response:
        try:
            print "Starting with " + str(numbers)
            connection = remote(address, port)
            print connection.recvline_regex("Repeat.*")
            print "Sending data " + str(" ".join(numbers))
            if numbers:
                connection.sendline(" ".join(numbers))
                response = connection.recvlines(len(numbers)*2)
                print response
            print "Sending " + "10000"
            connection.sendline("10000")
            response = connection.recvuntil("\n")
            numbers.append(response.strip())
            #print connection.recvuntil("\n")
            connection.close()
        except:
            connection.interactive()


def main():
    try:
        address = sys.argv[1]
        port = sys.argv[2]
        output_key_to_read_until = sys.argv[3]
    except:
        print "Usage: ./client.py [IP] [Port] [Key]"
        sys.exit(1)
    talk2(address, port, output_key_to_read_until)

if __name__ == "__main__":
    main()

