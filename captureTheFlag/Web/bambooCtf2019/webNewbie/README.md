### Web Newbie

* Challenge
```
http://34.82.101.212:8005/ http://bamboofox.cs.nctu.edu.tw:8005/ (Backup Server)

Hey, I just learned how to make a web application!

Even though I might create some vulnerabilities, but I bet you'll never get the flag!

The submitted files will be deleted every hour.
```

* Recon and Solve
  - Takes to a page where you can create code/text snippted with a filename
    - filename has character checking for char/nums
    - body does not seem to execute and just print the file contents, try a minimal injection attempts ( did not dwell more on this )
  - Looking at different requests/responses
  - Once the file is created a HTTP redirection to the GET request for `op=view&file=<filename>` happens.
    - Trying for path traversal instantly on this is a success
      - /etc/passwd and /etc/shadow are successfully retrieved
    - We do not know the location of the flag though. Trying different known LINUX/UNIX paths for the flag is in vain....
  - Bruteforce/Guessed some different OP types like read, write ..... there should be something that leads to this..
  - Coming back to read the challenge and review all the pages and contents
    - PAGE SOURCE shows there is another OP. `NAV`
      - op=nav&link=about
      - op=nav&link=error
      - And one commented section -----> `op=nav&link=hint`
  - HINT shows the flag is at `../flag.txt`
  - Accessing `?op=nav&link=../flag.txt` or `?op=view&file=a/../../flag.txt` --> GETS the flag but the contents are not displayed. There is a server side check which strips the content or flag is it finds the flag format in the content
    - Maybe assuming there is a server side logic to regex BAMBOOFOX{} and if it exists in content it gets replaced by `CONTENT CONTAINS FLAG` and is returned.
  - There was a simple work around that I missed....
    - I got focused on defeating this filter
      for the filename,
      - tried different attempts of navigation from different folder structures for both the OPS view and nav
      - tried encoded, double encoded payloads --> tried different separators like // or ., which would concatenate later. Nothing helped!
      for the content,
      - To alter the content from the server so the filter doesnt work, tried different headers
      - `Content-Language or Accept-Language` to change the content to a different language so the filter does not work and I could retranslate the flag
        - tried all the ISO code for languages but still no success
      - `Accept**` headers --> Tried different accept headers
        - Language
        - Encoding
        - Charset
      - Transfer Encoding, Trailer, ETag stuff changes to alter the response from the server so the check fails.....
    - Finally after this full attempts, I rethought, came back to the beginning ( sometimes this is where you will find the answer and rediscover )
      - Knowing the path and accessing `GET /../flag.txt` just returns the flag
      - when I was trying to use GET params the PHP Code executed and Filter worked. Just do not use it and directly access. Thats way to go!

      