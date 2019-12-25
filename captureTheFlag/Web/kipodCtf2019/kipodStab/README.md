# Web 1 --> Kipodstab

### Challenge
```
The one who stabbed me will never be exposed.
http://ctf.kaf.sh:3040/
```

### Recon, Explore and Hits

* Connecting with Chrome returns a `Apache2 Debian Default Page`
* Default debian page
```
srimbp-623:kipodStab sri$ curl http://ctf.kaf.sh:3040/
<!DOCTYPE html
  PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Apache2 Debian Default Page: It works</title>
  <style type="text/css" media="screen">
    * {
      margin: 0px 0px 0px 0px;
      padding: 0px 0px 0px 0px;
    }

    body,
    html {
      padding: 3px 3px 3px 3px;

      background-color: #D8DBE2;

      font-family: Verdana, sans-serif;
      font-size: 11pt;
      text-align: center;
    }

    div.main_page {
      position: relative;
      display: table;

      width: 800px;

      margin-bottom: 3px;
      margin-left: auto;
      margin-right: auto;
      padding: 0px 0px 0px 0px;

      border-width: 2px;
      border-color: #212738;
      border-style: solid;

      background-color: #FFFFFF;

      text-align: center;
    }

    div.page_header {
      height: 99px;
      width: 100%;

      background-color: #F5F6F7;
    }

    div.page_header span {
      margin: 15px 0px 0px 50px;

      font-size: 180%;
      font-weight: bold;
    }

    div.page_header img {
      margin: 3px 0px 0px 40px;

      border: 0px 0px 0px;
    }

    div.table_of_contents {
      clear: left;

      min-width: 200px;

      margin: 3px 3px 3px 3px;

      background-color: #FFFFFF;

      text-align: left;
    }

    div.table_of_contents_item {
      clear: left;

      width: 100%;

      margin: 4px 0px 0px 0px;

      background-color: #FFFFFF;

      color: #000000;
      text-align: left;
    }

    div.table_of_contents_item a {
      margin: 6px 0px 0px 6px;
    }

    div.content_section {
      margin: 3px 3px 3px 3px;

      background-color: #FFFFFF;

      text-align: left;
    }

    div.content_section_text {
      padding: 4px 8px 4px 8px;

      color: #000000;
      font-size: 100%;
    }

    div.content_section_text pre {
      margin: 8px 0px 8px 0px;
      padding: 8px 8px 8px 8px;

      border-width: 1px;
      border-style: dotted;
      border-color: #000000;

      background-color: #F5F6F7;

      font-style: italic;
    }

    div.content_section_text p {
      margin-bottom: 6px;
    }

    div.content_section_text ul,
    div.content_section_text li {
      padding: 4px 8px 4px 16px;
    }

    div.section_header {
      padding: 3px 6px 3px 6px;

      background-color: #8E9CB2;

      color: #FFFFFF;
      font-weight: bold;
      font-size: 112%;
      text-align: center;
    }

    div.section_header_red {
      background-color: #CD214F;
    }

    div.section_header_grey {
      background-color: #9F9386;
    }

    .floating_element {
      position: relative;
      float: left;
    }

    div.table_of_contents_item a,
    div.content_section_text a {
      text-decoration: none;
      font-weight: bold;
    }

    div.table_of_contents_item a:link,
    div.table_of_contents_item a:visited,
    div.table_of_contents_item a:active {
      color: #000000;
    }

    div.table_of_contents_item a:hover {
      background-color: #000000;

      color: #FFFFFF;
    }

    div.content_section_text a:link,
    div.content_section_text a:visited,
    div.content_section_text a:active {
      background-color: #DCDFE6;
      color: #000000;
    }

    div.content_section_text a:hover {
      background-color: #000000;
      color: #DCDFE6;
    }
  </style>
</head>

<body>
  <div class="main_page">
    <div class="page_header floating_element">
      <img src="/icons/openlogo-75.png" alt="Debian Logo" class="floating_element" />
      <span class="floating_element">
        Apache2 Debian Default Page
      </span>
    </div>
    <div class="content_section floating_element">
      <div class="section_header section_header_red">
        <div id="about"></div>
        It works!
      </div>
      <div class="content_section_text">
        <p>
          This is the default welcome page used to test the correct
          operation of the Apache2 server after installation on Debian systems.
          If you can read this page, it means that the Apache HTTP server installed at
          this site is working properly. You should <b>replace this file</b> (located at
          <tt>/var/www/html/index.html</tt>) before continuing to operate your HTTP server.
        </p>
        <p>
          If you are a normal user of this web site and don't know what this page is
          about, this probably means that the site is currently unavailable due to
          maintenance.
          If the problem persists, please contact the site's administrator.
        </p>
      </div>
      <div class="section_header">
        <div id="changes"></div>
        Configuration Overview
      </div>
      <div class="content_section_text">
        <p>
          Debian's Apache2 default configuration is different from the
          upstream default configuration, and split into several files optimized for
          interaction with Debian tools. The configuration system is
          <b>fully documented in
            /usr/share/doc/apache2/README.Debian.gz</b>. Refer to this for the full
          documentation. Documentation for the web server itself can be
          found by accessing the <a href="https://www.docker.com/" style="color: #389fee;">manual</a> if the <tt>apache2-doc</tt>
          package was installed on this server.
        </p>
        <p>
          The configuration layout for an Apache2 web server installation on Debian systems is as follows:
        </p>
        <pre>
/etc/apache2/
|-- apache2.conf
|       `--  ports.conf
|-- mods-enabled
|       |-- *.load
|       `-- *.conf
|-- conf-enabled
|       `-- *.conf
|-- sites-enabled
|       `-- *.conf
          </pre>
        <ul>
          <li>
            <tt>apache2.conf</tt> is the main configuration
            file. It puts the pieces together by including all remaining configuration
            files when starting up the web server.
          </li>
          <li>
            <tt>ports.conf</tt> is always included from the
            main configuration file. It is used to determine the listening ports for
            incoming connections, and this file can be customized anytime.
          </li>
          <li>
            Configuration files in the <tt>mods-enabled/</tt>,
            <tt>conf-enabled/</tt> and <tt>sites-enabled/</tt> directories contain
            particular configuration snippets which manage modules, global configuration
            fragments, or virtual host configurations, respectively.
          </li>
          <li>
            They are activated by symlinking available
            configuration files from their respective
            *-available/ counterparts. These should be managed
            by using our helpers
            <tt>
              a2enmod,
              a2dismod,
            </tt>
            <tt>
              a2ensite,
              a2dissite,
            </tt>
            and
            <tt>
              a2enconf,
              a2disconf
            </tt>. See their respective man pages for detailed information.
          </li>
          <li>
            The binary is called apache2. Due to the use of
            environment variables, in the default configuration, apache2 needs to be
            started/stopped with <tt>/etc/init.d/apache2</tt> or <tt>apache2ctl</tt>.
            <b>Calling <tt>/usr/bin/apache2</tt> directly will not work</b> with the
            default configuration.
          </li>
        </ul>
      </div>
      <div class="section_header">
        <div id="docroot"></div>
        Document Roots
      </div>
      <div class="content_section_text">
        <p>
          By default, Debian does not allow access through the web browser to
          <em>any</em> file apart of those located in <tt>/var/www</tt>,
          <a href="http://httpd.apache.org/docs/2.4/mod/mod_userdir.html" rel="nofollow">public_html</a>
          directories (when enabled) and <tt>/usr/share</tt> (for web
          applications). If your site is using a web document root
          located elsewhere (such as in <tt>/srv</tt>) you may need to whitelist your
          document root directory in <tt>/etc/apache2/apache2.conf</tt>.
        </p>
        <p>
          The default Debian document root is <tt>/var/www/html</tt>. You
          can make your own virtual hosts under /var/www. This is different
          to previous releases which provides better security out of the box.
        </p>
      </div>
      <div class="section_header">
        <div id="bugs"></div>
        Reporting Problems
      </div>
      <div class="content_section_text">
        <p>
          Please use the <tt>reportbug</tt> tool to report bugs in the
          Apache2 package with Debian. However, check <a
            href="http://bugs.debian.org/cgi-bin/pkgreport.cgi?ordering=normal;archive=0;src=apache2;repeatmerged=0"
            rel="nofollow">existing bug reports</a> before reporting a new bug.
        </p>
        <p>
          Please report bugs specific to modules (such as PHP and others)
          to respective packages, not to the web server itself.
        </p>
      </div>
    </div>
  </div>
  <div class="validator">
  </div>
</body>

</html>srimbp-623:kipodStab sri$ 

``` 
* checked for known pages like `robots.txt` 

