## Cross Site Scripting

* Brief:
- Is a code injection attack targeted on the client through the browsers, to steal confidential information + authentication.  

### What is it?
* Rogue code <Mostly Javascript> embedded in the web page to make it execute at the client end. 
* Even when same origin policy as in effect, XSS works as the script embedded in the page is served from the web server itself.

-----> Persistent XSS:
* Occurs in public web contents of a profile like social media, blogs etc.
* Malicious script fed into the profile or blog contents --> saved in the server --> served to all the clients
* No requirement to target an individual as it is automatically distributed.
* 

-----> Non Persistent XSS or Reflective or DOM based:
* Malicious link with the webpage and the input is distributed through phishing and clicked by the user
* Webpage link with script as input --> URL --> Phishing to user click
* Targetting a required individual is required.

### Vulnerability? How?

### Mitigation:

#### * Server Side Fix:

#### * Client Side Fix:

### How does it attack the Server?
* 

### How does it attack the Client?
* 

### What is stolen? How will it affect?
* Steal page content
* Steal cookies
* 

### What else can be done with the attack?
* 

### Summary:

* Data at Risk:
* Threat:
* Vulnerability:
* Exploit:
* Mitigation:


