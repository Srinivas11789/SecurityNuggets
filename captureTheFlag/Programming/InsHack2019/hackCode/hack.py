# Requests to fetch the router path's list 
import requests
def post(url, payload, cookie):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    headers["Referer"] = url
    req = requests.post(url, headers=headers, cookies=cookie, data=payload)
    cookie = req.cookies
    response = req.text
    return response, cookie

def get(url, cookie):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"}
    headers["Referer"] = url
    req = requests.get(url, headers=headers, cookies=cookie)
    cookie = req.cookies
    response = req.text
    return response, cookie

# Chal1 --> Enter all the router hop in each path once to jump through all the network paths.
# -- Should the repeated and common routers count? Try with a unique list of router paths that are required
url = "https://hack-code.ctf.insecurity-insa.fr/static/routes.txt"

# Get all the routes
resp, cookie = get(url, "")
routes = resp.split("\n")
routes = ["c,b,a", "d,a,g", "b,c,e", "f,d,g"]

# Get all unique routers totally
all_the_routers = []
for route in routes:
    all_the_routers.extend(list(set(route.split(","))))
    #all_the_routers = list(set(all_the_routers))

#print all_the_routers

# Get counts with collections
import collections
rcollect = collections.Counter(all_the_routers)

# Add all network taps
chal1_unique_router_every_path = []
for route in routes:
    r = route.split(",")
    present = 0
    for q in r:
        if q in chal1_unique_router_every_path:
            present = 1
    if present == 0:
   	r = sorted(r, key=lambda x: rcollect[x])
	print r[-1], r, rcollect
	if len(r) >= 2 and r[-1] == r[-2]:
            chal1_unique_router_every_path.append(r[-2])
        else:
	    chal1_unique_router_every_path.append(r[-1])

data_url = "https://hack-code.ctf.insecurity-insa.fr/submit"
result = {"taps": ""}
for router in chal1_unique_router_every_path:
    result["taps"] += router+"\n"
print result
resp2, cookie = post(data_url, result, "" )
print "First flag at: " + str(len(chal1_unique_router_every_path)) + " is " + resp2

