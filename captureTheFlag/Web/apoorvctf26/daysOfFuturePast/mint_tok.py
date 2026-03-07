import jwt
import datetime

#SECRET_KEY = "e53e6e2d3018dce302f876eda97d3852f5f1a81192a5f947ed89da9832ea17b8"
SECRET_KEY = "cryptovault2026"

payload = {
  "role":"admin",
  "iat": datetime.datetime.utcnow(),
  "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print(token)

