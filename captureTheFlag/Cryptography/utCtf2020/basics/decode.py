content = open("binary.txt", "r").read()
content = content.split(" ")

# Level 1 ==> Binary
decoded = ""
for c in content:
  if c != "":
    #print(c)
    c = int(c, 2)
    decoded += chr(c)
print("Output of level 1 is: ")
print(decoded)

# Level 2 ==> Base64
import base64
content = decoded.split(")")[-1]
decoded = base64.b64decode(content)
print("Output of level 2 is: ")
print(decoded)    

# Level 3 ==> Caesar Cipher
# Found from dcode.fr that the shift is +10
# https://www.dcode.fr/caesar-cipher
content = """
alright, you're almost there! Now for the final (and maybe the hardest...) part: a substitution cipher. In the following text, I've taken my message and replaced every alphabetic character with a correspondence to a different character - known as a substitution cipher. Can you find the final flag? hint: We know that the flag is going to be of the format utflag{...} - which means that if you see that pattern, you know what the correspondences for u, t, f, l a, and g are. You can probably work out the remaining characters by replacing them and inferring common words in the English language. Another great method is to use frequency analysis: we know that 'e' shows up most often in the alphabet, so that's probably the most common character in the text, followed by 't', and so on. Once you know a few characters, you can infer the rest of the words based on common words that show up in the English language.
hwxdnitvoitjwxk! gwv yiqa sjxjkyau tya padjxxan hngbtwdnibyg hyiooaxda. yana jk i soid swn ioo gwvn yinu asswntk: vtsoid{x0l_ty4tk_ly4t_j_h4oo_hngbt0}. gwv ljoo sjxu tyit i owt ws hngbtwdnibyg jk fvkt pvjoujxd wss tyjk kwnt ws pikjh rxwloauda, ixu jt naioog jk xwt kw piu istan ioo. ywba gwv axfwgau tya hyiooaxda
"""

# Level 4 ==> Substitution Cipher
content = "hwxdnitvoitjwxk! gwv yiqa sjxjkyau tya padjxxan hngbtwdnibyg hyiooaxda. yana jk i soid swn ioo gwvn yinu asswntk: vtsoid{x0l_ty4tk_ly4t_j_h4oo_hngbt0}. gwv ljoo sjxu tyit i owt ws hngbtwdnibyg jk fvkt pvjoujxd wss tyjk kwnt ws pikjh rxwloauda, ixu jt naioog jk xwt kw piu istan ioo. ywba gwv axfwgau tya hyiooaxda"
subs = {
  'v': 'u',
  't': 't',
  's': 'f',
  'o': 'l',
  'i': 'a',
  'd': 'g'
}
new_content = ""
for c in content:
    if c in subs:
      new_content += subs[c]
    else:
      new_content += c
print(content)
print("\n")
print(new_content)
# Running out of time -- Pending to write algos for the above
# Until the resorting to https://www.dcode.fr/monoalphabetic-substitution
"""
CONGRATULATIONS! YOU HAVE FINISHED THE BEGINNER CRYPTOGRAPHY CHALLENGE. HERE IS A FLAG FOR ALL YOUR HARD EFFORTS: UTFLAG{N0W_TH4TS_WH4T_I_C4LL_CRYPT0}. YOU WILL FIND THAT A LOT OF CRYPTOGRAPHY IS JUST BUILDING OFF THIS SORT OF BASIC KNOWLEDGE, AND IT REALLY IS NOT SO BAD AFTER ALL. HOPE YOU ENJOYED THE CHALLENGE
"""
      
