# Content
content = open("output.txt", "rb").read()
# Reverse it
content = content[::-1]
# Write back into new file
open("result.txt", "wb").write(content)
