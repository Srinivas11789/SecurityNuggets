# Ref: https://stackoverflow.com/questions/3451111/unzipping-files-in-python
import zipfile
import os
#start = "smelly-onion.rar"
start = "ans/onion.zip"
universal = ["onion"]
old_file_list = set(os.listdir("ans"))
with zipfile.ZipFile(start,"r") as zip_ref:
    universal.extend(zip_ref.namelist())
    zip_ref.extractall("ans")
new_file_list = set(os.listdir("ans"))
extracted = new_file_list - old_file_list
"""
while extracted:
   #print(extracted)
   new = set()
   for f in extracted:
      old_file_list = set(os.listdir("ans"))
      with zipfile.ZipFile("ans/"+f,"r") as zip_ref:
        for o in old_file_list:
          os.remove("ans/"+o)
        zip_ref.extractall("ans")
   new_file_list = set(os.listdir("ans"))
   new = new.union(new_file_list - old_file_list)
   #print(new)
   extracted = new
"""
comments = []
while extracted:
   new = set()
   for f in extracted:
      with zipfile.ZipFile("ans/"+f,"r") as zip_ref:
        #print(zip_ref.infolist(), zip_ref.namelist())
        for p in zip_ref.infolist():
            print(p.filename, p.file_size, p.comment)
        comments.append(zip_ref.comment)
        universal.extend(zip_ref.namelist())
        new = new.union(set(zip_ref.namelist()))
        zip_ref.extractall("ans")
   new_file_list = set(os.listdir("ans"))
   remove = new_file_list - new
   if not new:
     break
   #print(new_file_list, new, remove)
   for o in remove:
       os.remove("ans/"+o)
   extracted = new
print(universal)
for o in universal:
    print(o),
c = ['onion']
for name in universal[1:]:
    c.append(chr(int(name)))
print("".join(c))

for n in comments:
  print(n.decode("hex")),
print("Done")
