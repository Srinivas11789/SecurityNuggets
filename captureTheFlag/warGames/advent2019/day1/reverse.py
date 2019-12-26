# Implement N7110 reverse from the csv < key_logs > ---> text < message >

# 1. Key mapping --> keys.h --> convert the c data structure to python --> Refer keys.h
# key map + key characters of the button on a keypad 

# 2. Keys in Python

key_map = {
"0": " 0",
"1": ".,'?!\"1-()@/:",
"2": "abc2",
"3": "def3",
"4": "ghi4",
"5": "jkl5",
"6": "mno6",
"7": "pqrs7",
"8": "tuv8",
"9": "wxyz9",
"10": "@/:_;+&%*[]{}",
"11": "#",
"100": "<-",
"101": "->",
"102": "^|",
"103": "~|",
"104": "OK",
"105": "REJECT"
}

def get_all_possible_combinations(current, value, press_times, prefix):
    #print(current, prefix)
    if press_times == 0 and current != "":
        #if "o" not in current and "a" not in current and "e" not in current and "i" not in current:
        if len(current) <= 4:
            prefix.append(current)
    else:
        for i in range(1, press_times+1):
            if press_times-i >= 0 and i-1 < len(value):
                #print(i-1, value)
                get_all_possible_combinations( current + value[i-1] , value, press_times-i, prefix)
            else:
                break
    return prefix

message_maps = {"flag"}#, "1", "2", "3", "4"}

# 3. Read the CSV file < key_logs > and obtain the key logs or code
# 4. Reverse the values by iterating the key_logs and converting them to keys
# 5. Output the messages SMSes

for sms in message_maps:
    print("="*50+"Message for SMS"+sms+":")
    plaintext = ""
    possible_flags = [""]
    if sms == "flag":
        f = open(sms+".csv", "r")
    else:
        f = open("sms"+sms+".csv", "r")
    content = f.readlines()
    prev_press = None
    press_times = 0
    l = 0
    while l < len(content):
        line = content[l].strip()
        id, key = line.split(",")
        if prev_press == None:
            prev_press = key
            press_times += 1
            l += 1
        elif prev_press == key:
            press_times += 1
            l += 1
        else:
            if int(prev_press) <= 100:
                #print(prev_press, press_times, l)
                all_possible = get_all_possible_combinations("", key_map[prev_press], press_times, [])
                """
                if len(key_map[prev_press])-1 >= press_times-1:
                    plaintext += key_map[prev_press][press_times-1]
                else:
                    #Logic: Divisibility check and predict
                    for i in range(press_times-1, 1, -1):
                        #print(prev_press, press_times, i)
                        if press_times%i == 0 and i < len(key_map[prev_press]):
                            plaintext += (key_map[prev_press][i-1])*(i)
                            break
                """
                    
                # Logic: Try all combinations and maintain different threads as we proceed
                """
                new_all_possible = []
                for f in range(len(possible_flags)):
                    for p in all_possible:
                        new_all_possible.append(possible_flags[f]+p)
                possible_flags = new_all_possible[:]
                """

            
                print(plaintext, key_map[prev_press], press_times,)
                if len(all_possible) == 1:
                    plaintext += all_possible[-1]
                else:
                    for p in range(len(all_possible)):
                        print(p, all_possible[p])
                    choice = int(input("Enter your choice: "))
                    if choice > len(all_possible):
                        print("Cannot continue....")
                    plaintext += all_possible[choice]
                


            prev_press = None
            press_times = 0
            #print(possible_flags)
    print(plaintext)
    for message in possible_flags:
        print(message)


    """
    plaintext = [""]
    f = open("sms"+sms+".csv", "r")
    content = f.readlines()
    prev_press = None
    press_times = 0
    l = 0
    while l < len(content):
        line = content[l].strip()
        id, key = line.split(",")
        if prev_press == None:
            prev_press = key
            press_times += 1
            l += 1
        elif prev_press == key:
            press_times += 1
            l += 1
        else:
            # Logic: Try all combinations and maintain different threads as we proceed
            def get_all_possible_combinations(current, value, press_times, prefix):
                if press_times == 0 and current != "":
                    prefix.append(current)
                else:
                    for i in range(1, press_times+1):
                        if press_times-i >= 0:
                            get_all_possible_combinations( current + value[i-1] , value, press_times-i, prefix)
                        else:
                            break
                return prefix

            if int(prev_press) <= 10 and len(key_map[prev_press]) <= press_times:
                print(prev_press, press_times)
                substrs = get_all_possible_combinations("", key_map[prev_press], press_times, [])
                #print(substrs)
                current_possible = []
                for text in plaintext:
                    for j in range(len(substrs)):
                        current_possible.append(text+substrs[j])
                    text += substrs[0]
                plaintext.extend(current_possible)
                #print(plaintext)
                #break
                
            prev_press = None
            press_times = 0
            #print(plaintext)
            
    print(plaintext)
    """
# aotw{l3ts_dr1nks0m3_eggnnnm0g_y0u_cr4zy_d33r}
#aotw{l3ts_dr1nks0m3_eggno60g_y0u_cr4zy_fedder}
#aotw{l3ts_dr1nks0m3_eggnnnog0g_y0u_cr4zy_fedder}
# aotw{l3ts_dr1nk_s0m3_eggnnnog0g_y0u_cr4zy_fedder}

# aotw{l3ts_dr1nk_*_s0m3_eggnnnog0g_y0u_cr4zy_fedder}

# aotw{l3ts_dr1nk_*_s0m3_eggnnnnmg0g_y0u_cr4zy_d33r}
# aotw{l3ts_dr1nk_s0m3_eggn0g_y0u_cr4zy_fffr}

# Finally! Yay! this worked ==>  l3ts_dr1nk_s0m3_eggn0g_y0u_cr4zy_d33r