encoded = "IZZMYN"
encoded = "JCWIGP"
encoded = "HASRQHQWLDO"
for i in range(1, 27):
  shift = i
  decoded = ""
  for c in encoded:
    target = ord(c)+shift
    while target > ord("Z"):
        target -= ord("Z")
        target = ord("A")+target-1
    decoded += chr(target)
  print(decoded)


