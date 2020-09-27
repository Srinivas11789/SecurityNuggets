### Challenge
* SSDEEP value of a executable ( potential malware )

### Recon 
* The SSDEEP tools is used to simulate CTPH or fuzzy segment hashes
* Hash sum gets altered for a bit change in a executable, this would allow malwares to sneak through hashsum checks for malwares. Therefore retaining the same functionality.
* This technique is used to verify matches of functionality or hashes across multiple binaries for similar functionality or code blocks.
* Ref https://medium.com/@nikhilh20/fuzzy-hashing-ssdeep-3cade6931b72

### Solve
* 
```
ssdeep -s deep

ssdeep,1.1--blocksize:hash:hash,filename
1536:KCnGt1AnxGhRoE0JLEaolArglgidmpHACgaSz42tpAonFcP+i+9l:jG1hRoE0JLE8Qjg6aSk0LE+9l,"/home/kali/Downloads/ekoparty/trivia/deep"
```
