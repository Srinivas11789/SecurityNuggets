# Info challenge - Forensics Steganography

### Given
* `info.jpg` - image file with some hidden information
* Difficulty: Medium

### Thinking...
* As usual, check the image information in all the tools
  - exiftool
  - img_stat
  - file
  - binwalk 
  - exif
  - Just view file in hex editor or just as easy as cat
* Everything seemed usual except for the comment `badisbad`
* Using `steghide` to extact files with the comment as the passphrase is a success..
* (solved this after the ctf end).. Got pulled into jsteg and into another approach as a detour!

### Steps: 
* Look at the image information
* Collect unusual or user entered info like comments, trailer or headers
* Use steghide to extract with known string as password

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/saudiAndOmanNationalCtf/info/asset1.png" title="hexed">

* complete steps

<img src="https://srinivas11789.github.io/SecurityNuggets/captureTheFlag/Forensics/saudiAndOmanNationalCtf/info/asset2.png" title="steps">

### Flag
flag{Stegn0_1s_n!ce}

### Other attempts:
```
root@kali:~/Downloads/info# cat extract.go 
package main

import (
    "fmt"
    "os"
    "github.com/lukechampine/jsteg"
)

func main() {
    f, _ := os.Open("info.jpg")
    hidden, _ :=  jsteg.Reveal(f)
    fmt.Println(hidden)
}

root@kali:~/Downloads/info# go run extract.go 
[0 32 34 162 80 44 102 15 1 109 232 66 0 2 64 12 10 151 96 62 2 34 129 240 166 241 214 198 136 156 1 32 235 171 4 48 5 128 131 206 152 73 116 16 53 34 133 53 9 4 33 1 232 196 160 68 58 108 16 131 2 44 1 181 132 48 0 23 84 5 90 160 131 47 40 16 40 0 9 48 240 112 128 104 148 33 117 0 38 144 82 130 8 44 36 182 131 60 4 3 176 168 112 24 2 243 129 17 188 96 21 68 62 96 52 1 106 144 216 0 82 7 13 65 80 0 125 72 56 136 29 80 97 84 64 65 136 50 49 165 185 124 82 132 59 133 76 27 32 28 210 253 138 110 2 13 64 136 144 192 161 193 27 219 192 51 34 230 218 8 101 3 3 131 242 8 128 82 52 7 164 141 226 196 35 28 37 0 16 104 10 181 225 10 18 97 4 160 97 16 138 2 140 113 2 11 171 176 12 154 80 17 110 84 123 116 147 33 34 182 146 0 214 92 99 89 83 34 136 90 219 133 37 4 6 143 98 26 146 44 6 202 137 217 165 233 39 250 33 160 65 178 69 108 254 12 186 14 102 17 19 12 215 184 1 188 81 32 37 205 200 72 147 6 225 88 209 67 72 89 2 72 184 26 0 160 18 208 16 164 223 0 113 201 81 34 19 68 54 211 35 9 118 88 66 76 18 1 84 56 65 192 4 2 129 165 6]

```
