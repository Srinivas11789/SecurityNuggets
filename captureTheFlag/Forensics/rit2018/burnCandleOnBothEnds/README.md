## RIT CTF 

### Forensics 1: 
Burn the candle on both ends
* It's a two step process

### Think Think
* Given a image file,
  - Look for embedded items in the image --> found a zip file
  - The zip file has the flag.txt file 
  - As the zip file looks encrypted, try using any zip crack tools to bruteforce password
* Zip file seems to be AES encrypted (possibly due to iv or salt) --> using fcrackzip with dictionary attack fails!
* Extracting the password hash from the zip file and cracking hash with dictionary succeeds (using John)!

### Steps
* Investigate starting from `file` to `binwalk` command
* Use `binwalk` to look at the contents of the zip file for embedded items and extract
  - Details: `binwalk candle.zip`
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/binwalk1.png" title="Img">
  - Extract: `binwalk --dd='.*' candle.zip`
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/binwalk2.png" title="Img2">
* Use `zipdetails` to view the details of the zip file
  - `flag.txt` is found in the zip file - Encrypted
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/zipDetails.png" title="Img2">
  - By default resorting to `fcrackzip` with dictionary attack faile - possibly due to salt <I assume it is, will verify and update soon!>
* Use `johnTheRipper` tool `zip2john` to extract the hash of the zip file and then use `john` to crack the obtained hash revealed the answer (`rockyou` wordlist)
  - Obtaining Hash
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/hash.png" title="hash">
  - Cracking with `John` with `rockyou wordlist`
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/johnCrack.png" title="john">
* Using the password `stegosaurus` obtained from john, successfully extracts the flag
  <img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/rit2018/burnCandleOnBothEnds/flag.png" title="flag">

-- Busy travelling this weekend (Ctf), solving it after the ctf ended!..


