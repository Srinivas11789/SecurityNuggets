# Reverseing 2

### Given:
* An exe file for payroll

### Notes:
* It was an exe file, running the file required a windows box, argh!
* Binary ninja analysis had a number of functions and flows.
  - The code flow shows some username and password being checked
  - Some details on the token, username, password but no proper flow...
* IDA gave some errors
  - Finding was it is a dotnet based, probably a dotnet decompiler should solve this...
* Tried `strings` for the exe but was not able to return any possible password/username 
* I am not very good with reversing, but this binary had a abnormal flow on all the tools
* Checking for decompilers for dotnet binary
  - dnspy, dotPeek looks promising but again they only work for windows...
* Running through a decompiler provides all the functions,
  - check_username
  - check_password
  -- Have the harcoded strings to use for login and get the flag...
