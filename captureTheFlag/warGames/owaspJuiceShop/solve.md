# OWASP Juice Shop --> is a bug free website with some known vulnerabilities

### Login
* Login form for username and password is vulnerable to sql injection. Tested with `'`
  - Error shows username being replaced with the input and password hashed before replacing
  - admin' or '1' == '1' -- ( logs in as admin )

* Accessing the admin page --> track order --> looking at status/receipts --> Possible to `Path Traversal` for `/ftp` directory --> EasterEgg is inside there `eastere.gg` --> but the download only allow .md or .pdf files as a part of server side validation --> Null byte path traversal attack --> eastere.gg%00.pdf does not bypass and throws bad request error --> URL encoded null byte works --> eastere.gg%2500.pdf bypasses the filter and allows easter egg download --> That is not a real easter egg --> It has a long path --> Try different encoding or exor or known cracked cipher attacks --> Look at plaintext attack --> repeatable elements or characters --> ROT13 --> replace with path for easter egg (dont use ftp)
  - While the above is success path, all other approach of failures is also valuable
    - Tried `UTF16 UTF8 Double Encoded paylaods` for path traversal 
    - Tried to request to a malicious url as file open also open http requests sometimes
    - Tried to change the gravatar of admin with localhost/ftp/eastere.gg to bypass filter and then download the image file to look if the contents are migrated