* (1.) `DEFAULTS` --> something wrong with the default page and configuration that could be bypassed.

* (2.) `BUGS` --> bugs in current version of the apache2 that could be exploited. The default web page already has a link to the `bug reports`...

* `The one who stabbed me will never be exposed.` --> never be exposed --> so flag is indeed hidden here?

* Check for known owasp top 10 --> 
```
- file traversal
```

* `DirBuster` or `dirb` results show
  - `/index.html` -> as already found
  - `/icons/` -> directory with all the files
  - `.htaccess` or `.htpasswd` -> 403 forbidden

* Going back again to the default page --> links to 
  - manual --> docker
  - public_html --> leads to apache doc --> `userDir module` ( mod_userdir apache module)

* Now that fits the challenge hint --> one who stabs is never exposed --> some user or username should be existing --> found out by https://<target>/~<username> --> should return 200 for a successful existence

* After trying out some default usernames like root, bob, trudy and some names from the apache documents --> still no success

* Looking for enumeration tools online found out,
  - metasploit module
  - apache-users
  - wfuzz or dirb or dirbuster or dirble did not help much here. Maybe they do --> dig further....
  - nmap http-userdir-enum

```
nmap -sV --script=http-userdir-enum http://ctf.kaf.sh:3040/
apache-users -h ctf.kaf.sh -l /usr/share/wordlists/metasploit/unix_users.txt -p 3040 -s 0 -e 200 -t 15

```
root@kali:~/Downloads# apache-users -h ctf.kaf.sh -l /usr/share/wordlists/dirbuster/apache-user-enum-2.0.txt -p 3040 -s 0 -e 200 -t 10
Execution time: 1049 seconds!
```

```
root@kali:~/Downloads# dirb http://ctf.kaf.sh:3040/ /usr/share/wordlists/dirbuster/apache-user-enum-1.0.txt 

