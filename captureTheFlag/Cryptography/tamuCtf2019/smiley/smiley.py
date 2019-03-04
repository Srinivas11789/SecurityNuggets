# Smiley
# - Repeating XOR Key

"""
* was diverted a lot with various hints in this challenge.
  - emoji tweets with the ciphertext
  - tried very much for a long time to discover smiley cipher
    - detour at codeEmoji
    - some detour at using emoji characters for encryption
    - the website that claims for smiley cipher --> enisoc.com/smileycipher was taken down --> 
so looked into the archives in google to find the code possibly --> found that the key was just repeating xor with smileys
    - Also, ended up at different articles of xor encryption being broken with smiley pictures.
  - After a long search knew that the given string was cipher text and smiley was the key. Repeating exor solved it...
* https://ayende.com/blog/177729/emoji-encoding-a-new-style-for-binary-encoding-for-the-web
* https://gist.github.com/ayende/c7977cda3fe64c1399fea80837c9904e
* https://stackoverflow.com/questions/31280295/python-reading-emoji-unicode-characters
* https://cryptii.com/pipes/morse-code-with-emojis
* http://decodemoji.com/
* https://codemoji.org/#/encrypt
* https://www.dcode.fr/
   - Went through all the different ciphers, crypto and symbols (was helpful in getting know different ciphers though)
"""

import base64

cipher_text = "XUBdTFdScw5XCVRGTglJXEpMSFpOQE5AVVxJBRpLT10aYBpIVwlbCVZATl1WTBpaTkBOQFVcSQdH"
cipher_text = base64.b64decode(cipher_text)

key = ":)"*len(cipher_text)

print "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(cipher_text,key)])
