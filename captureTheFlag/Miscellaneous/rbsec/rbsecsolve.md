## RB Sec Solving

## Problem:
Given a visiting card with a series of HEX digits at the back, with a signature and highlight.

## Analysis:
* Looks like a packet hex bits
* Converting hex to ASCII provides some characters which appears to be a good lead initially
* Use Hexed.it or python

## Implementation:
* Converting into ASCII using HEXED.it, some jumbled characters are visible - clearly ballonsec is visiable among the jumbled letter
	* Restructuring the jumbled ballonsec found that the characters were left shift 1
* Left shift 1 provides the email address and asks to tell about your favourite Hack...