-----------------
DIRB v2.22    
By The Dark Raver
-----------------

START_TIME: Tue Dec 24 22:43:52 2019
URL_BASE: http://ctf.kaf.sh:3040/
WORDLIST_FILES: /usr/share/wordlists/dirbuster/apache-user-enum-2.0.txt

-----------------

GENERATED WORDS: 10341                                                         

---- Scanning URL: http://ctf.kaf.sh:3040/ ----
+ Remaining scan stats:                                                                                                                                         
Words: 7934 | Directories: 0
--> Testing: http://ctf.kaf.sh:3040/~adamsky                                           
-----------------
END_TIME: Tue Dec 24 23:11:53 2019
DOWNLOADED: 10341 - FOUND: 0
```


  - Using different wordlists but still no success
    - metasploit/unix_users.txt
    - commons.txt
    - dirb/ or dirbusted/
    - nmap.lst
  
* Also, just in case retried hackerone apache CTF -> andre's writeup for admin pages.

* Checked HTTP methods as well --> Nothing appeared to follow up...

* One thing that is promising is `mod_userdir` hacks.. Redid with dirb, apache-users, dirbuster, nmap. Nothing found with a number of wordlists.

* Another possible hit would be to purse other links and review them. 

* Had already pursued reading a number of bugs in the debian bugs link and reviewed different bugs to check if there is any vuln that can be exploited.

* Reading the description again. The `manual` url was always docker and apache2-doc. Tried for sometime with local documentation links for apache with the webserver. Nothing obvious.

* Stumbled upon another idea. Compare it with the REAL default debian page. The manual link with docker and apache2-doc outstands. Dig more. `https://packages.debian.org/unstable/apache2-doc`

