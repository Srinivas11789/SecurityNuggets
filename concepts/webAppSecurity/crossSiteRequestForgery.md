## Cross Site Scripting

* Brief:
Behavior of executing unauthorized commands as a trusted user to a web site. Tricking the user to execute unauthroized command or instruction to a website already authenticated by the user. 

## Exploiting or Dependant on what Trust:
* Depends on the trust that the browser has with the web page 

### What is it?
* Hidden image tags or script that invokes an instruction to a particular url with the current users authentication + without authorization, delivered through image loading or url clicks. An unintended action like money transfer or password change or account delete could be initiated causing damage to the user.

### Payload?
* Dashboard or blogs with images that can trigger csrf without users intention, when the particular image loads
* Corresponding urls through email and web content

### Vulnerability? How?
* 

### Mitigation:
* Initial efforts involved disabling the HTTP GET request usage for critical state changing requests to the website. 

#### * Server Side Fix:
* Separate csrf cookie for important or crucial activity like payments

#### * Client Side Fix:

### How does it attack the Server?
* It doesnt attack the server directly but affects the servers trust with respect to the user

### How does it attack the Client?
* Perform actions which are critical without the users knowledge 

### What is stolen? How will it affect?

### What else can be done with the attack?

### Summary:

* Data at Risk:
* Threat:
* Vulnerability:
* Exploit:
* Mitigation:


