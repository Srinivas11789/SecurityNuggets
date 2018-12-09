# Guard falling asleep
# Example:
# * [1518-11-01 00:00] Guard #10 begins shift
# * [1518-11-01 00:05] falls asleep
# * [1518-11-01 00:25] wakes up
# Format:
# * [year-month-day hour:minute] < begins shift/ falls asleep/ wakes up > 
# 
# Logic:
# * Parse each line and group into a dictionary
# * Data --> ID --> sleep times, wake times
# * Create table and populate data

import sys
from datetime import datetime

def parse_data(input, data):
    for i in input:
     try: 
      if i:
        # Parse data

        # Date
        i = i.split("]")
        time = datetime.strptime(i[0].strip("["), '%Y-%m-%d %H:%M')
        if time.day < 10:
           day = "0"+str(time.day)
        else:
           day = str(time.day)
        date = str(time.month)+"-"+day
        
        # Guard id and activity
        remaining = i[1].split(" ")
        if "#" in remaining[2]:
           guard = remaining[2]
           activity = remaining[3]
        else: 
           activity = remaining[2]
        
        # Fill dictionary
        if date not in data:
           data[date] = {}
        if guard not in data[date]:
           data[date][guard] = {}

        # Minute
        if time.minute < 10:
           minute = "0"+str(time.minute)
        else:
           minute = str(time.minute)  

        # Activity
        #print data, minute, activity
        if activity == "asleep":
               if minute not in data[date][guard]:
                    data[date][guard][minute] = ""
               data[date][guard][minute] = "last"
        if activity == "up":
               for min in data[date][guard].keys():
                   if data[date][guard][min] == "last":
                      data[date][guard][min] = minute
                      #break
     except:
        print i  
    print data
    return data

def andOp(s1, s0=[0]*60):
    test = s0[:]
    #maxi = -1
    for i in range(len(s1)):
        if s1[i] == "#":
           test[i] += 1
        #maxi = max(maxi, test[i])
    return test
        
def create_table(data):
    max_sleep = 0
    pattern = {}
    max_person = ""
    print "Date   ID     Minute"
    print "              "+"0"*10+"1"*10+"2"*10+"3"*10+"4"*10+"5"*10
    print "              "+"0123456789"*6
    dates = sorted(data.keys())
    for date in dates:
        last = 0
        ranger = ""
        #print date, ide
        for id in data[date].keys():
            if data[date][id] != {}:
                acts = sorted(data[date][id].keys())

                for act in acts:
                    ranger += "." * (int(act)-last)
                    #last = int(act)
                    ranger += "#" * (int(data[date][id][act]) - int(act))
                    last = int(data[date][id][act])

                ranger += "." * int(60-int(data[date][id][act]))

                if "max_sleep" not in data[date][id]:
                    data[date][id]["max_sleep"] = 0

                data[date][id]["max_sleep"] += ranger.count("#")

                if id not in pattern:
                   pattern[id] = {}

                #if "intersection" not in pattern[id]:
                #    pattern[id]["intersection"] = []

                if "pattern" not in pattern[id]:
                    pattern[id]["pattern"] = andOp(ranger)
                    if id == "#1523":
                       print pattern[id]["pattern"]
                else:
                    pattern[id]["pattern"] = andOp(ranger, pattern[id]["pattern"]) #pattern[id]["pattern"] and ranger
                    if id == "#1523":
                       print pattern[id]["pattern"]
                    #for u in range(len(pattern[id]["pattern"])):
                    #    if ranger[u] == pattern[id]["pattern"][u]:
                    #       pattern[id]["intersection"] = u
                
                if "intersection" not in pattern[id]:
                    pattern[id]["intersection"] = 0
                pattern[id]["intersection"] = pattern[id]["pattern"].index(max(pattern[id]["pattern"])) # pattern[id]["pattern"].index("#")
                
                if "s" not in pattern[id]:
                    pattern[id]["s"] = []
                pattern[id]["s"].append(ranger)
                
                if "max_sleep" not in pattern[id]:
                    pattern[id]["max_sleep"] = 0
                pattern[id]["max_sleep"] += ranger.count("#")
                #pattern[id]["max_sleep"]
                
                if pattern[id]["max_sleep"] > max_sleep:
                   max_sleep = pattern[id]["max_sleep"]
                   max_person = id
                print date+"  "+id+"  "+ ranger

    print pattern[max_person]
    for com in pattern[max_person]["s"]:
        print com
    return max_sleep, max_person, pattern[max_person]["intersection"]

def main():
    data = {}
    input = open("41.input","r").read()
    input = input.split("\n")
    input = sorted(input)
    #print input
    max_sleep, max_person, most_times = create_table(parse_data(input, data))
    print max_sleep, max_person, most_times
    print "Answer is "+ str(int(max_person.strip("#"))*most_times)

main()
