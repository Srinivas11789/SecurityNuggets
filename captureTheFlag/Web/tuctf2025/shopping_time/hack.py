import hashlib
import requests
import random, string

target = "Flag"
hash = hashlib.md5(target.encode()).hexdigest()
print(hash)
target_match = hash[0:6]

resp = requests.get("https://raw.githubusercontent.com/kkrypt0nn/wordlists/refs/heads/main/wordlists/languages/english.txt")
wordlist = resp.text.split("\n")
#print(wordlist[:10])

print("Trying to find collision...")

for w in wordlist:
  if w == target:
    continue
  hash = hashlib.md5(w.encode()).hexdigest()
  if hash[0:6] == target_match:
    print(w)
    break


times = 10000000000
for i in range(times):
  random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
  if w == target:
    continue
  hash = hashlib.md5(w.encode()).hexdigest()
  if hash[0:6] == target_match:
    print(w)
    break
