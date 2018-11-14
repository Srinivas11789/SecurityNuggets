### Winter sport

### The Challenge:

======= Difficulty level : Easy ========

I have a friend named Jake.We were watching a football tournament on one fine chilly morning. Meanwhile Jake's sister Susan did something mischievous which cause Jake to lose some really important data. We could only find this piece of evidence, can you recover it for him?

========== Authors : cr4ck3t, stuxn3t ==========

### Approach:

* Using VI editor to look at the pdf internals
  - exposes the embedded ".7z" file present within the pdf
  - One of the object stream is the zip file contents, trying to decompress or decode the stream
  - Objective:
    - Using qpdf with a command to decompress reveals the 7z magic number in the object stream
    - Command: qpdf -pdf -object-stream=disable file.pdf
    - Or using zlib.decompress for corresponding stream with python gives the decompressed stream
  - Using this stream to create a file that would become a .7z file
  - Decompressing this file returns omg.pdf which when opened gives weird special character strings
  - omg.pdf shows different content based on the reader -> in mac it shows nothing, but in browser it shows a special char string

* Using VI or Sublime and selecting all shows white spaces in all the first few lines
  - Try a white space stegano tool to extract the contents
  - Using stegsnow -C omg.pdf returns the flag

* I solved half of this challenge until the extraction of the omg.pdf file
  - Good introduction to the world of whitespace steganography

* I diverted after the part 1 of this challenge into the pdf file --> omg.pdf
  - Having done some anti forensics of zip file in defcon ctf, I started to reconstruct the omg.pdf which was broken
  - I assumed the graphic image block existing in the pdf file would have the flag and tried to recontruct the image 
  - Studied the internals of the pdf file
  - Attached the flow diagram of the pdf
  - Studied Trailers, root, objects, xref, streams and the flow of a pdf
  - Parallely checking with the qpdf --check omg.pdf while I edit to recontruct the flow
  - Some references below:

* Lesson Learnt: Approach the challenge based on the difficulty, an easy challenge should have a easy way to proceed and solve for the solution

* A Quick look at white space steganography
