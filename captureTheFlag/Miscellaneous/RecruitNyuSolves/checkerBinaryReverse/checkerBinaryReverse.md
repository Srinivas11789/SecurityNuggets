Given a Binary which asks for the secret message...

* Tools Used: Binary Ninja and GDB

* Control Flow --> 
	* The program received a input from stdin through fgets
	* The check function is called to check the stdin against some password
	* Once this passes give_flag function is called
	* Looking into the check function
		*  First step the length of the input is checked with a constant through strlen - This has to match 0x13 matches 19 but 20 character match works
		* Second the values are compared byte by byte against hex values
		* Easily we know they are compared against "aqua"
		* Then a for loop is executed with some byte matching done
		* Looking closely the characters are moved one by one and compared with other character in the string possibly a palindrome matching
		* Construct aqua such that it is of 20 characters and palindrome
		* aquaaquaauuaauqaauqa --- first and last char match, moving around the loop
		* Use GDB and keep break points now and then to look at the registers and see what is compared



