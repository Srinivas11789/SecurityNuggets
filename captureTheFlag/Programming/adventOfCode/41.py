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
   
def create_table(data):
    print "Date   ID   Minute"
    print "            "+"0"*10+"1"*10+"2"*10+"3"*10+"4"*10+"5"*10
    print "            "+"0123456789"*6
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
                print date+"  "+id+"  "+ ranger

def main():
    data = {}
    input = open("41.example","r").read()
    input = input.split("\n")
    create_table(parse_data(input, data))

main()
