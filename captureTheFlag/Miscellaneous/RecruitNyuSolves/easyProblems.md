### Easy Examples -- Pieces Of Cake

##### View Source => 
Client side source code has the flag (Inference: Client Side code is always vulnerable to any data leaks)

##### PHP => 
Php code with GET parameter, Code contains logic for 2 different Get parameters. One of the Get parameter in the request if mentioned "?param=flag" reveals the flag

##### Wirysharks =>
Follow the TCP or HTTP Stream in the packet capture, a HTTP 404 appears, the data part in the 404 reveals the flag. (Inference: 404 could leak data, caution about any HTTP packets should be taken as their data could leaks potential confidential information)

##### thestream =>
Follow the TCP stream to find out a HTTP 200 packet with png data exchanged. Dump the packet using Export->HTTP->PNG in wireshark to dump the bytes into a png file which has the flag in the image

##### Corrupted File problem =>
The magic numbers have been removed clearly it shows 787878787878 in the start. The type command outputs the file being only data. Research on some possible flags at the tail of the data and near the magic numbers like IEND and IHDR reveal they are part of PNG file chunks. Replace the magic number with PNG file magic numbers and export file as .png

##### Bigc =>
A C program provided with long lines of code. Answer string is already hard coded with some hex bytes. There is a array of array data structure with mapping. The input from stdin is taken and processed with the mapping and result is produced. This result is matched with the answer key length wise and string match. Once successfull the flag is known. Make a table with the respective mapping of input to the respective output string in the map. Image of worked out table attached. Flag is revealed

