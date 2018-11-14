#!/usr/bin/env bash

#################################################################################################
#
# * Filename: harden.sh
# * Goal: Hardening the Linux Kernel + Web Server
# * Usage: With Vagrant - call from the vagrant file
# * Description: Header descriptions and reason in the infoSecAudit.md file
#
#################################################################################################

### 1. Linux Libraries: apt update to sync with the repository for updated libararies and updates

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y autoremove
sudo apt-get -y autoclean

### 2. Install the Web Server - Apache2 with the SQL database

# Apache2 install
sudo apt-get install -y apache2

# Setting the apache default web hosting folder
if ! [ -L /var/www/html ]; then
  rm -rf /var/www/html
  ln -fs /vagrant /var/www/html
fi

# Database configuration - initial default username and password
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password vagrant'
sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password vagrant'

# Database install
sudo apt-get install -y mysql-server

### 4. Disable/Remove known less secure services/protocols like plain text terminal protocols - Telnet, Netcat

# Telnet protocol
sudo apt-get -y purge telnet

# File transfer plaintext
sudo apt-get -y purge xinetd nis yp-tools tftpd atftpd tftpd-hpa telnetd rsh-server rsh-redone-server

# Netcat protocol
sudo apt-get -y purge netcat

# network file sharing services
sudo apt-get -y purge nfs-kernel-server nfs-common

# rpc services and port mappings
sudo apt-get -y purge portmap rpcbind

# Mount directories
sudo apt-get -y purge autofs

### 5. SSH Hardening

# Custom port SSH Run to hide from port scanning - more than 1024 as they are common reserved ports that are scanned,Delete existing config and add new custom port
sudo sed -i '/Port/d' /etc/ssh/sshd_config
sudo sh -c 'echo "Port 8000" >> /etc/ssh/sshd_config'

# ssh Root login disable
sudo sh -c 'echo "PermitRootLogin prohibit-password" >> /etc/ssh/sshd_config'

# Set account lockout and ssh sessions to prevent brute force attacks against weak passwords
ufw limit OpenSSH
sudmmao sh -c 'echo "MaxAuthTries 5" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "MaxSessions 5" >> /etc/ssh/sshd_config'

# SSH Tuning - Disable features that are not required to reduce attack surface
sudo sh -c 'echo "AllowTcpForwarding no" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "AllowStreamLocalForwarding no" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "GatewayPorts no" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "PermitTunnel no" >> /etc/ssh/sshd_config'

# Disable weak ciphers and modes - Only CTR mode secure ciphers - some clients dont support very secure modes like GCM hence resorting to CTR
sudo sh -c 'echo "Ciphers aes128-ctr,aes192-ctr,aes256-ctr" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "MACs hmac-sha2-256,hmac-sha2-512,hmac-sha1" >> /etc/ssh/sshd_config'
sudo sh -c 'echo "KexAlgorithms ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521" >> /etc/ssh/sshd_config'

# sDisable password authentication and enable public key authentication if possible
sudo sh -c 'echo "PasswordAuthentication no" >> /etc/ssh/sshd_config'

# Regenerate SSH Keychain or delete all the public key and add only one authorized key - fully detach from the default user - vagrant
# Setting done in the vagrant file itself as public key file was not copied due to late file share linking by vagrant
# Uncomment during production purposes - commented to debug the machine using default user
#sudo rm -rf /etc/ssh/ssh_host_*
#sudo rm -rf ~/.ssh/authorized_keys
#sudo sh -c 'cat /vagrant/dummy.pub >> /home/dummy/.ssh/authorized_keys'

# Apply changes
sudo service ssh restart

### 6. Disable all the compilers and programming language interpreters

