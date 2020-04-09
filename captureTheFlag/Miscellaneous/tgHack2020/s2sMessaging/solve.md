### Challenge

```
s2s messaging
Author: Krister Borge - kristebo#9730

Intercepted ship to ship communication. Can you find the message?

s2s.pcapng.
```

### Recon
* Looking at the packet capture in wireshark
* Neglecting TLS exchanges by default
* DNS seems interesting as there is a lot of exchange, seems valid but lets revisit this after we search for some obvious ones
* No plaintext exchanges
* Message Publish/Subscribe is present with MQTT protocol ( aligns with the challenge heading to be messaging protocol )
  - The TCP stream has some encoded data as radio data in the end. Following TCP stream to get all the data
* `==` at the end confirms base64 encoded data

### Solve

```python
Python 2.7.16 (default, Feb 29 2020, 01:55:37) 
[GCC 4.2.1 Compatible Apple LLVM 11.0.3 (clang-1103.0.29.20) (-macos10.15-objc- on darwin
Type "help", "copyright", "credits" or "license" for more information.
i>>> import base64
>>> c = """
... iVBORw0KGgoAAAANSUhEUgAABTkAAAA7CAIAAAA/
...
+CxwVgcAAAAAAAAAAD4LnNUBAAAAAAAAAIBP4n//+z8ELqgvrQH+IAAAAABJRU5ErkJggg=="""
>>> base64.b64decode(c)
'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x059\x00\x00\x00;\x08\x02\x00\x00\x00?
...
\x04.\xa8/\xad\x01\xfe \x00\x00\x00\x00IEND\xaeB`\x82'
>>> d = base64.b64decode(c)                                                                                                        
>>> f = open("flag.png", "w")
>>> f.write(d)
>>> f.close()
```

### Flag
* Image has the flag
