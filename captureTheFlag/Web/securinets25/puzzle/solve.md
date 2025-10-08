## Account Creation
* admin1234
* admin1234@admin.com
* O4w6E#GJDNnw

* admin22@admin.com
* ee&m1XCdCr1u

* ad123
* editor: 1
* UCqvK&o3uOVy

* {{7*7}}
* 9N7qa^1O6hjG


## Leads
* password is not hashed
* password generation involves set character at len 12 to bruteforce (randomly created, some predictability)
* role during registration, can be made EDITOR
* flask + templat --> SSTI
* colaborator check >> username check
* admin seems to be a privileged user, maybe contain post with flag.
* cookie with UUID
* notes rederred via UUID
* send_from_directory re traversal?
* cookie based forging (uuid, first_login_password)
* sqli at get_user_by_username, register?
* is_localhost bypass --> x-fwd, x-real
* disclose admin uuid and leverage it
* /db download for old users >> search admin and crack creds 
  - old.db
  - summarized via llm
*  /collab/request has SQLI but backed by is_local_host


## Path 1

```
    @app.route('/db/', defaults={'req_path': ''})
    @app.route('/db/<path:req_path>')
```

* download old.db
* find admin (there is only one)
* do not follow the default password policy --> that will complicate cracking
* there init_db() functions sets "sompass" which can be predictable so using rockyou

```
┌──(kali㉿kali)-[~/Desktop/securinets]
└─$ hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt               
hashcat (v6.2.6) starting

OpenCL API (OpenCL 3.0 PoCL 3.1+debian  Linux, None+Asserts, RELOC, SPIR, LLVM 15.0.6, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
==================================================================================================================================================
* Device #1: pthread-haswell-Intel(R) Core(TM) i9-9880H CPU @ 2.30GHz, 1425/2914 MB (512 MB allocatable), 4MCU

Minimum password length supported by kernel: 0
Maximum password length supported by kernel: 72

Hashes: 1 digests; 1 unique digests, 1 unique salts
Bitmaps: 16 bits, 65536 entries, 0x0000ffff mask, 262144 bytes, 5/13 rotates
Rules: 1

[s]tatus [p]ause [b]ypass [c]heckpoint [f]inish [q]uit => s

Session..........: hashcat
Status...........: Running
Hash.Mode........: 3200 (bcrypt $2*$, Blowfish (Unix))
Hash.Target......: $2a$06$VhuKtbW6RM9BFml.u37gIeL1Dfg2NordyqvFNsfJ7YrX...icPSa2
Time.Started.....: Sat Oct  4 19:00:35 2025 (35 secs)
Time.Estimated...: Sat Oct  4 23:05:48 2025 (4 hours, 4 mins)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (/usr/share/wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:      975 H/s (3.77ms) @ Accel:4 Loops:16 Thr:1 Vec:1
Recovered........: 0/1 (0.00%) Digests (total), 0/1 (0.00%) Digests (new)
Progress.........: 33808/14344385 (0.24%)
Rejected.........: 0/33808 (0.00%)
Restore.Point....: 33808/14344385 (0.24%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:48-64
Candidate.Engine.: Device Generator
Candidates.#1....: pinkky -> pachuchay
Hardware.Mon.#1..: Util: 89%

$2a$06$VhuKtbW6RM9BFml.u37gIeL1Dfg2NordyqvFNsfJ7YrXQKoicPSa2:pizzaguy
                                                          
Session..........: hashcat
```

* does not work as this is old.db

## PAth 2 --> jwt cracking

```
┌──(enb)─(kali㉿kali)-[~/Desktop/securinets]
└─$ python3 -m flask_unsign --unsign --cookie 'eyJ1dWlkIjoiMGU5MWExZTEtMWVmNi00MjhmLWEzMjUtNDgyOWQ2MzIwNDgxIn0.aOGYWA.08mdHipaq-Q1A1GxkVv6R9L-oAs' -w /usr/share/wordlists/rockyou.txt  --no-literal-eval 
[*] Session decodes to: {'uuid': '0e91a1e1-1ef6-428f-a325-4829d6320481'}
[*] Starting brute-forcer with 8 threads..
[!] Failed to find secret key after 14344392 attempts.nd
```

* SSTI
  - _, % are not allowed. Merely using \ actually causes 500  
  - \x5f hex encode results in 500
  - {{ 7*7 }} and {{ g }} work
  - self, config, {{ \x41 }} donot work
  - this was a deadend.... variants of this including g.*, context based params (config/settings) did not work


## Path 3
  * IDOR to accept collaboration
  * Leak ADmin UUID (based on inviting admin to collab and accepting)
  * users/<admin-uuid> leaks admin password and username

  * SSTI -- deadend with ban_user path

  * /data path next...

  * connect to data to download additional files

  ```
  
    @app.route('/data/', defaults={'req_path': ''})
    @app.route('/data/<path:req_path>')
    @admin_required
  ```

  * Strings with db_connect.ext


  ```
   1 server = '127.0.0.1'
   2 database = 'puzzledb'
   3 username = 'sa'
   4 password = 'PUZZLE+7011_X207+!*'
  ``` 

  * Flag

  ```
 unzipped secrets.zip with password PUZZLE+7011_X207+!*, extracting data.txt. Read data.txt for the flag or a clue.
✦ Flag found: Securinets{777_P13c3_1T_Up_T0G3Th3R}.
```