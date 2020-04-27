### Challenge
```
Neko Hero

Please join us in our campaign to save the catgirls once and for all, as the COVID-19 virus is killing them all and we need to provide food and shelter for them!
nya~s and uwu~s will be given to those who donate!
and headpats too!

Dev: William
```

### Recon & Solve
( Lesson: Make a run book else it might take hours on one problem which is easy )
* For image steganography, start with `file, strings, xxd, binwalk, exiftool` for the comments tailers and unique strings found
  - did not relieve anything
* LSB stegano --> `zsteg -a` option
  - did not detect any trace of flag either
* The next possibility is visual stegano --> use gimp or photoForensics
  * Image historgram --> gave a trace of the flag 
  * Looking at only the GREEN layer of image revealed more but not the full flag... 
* Stegsolve it is! for looking at each plan of color Green as the background is green ( Green Plane 0 to get full flag)

### Flag
* rtcp{s4vE_@LL_7h3m_c4tG1Rl$}