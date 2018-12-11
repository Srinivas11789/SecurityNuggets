def reaction(string):
    lstr = list(string)
    i = 0
    while i < len(lstr):
        if i < len(lstr)-1:
           if lstr[i].islower():
              if lstr[i].upper() == lstr[i+1]:
                 del lstr[i]
                 del lstr[i]
                 i -= 1
              else:
                 i += 1
           elif lstr[i].isupper():
              if lstr[i].lower() == lstr[i+1]:
                 del lstr[i]
                 del lstr[i]
                 i -= 1
              else:
                 i += 1
           else:
              i += 1
        else:
           i += 1  
    return len("".join(lstr))
                
           
        
def main():
    input = open("51.input","r").read()
    input = input.split("\n")
    for inp in input:
     if inp:
        print reaction(inp)

main()

