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

"""
url = "https://hack-code.ctf.insecurity-insa.fr/static/routes.txt"

resp, cookie = get(url, "")
routes = resp.split("\n")

# Create a combination list between each route with every other route (Find all intersections)
intersections = {}
n = len(routes)
for route in range(n):
    routers_intersections = ""
    match = False
    for other in range(route+1, n):
        r = routes[route].split(",")
        o = routes[other].split(",")
        if r != o:
            common = set(r).intersection(set(o))
            if common:
                routers_intersections += "".join(sorted(common))
                match = True
    if match == False:
       routers_intersections += routes[route][0]
    
    

keys = sorted(intersections.keys(), key=lambda x: len(x), reverse=True)
"""

# Too intense pseudo code - optimize 
# Chal 2 and 3 --> Enter all the router hop in each path once to jump through all the network paths.
# -- Follow the logic diagram laid out
url = "https://hack-code.ctf.insecurity-insa.fr/static/routes.txt"

# Get all the routes
resp, cookie = get(url, "")
routes = resp.split("\n")
#routes = ["c,b,a", "d,a,g", "b,c,e", "f,d,g", "z,z,z", "y,g,m"]

import os
if os.path.isfile("backup.txt"):
    import json
    f = open("backup.txt", "r")
    content = json.loads(f.read())
    intersections = content[0]
    hits = content[1]
    matched = content[2]
else:
    # Create a combination list between each route with every other route (Find all intersections)
    intersections = {}
    hits = {}
    matched = []
    n = len(routes)
    for route in range(n):
        for other in range(route+1, n):
            r = routes[route].split(",")
            o = routes[other].split(",")
            if r != o:
                common = set(r).intersection(set(o))
                for c in common:
                    if c not in hits:
                        hits[c] = 0
                    hits[c] += 1
                if common:
                    common = "-".join(sorted(common))
                    if common not in intersections:
                        intersections[common] = [route, other]
                    else:
                        intersections[common].append(other)
                    matched.extend([route, other])
        if route not in matched:
            r = routes[route].split(",")
            if r[0] not in hits:
                hits[r[0]] = 0
            hits[r[0]] += 1
            intersections[r[0]] = [route]
        
    print intersections, hits

    import json
    backup = open("backup.txt", "w")
    backup.write(json.dumps([intersections, hits, matched]))


keys = sorted(intersections.keys(), key=lambda x: len(x), reverse=True)

selected_routers = []
visited = []

h = sorted(hits.keys(), key=lambda x: hits[x], reverse=True)

total = 0
for i in h:
    if i not in selected_routers:
        selected_routers.append(str(h))
        total += hits[i]
    print total

"""
for key in keys:
        previous = len(visited)
        #for r in intersections[key]:
        #    if r not in visited:
        #        visited.append(r)
        visited.extend(intersections[key])
        visited = list(set(visited))
        if previous < len(visited):
            if "-" in key:
                key = key.split("-")
                for k in key:
                    maxi = 0
                    select = None
                    if k in hits and max(hits[k], maxi) == hits[k]:
                        maxi = hits[k]
                        select = k
                if select and select not in selected_routers:
                    selected_routers.append(select)
                else:
                    if k[0] not in selected_routers:
                        selected_routers.append(k[0])
            else:
                if key not in selected_routers:
                    selected_routers.append(key)
"""

print selected_routers

data_url = "https://hack-code.ctf.insecurity-insa.fr/submit"
result = {"taps": ""}
for router in selected_routers:
    result["taps"] += str(router)+"\n"

#print result

resp2, cookie = post(data_url, result, "" )
print "Next flag at: " + str(len(selected_routers)) + " is " + resp2


