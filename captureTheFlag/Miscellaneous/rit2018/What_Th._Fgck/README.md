### Challenge: What_Th._Fgck

### Given an expression which seems random: OGK:DI_G;lqk"Kj1;"a"yao";fr3dog0o"vdtnsaoh"patsfk{+

### Think, Think, Think

* Encode/Decode: Doesnt seemm to resemble any encoding: Try various decoding stuff to identify substrings --> test substrings as well
* Google Search: Search the string with Google, also try substrings with google (from just OGk to different substrings)
  - one of the promising substring is "vdtnsaoh" which is a keyboard layout

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Miscellaneous/rit2018/What_Th._Fgck/search.png" title="search">

### Steps
* Try substrings in Google search for any promising hit - obtained a particular keyboard layout and converted to qwerty
* Convert the string from the respective keyboard format to obtain the flag
* Using this project - https://github.com/bahamas10/node-dvorak, we can decode the given string

### Flag

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Miscellaneous/rit2018/What_Th._Fgck/flag.png" title="flag">
