import requests, hashlib, datetime
while 1:
  curr_time = str(datetime.datetime.now())
  curr_hex = hashlib.sha256(str(datetime.datetime.now())).hexdigest()
  print("Hashed time is :", curr_hex)
