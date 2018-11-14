### USB Forensics

# How to start? What to look at?
* For any packet capture that was shared, always look through the communication for possible ascii strings
* Go through the descriptors and details exchanged between usb device
  - Especially fetch any unique strings exchanged (feel-it challenge has a braille string already hinting this...)
  - Also, the manufactuerer and other id is used to determine what type of device is under consideration and what to look for based on the device type..
* In USB traffic always start with "leftover capture data", 
  * this data is present in the USB Interrupt-in packet
  * this is that data that has unique details exchanged based on the io of the usb device
  * It would be evident for keyboard or mouse events where mapping could be performed to reveal activity
* Also, if the usb spec is not clear for the above method, also look for other packets with weird data
  - There are SET and GET requests
  - Most of the SET request generally have data shared (this can be a terminal data that is displayed in the LCD based on the type)
  - Look for patterns in these data which can be used for analysis

