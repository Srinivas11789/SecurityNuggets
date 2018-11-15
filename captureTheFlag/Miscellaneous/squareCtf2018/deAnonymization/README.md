### Square Ctf 2018 --> GDPR category: deAnonymization

### Concept
* In GDPR, anonymization is when the privacy of the user is protected by anonymizing the data such that nothing is derived about any person.

### Given
* Five csv data sets containing different parameters like Firstname, email, 4 digits of SSN, Role, Pay, State, Street Address.
* A web portal which has a login and reset password page
* Says you have to find details about the user `Yakubovics` who is the captain to login the system

### Think, Think, Think
* Looking at the portal it is very intriguing to perform a sql injection or admin login BUT we have the datasets and a hint name.
* It is obvious, from the details of the dataset and the reset password form that we should find the data from the datasets and fill in reset password to reset it and then login

### Steps
* Start from the name we have `Yakubovics` and boil down to get the firstname, ssn, street address, state
* From all possible sets obtained from the above filter, use these in reset password form
* Get or change the password 
* Login

### Details:
* Start with the given name we have `Yakubovics`
* Check the dataset1 --> We obtain email with the last name
* Check the dataset2 --> Use the email and last name obtained from dataset1 to obtain the STATE
* Check the dataset3 --> With the State, obtain the ssn and street address
* Check the dataset4 --> Get income and postal code with the state obtained
* Check the dataset5 --> From the email we know the first character of name is `e`, use this to filter first name in the fifth dataset 
* As we progress delete the non matched sets

### Program
* reader.py
  - This program throws the final set of data from all the filter through the dataset csv 1 -5. From this set using `Elyssa` gives the answer

```python
import json
names = []
yaku = {}

# File 1: Fetch all the existence of the names of the Captain
for i in range(1,2):
    name = str(i)+".csv"
    file = open(name,"r")
    for line in file.readlines():
        if "Yakubovics" in line.strip() or "Yakubovics".upper() in line.strip() or "Yakubovics".lower() in line.strip():
           l = line.strip().split(",")
           yaku["email"] = l[0]
           yaku["role"] = l[1]
           yaku["income"] = l[2]
    file.close()


# File 2
for i in range(2,3):
    name = str(i)+".csv"
    file = open(name,"r")
    for line in file.readlines():
        if "Yakubovics" in line.strip() or "Yakubovics".upper() in line.strip() or "Yakubovics".lower() in line.strip():
           l = line.strip().split(",")
           yaku["state"] = l[1]
    file.close()

# doc has the ssn, address --> Fetch all florida addresses and ssn
name = str(3)+".csv"
file = open(name,"r")
for line in file.readlines():
    if "Florida" in line.strip() or "Florida".lower() in line.strip() or "Florida".upper() in line.strip():
       l = line.strip().split(",")
       # ssn
       yaku[l[2]] = {}
       # street
       yaku[l[2]]["ssn"] = l[0]
file.close()

# Fourth
name = str(4)+".csv"
file = open(name,"r")
for line in file.readlines():
    l = line.strip().split(",")
    if " ".join(l[2:-1]) in yaku and ("Florida" in l[1] or "Florida".upper() in l[1] or "Florida".lower() in l[1]):
       yaku[" ".join(l[2:-1])]["income"] = l[0]
       yaku[" ".join(l[2:-1])]["postal"] = l[-1]
file.close()

# Fifth
name = str(5)+".csv"
file = open(name,"r")
for line in file.readlines():
    l = line.strip().split(",")
    if " ".join(l[1:]) in yaku:
       yaku[" ".join(l[1:])]["name"] = l[0]
       # This assumption doesnt work?
       if l[0][0] != "e".upper() and l[0][0] != "e".lower():
          del yaku[" ".join(l[1:])]
file.close()

print json.dumps(yaku, sort_keys=True, indent=4)

```

### Output Flag - Hidden password can be obtained by looking at the source for the masked/hidden field

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Miscellaneous/squareCtf2018/deAnonymization/flag_output.png" title="Flag">

### Program output - Based on the relation boil the data down to possible sets

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Miscellaneous/squareCtf2018/deAnonymization/program_output.png" title="Program">

### Result

* Using details of Elyssa throws the answer

`    
    "4 Magdeline": {
        "income": "96605", 
        "name": "Elyssa", 
        "postal": "33421", 
        "ssn": "4484"
    }, 
`