* Checked docker.com
  - certs
  - possible names
  - manuals
  - dockerfile
    - hashes, names, users, files

* All night, I retried and reread this challenge and assets more than once --> Tried different files and usernames at the web server but in vain.

* The Flag was just to access the `Dockerfile` in the web server. It was obvious --> Given `docker.com` --> First things first you should check the Dockerfile in the server ( I had been using or trying with docker user, docker user-agent, docker as usernames in vain...)

* As anticipated the last hit was a success. I kept retrying with `dockerfile` and other stuff related to docker in vain. Also overthinking into reading all the apache2 dockerfiles at github and docker hub.

* `Dirsearch` proved to be very useful here
```
srimbp-623:dirsearch sri$ python3 dirsearch.py -u http://ctf.kaf.sh:3040 -e *

 _|. _ _  _  _  _ _|_    v0.3.9
(_||| _) (/_(_|| (_| )

Extensions: CHANGELOG.md | HTTP method: get | Threads: 10 | Wordlist size: 6103

Error Log: /Users/sri/Desktop/dev/personalGit/algo/SecurityNuggets/captureTheFlag/Web/kipodCtf2019/kipodStab/dirsearch/logs/errors-19-12-25_11-55-23.log

Target: http://ctf.kaf.sh:3040

[11:55:23] Starting: 
[11:55:28] 403 -  199B  - /.hta                                     
[11:55:28] 403 -  199B  - /.ht_wsr.txt
[11:55:28] 403 -  199B  - /.htaccess-local
[11:55:28] 403 -  199B  - /.htaccess-dev
[11:55:28] 403 -  199B  - /.htaccess-marco
[11:55:28] 403 -  199B  - /.htaccess.BAK
[11:55:28] 403 -  199B  - /.htaccess.bak1
[11:55:28] 403 -  199B  - /.htaccess.orig
[11:55:28] 403 -  199B  - /.htaccess.old
[11:55:28] 403 -  199B  - /.htaccess.txt
[11:55:28] 403 -  199B  - /.htaccess.sample
[11:55:28] 403 -  199B  - /.htaccess.save
[11:55:28] 403 -  199B  - /.htaccess_extra
[11:55:28] 403 -  199B  - /.htaccess_orig
[11:55:28] 403 -  199B  - /.htaccessBAK
[11:55:28] 403 -  199B  - /.htaccess_sc
[11:55:28] 403 -  199B  - /.htaccessOLD2
[11:55:28] 403 -  199B  - /.htaccessOLD
[11:55:28] 403 -  199B  - /.htaccess~
[11:55:28] 403 -  199B  - /.htgroup
[11:55:28] 403 -  199B  - /.htpasswd-old
[11:55:28] 403 -  199B  - /.htpasswd_test
[11:55:28] 403 -  199B  - /.htpasswds
[11:55:28] 403 -  199B  - /.htusers
[11:56:15] 200 -  107B  - /Dockerfile                                                                             
[11:56:26] 301 -  237B  - /icons  ->  http://ctf.kaf.sh:3040/icons/                                   
[11:56:28] 200 -    9KB - /index.html                                                                          
                                                                                                                  
Task Completed
srimbp-623:dirsearch sri$ 
```
* It was obvious `Dockerfile` was the one to build the image!

* The flag...
```
srimbp-623:kipodStab sri$ curl http://ctf.kaf.sh:3040/Dockerfile
FROM httpd:alpine

WORKDIR /usr/local/apache2/htdocs/

COPY . .

# Flag is KAF{dOn7_5748_doCK3R_CON741n3R2}srimbp-623:kipodStab sri$ 
```

### References
* https://books.google.com/books?id=FD1lDwAAQBAJ&pg=PT329&lpg=PT329&dq=apache-users+kali&source=bl&ots=0mVcuigl1i&sig=ACfU3U2wwpjjP8MXDfpcDE_u--0j5j3JoQ&hl=en&ppis=_c&sa=X&ved=2ahUKEwj7-u-ojs3mAhW1KX0KHd3QB0A4ChDoATACegQIBhAB#v=onepage&q=apache-users%20kali&f=false
* 

  
