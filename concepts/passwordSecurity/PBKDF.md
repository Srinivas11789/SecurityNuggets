# Password Based Key Derivation Function < 2 >

### What is It?
* Its a key derivation function, which uses
  - password as a secret
  - HMAC function
  - Length of the resulting key
  - Number of iterations to hash 

### NIST Recommendation
* Based on the latest recommendation which is of 2010, NIST recommends using PBKDF

### Known Facts 

* Hash Collision in HMAC < not a security vulnerability >
  - Scenario: When password is very long...
    * 

* what is this number of iterations?
  - My perception is: Hashing every time a password is input is already computation intensive, if the hashing is done in iterations (1000s or 100000s), the performance of the server should degrade considerably. How is this done and what does it achieve?
  - How? hashing iterated in chuncks to build the master key
  - Achievement? Prevents the password to be brute forced or hash cracked or usage of rainbow tables

### Weakness
* Vulnerable to brute force attack possibility - PBKDF fairly requires smaller chip and lesser RAM for computation hence using a performance processor will lead to easy brute force of the passwords. 

### References:
* https://en.wikipedia.org/wiki/PBKDF2
* https://security.stackexchange.com/questions/98214/why-should-i-choose-sha-such-as-sha-512-instead-of-bcrypt-or-pbkdf2-for-fips