# Compilers disable
chmod 000 /usr/bin/byacc
chmod 000 /usr/bin/yacc
chmod 000 /usr/bin/bcc
chmod 000 /usr/bin/kgcc
chmod 000 /usr/bin/cc
chmod 000 /usr/bin/gcc
chmod 000 /usr/bin/*c++
chmod 000 /usr/bin/*g++

# Disable Python, Perl, Php, Tcl support - decision to be made on what tech the web stack will be run on, disable others

#sudo apt-get -y remove python3
#sudo apt-get -y remove python-minimal
#sudo apt-get -y remove perl
#sudo apt-get -y remove php

### 7. Firewall Setting

# Only enable ssh, http and https - disable everything else - http allowed for not secure page <static pages> hosting
ufw allow ssh
ufw allow http
ufw allow https
ufw default deny
ufw enable

### 8. Kernel Tuning

# ASLR Enable to prevent easy buffer overflow exploits
sysctl kernel.randomize_va_space=1

# Kernel Networking or Handling packets that are received at the CPU sockets - might cause CPU crash sometimes - reduce attack surface
# Reverse Path Filtering - Bogus packets that escape into the networks and make it to the CPU which cannot be routed back are discarded
sysctl net.ipv4.conf.all.rp_filter=1

# ICMP - disable control message redirects disable - ipv4 and ipv6
sysctl -w net.ipv4.conf.all.accept_redirects=0
sysctl -w net.ipv6.conf.all.accept_redirects=0
sysctl -w net.ipv4.conf.all.send_redirects=0

# Corner Cases - Disable broadcasts and bogus error messages that might cause perf or security problems
sysctl -w net.ipv4.conf.all.accept_source_route=0
sysctl -w net.ipv4.icmp_echo_ignore_broadcasts=1
sysctl -w net.ipv4.icmp_ignore_bogus_error_messages=1

# Logging of possible spoofed packets
sysctl -w net.ipv4.conf.all.log_martians=1

# Turn on execution shield
sysctl kernel.exec-shield=1

# Publish the settings
sysctl -p

### 10. User Accounts Setting

# Remove the default vagrant user and keys
# Tools like shodan and github might have the vagrant default user credentials which can be used if left in the server. Clean up after configuration
# Commented out for debug purpose - uncomment for production
#sudo deluser vagrant

# Remove past passwords reuse
sudo sh -c 'echo "password sufficient pam_unix.so use_authtok md5 shadow remember=15" >> /etc/pam.d/common-password'

# Remove default root and other usernames
#sudo cut -d: -f1 /etc/passwd | while read name ; do deluser "$name" ; done

# Add one particular username/password <strong random> for the web server
sudo useradd -m dummy
sudo echo -e "dummy\ndummy" | passwd dummy
sudo mkdir /home/dummy/.ssh
sudo touch /home/dummy/.ssh/authorized_keys
sudo sh -c 'cat /vagrant/dummy.pub >> /home/dummy/.ssh/authorized_keys'
sudo usermod -aG sudo dummy

# uncomment default vagrant user during production run
#sudo rm -rf /home/vagrant/.ssh/authorized_keys

#### 11. Enable SE Linux or AppArmour

# Ubuntu by default has appArmour
sudo /etc/init.d/apparmor start

# Selinux settings
#sudo apt install selinux-utils
#sudo setenforce 1

### 3. Disable Root - disable root
passwd -l root
passwd -l vagrant

### BIOS Settings

### 12. Set all files to read only

### 13. Disk Partition

### 14. External Device Mount disabling

### 15. Web Server hardening

# Stop apache server to add more configurations
sudo service apache2 stop

# Disable to supress apache version and other details display and just display apache as a product
sudo sed -i '/ServerTokens/d' /etc/apache2/apache2.conf
sudo sh -c 'echo "ServerTokens Prod" >> /etc/apache2/apache2.conf'
sudo sed -i '/ServerSignature/d' /etc/apache2/apache2.conf
sudo sh -c 'echo "ServerSignature Off" >> /etc/apache2/apache2.conf'
sudo sed -i '/TraceEnable/d' /etc/apache2/apache2.conf
sudo sh -c 'echo "TraceEnable Off" >> /etc/apache2/apache2.conf'

# Disable directory traversals
sudo sh -c 'echo "Options  -Indexes -Includes" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "Options  -ExecCGI" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "Options  -FollowSymLinks" >> /etc/apache2/apache2.conf'

# File inode and details protect - restricts possible social engineering of file internals
sudo sh -c 'echo "FileETag None" >> /etc/apache2/apache2.conf'

# Dos Attack Protection
# Further options with default value keepAliveTimeout(5) + MaxClients(256) + LimitRequestFields(100) + LimitRequestFieldSize could be altered based on Dos protect needed
sudo sed -i '/LimitRequestBody/d' /etc/apache2/apache2.conf
sudo sh -c 'echo "LimitRequestBody 512000" >> /etc/apache2/apache2.conf'
sudo sed -i '/Timeout/d' /etc/apache2/apache2.conf
sudo sh -c 'echo "Timeout 60" >> /etc/apache2/apache2.conf'

# Application Security Protection
sudo a2enmod headers
sudo sh -c 'echo "Header edit Set-Cookie ^(.*)$ $1;HttpOnly;Secure" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "Header always append X-Frame-Options SAMEORIGIN" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "Header set X-XSS-Protection "1; mode=block" >> /etc/apache2/apache2.conf'

# System Directory Protection
sudo sh -c 'echo "<Directory />\nOptions -Indexes\nAllowOverride None\n</Directory>" >> /etc/apache2/apache2.conf'

# Lower version of HTTP removal - harden http
sudo a2enmod rewrite
sudo sh -c 'echo "RewriteEngine On" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "RewriteCond %{THE_REQUEST} !HTTP/1.1$" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "RewriteRule .* - [F]" >> /etc/apache2/apache2.conf'

# SSL Settings to Strict

# SSL Mode
sudo a2enmod ssl

# SSL Configuration and Harden
sudo sh -c 'echo "Listen 443" >> /etc/apache2/apache2.conf'
sudo sh -c 'echo "<VirtualHost *:443>\nDocumentRoot /var/www/\nServerName www.dummy.com\nSSLEngine on\nSSLCertificateFile \"/vagrant/dummyssl.pem\"\nSSLCertificateKeyFile \"/vagrant/dummyssl.key\"\nSSLCipherSuite HIGH:!MEDIUM:!aNULL:!MD5:!RC4\n</VirtualHost>\n#SSLPassPhraseDialog  exec:/vagrant/passwd" >> /etc/apache2/apache2.conf'
#sudo sh -c 'echo "SSLCipherSuite HIGH:!MEDIUM:!aNULL:!MD5:!RC4" >> /etc/apache2/apache2.conf'
#sudo sh -c 'echo "SSLProtocol –ALL +TLSv1 +TLSv1.1 +TLSv1.2" >> /etc/apache2/apache2.conf'

# Non privilege user setting for apache2
#sudo groupadd www
#sudo useradd –g www www
#sudo sed -i '/User/d' /etc/apache2/apache2.conf
#sudo sh -c 'echo "User www" >> /etc/apache2/apache2.conf'
#sudo sed -i '/Group/d' /etc/apache2/apache2.conf
#sudo sh -c 'echo "Group www" >> /etc/apache2/apache2.conf'

# Web Reverse Proxy Nginx or ModSecurity Settings

# Install ModSecurity
sudo apt-get install -y libapache2-mod-security2

# Configuration
sudo mv /etc/modsecurity/modsecurity.conf-recommended /etc/modsecurity/modsecurity.conf
sudo sed -i "s/SecRuleEngine DetectionOnly/SecRuleEngine On/" /etc/modsecurity/modsecurity.conf
sudo sed -i "s/SecResponseBodyAccess On/SecResponseBodyAccess Off/" /etc/modsecurity/modsecurity.conf

# Apply changes to web server
sudo service apache2 start
sudo sh -c "echo dummy\n"
sudo service ssh start

# Protect the apache directory and the configurations
sudo chmod -R 750 /etc/apache2
