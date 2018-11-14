# RCTF WriteUp

# Challenge: git 
# Type: Misc 

# Given:
# A folder with HelloWorld.txt file with a ".git" folder

# Flag:
# RCTF{gIt_BranCh_aNd_l0g}

### Debug Logs:

# Boiling Down to the answer:
"""
Srinivass-MacBook-Pro:git 2 darkknight$ git reflog
22d3349 (HEAD -> rctf, master, develop) HEAD@{0}: checkout: moving from master to rctf
22d3349 (HEAD -> rctf, master, develop) HEAD@{1}: checkout: moving from develop to master
22d3349 (HEAD -> rctf, master, develop) HEAD@{2}: rebase -i (finish): returning to refs/heads/develop
22d3349 (HEAD -> rctf, master, develop) HEAD@{3}: rebase -i (start): checkout 22d3349
f671986 HEAD@{4}: checkout: moving from master to develop
22d3349 (HEAD -> rctf, master, develop) HEAD@{5}: checkout: moving from develop to master
f671986 HEAD@{6}: checkout: moving from master to develop
22d3349 (HEAD -> rctf, master, develop) HEAD@{7}: checkout: moving from rctf to master
f671986 HEAD@{8}: commit: Revert
f4d0f6d HEAD@{9}: commit: Flag
22d3349 (HEAD -> rctf, master, develop) HEAD@{10}: checkout: moving from master to rctf
22d3349 (HEAD -> rctf, master, develop) HEAD@{11}: commit (initial): Initial Commit
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout -b rctf f4d0f6d
fatal: A branch named 'rctf' already exists.
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout -b rctf1 f4d0f6d
Switched to a new branch 'rctf1'
Srinivass-MacBook-Pro:git 2 darkknight$ ls
HelloWorld.txt flag.txt
Srinivass-MacBook-Pro:git 2 darkknight$ cat flag.txt 
RCTF{gIt_BranCh_aNd_l0g}
Srinivass-MacBook-Pro:git 2 darkknight$ 
"""

# All Possible Tries:
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG 
Revert
# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 说明将会终止提交。
#
# 位于分支 rctf
# 要提交的变更：
#	删除：     flag.txt
#
Srinivass-MacBook-Pro:git darkknight$ git checkout rctf
error: pathspec 'rctf' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git bramcnch
git: 'bramcnch' is not a git command. See 'git --help'.
Srinivass-MacBook-Pro:git darkknight$ git branch
  develop
* master
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ git checkout .
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git branch
  develop
* master
Srinivass-MacBook-Pro:git darkknight$ git checkout -b rctf
Switched to a new branch 'rctf'
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git status
On branch rctf
nothing to commit, working tree clean
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ git checkout .
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git reset head
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git reset head --hard
HEAD is now at 22d3349 Initial Commit
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat HelloWorld.txt 
HelloWorld
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat HelloWorld.txt 
HelloWorld
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ pwd
/Users/darkknight/Downloads/NewDownload10Oct/git
Srinivass-MacBook-Pro:git darkknight$ ls -ltr
total 8
-rw-r--r--  1 darkknight  staff  11 May 20 03:41 HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git checkout 
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:git darkknight$ git checkout 
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:git darkknight$ git checkout 
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout HEAD^ flag.txt
error: pathspec 'HEAD^' did not match any file(s) known to git.
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git reset HEAD .
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout .
Srinivass-MacBook-Pro:git darkknight$ ;ls
-bash: syntax error near unexpected token `;'
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat HelloWorld.txt 
HelloWorld
Srinivass-MacBook-Pro:git darkknight$ ;s
-bash: syntax error near unexpected token `;'
Srinivass-MacBook-Pro:git darkknight$ git clean
fatal: clean.requireForce defaults to true and neither -i, -n, nor -f given; refusing to clean
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git clean --force
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat HelloWorld.txt 
HelloWorld
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG `
> 
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG `
> 
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG 
Revert
# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 说明将会终止提交。
#
# 位于分支 rctf
# 要提交的变更：
#	删除：     flag.txt
#
Srinivass-MacBook-Pro:git darkknight$ git checkout ./*
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout develop
Switched to branch 'develop'
Srinivass-MacBook-Pro:git darkknight$ git checkout ./*
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> develop, rctf, master)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ git reset HEAD .
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout .
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git reset -- flag.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout -- flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat HelloWorld.txt 
HelloWorld
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout -- flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git checkout -- 
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:git darkknight$ git checkout ./*
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git stash
No local changes to save
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git ls-files -d | xargs git checkout --
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cd ..
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd gti
-bash: cd: gti: No such file or directory
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git status
On branch develop
nothing to commit, working tree clean
Srinivass-MacBook-Pro:git darkknight$ git checkout master
Switched to branch 'master'
Srinivass-MacBook-Pro:git darkknight$ git ls-files -d | xargs git checkout --
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG 
Revert
# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 说明将会终止提交。
#
# 位于分支 rctf
# 要提交的变更：
#	删除：     flag.txt
#
Srinivass-MacBook-Pro:git darkknight$ git checkout rctf
Switched to branch 'rctf'
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git ls-files -d | xargs git checkout --
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ git revert
usage: git revert [<options>] <commit-ish>...
   or: git revert <subcommand>

    --quit                end revert or cherry-pick sequence
    --continue            resume revert or cherry-pick sequence
    --abort               cancel revert or cherry-pick sequence
    -n, --no-commit       don't automatically commit
    -e, --edit            edit the commit message
    -s, --signoff         add Signed-off-by:
    -m, --mainline <parent-number>
                          select mainline parent
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --strategy <strategy>
                          merge strategy
    -X, --strategy-option <option>
                          option for merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Srinivass-MacBook-Pro:git darkknight$ git revert -n
usage: git revert [<options>] <commit-ish>...
   or: git revert <subcommand>

    --quit                end revert or cherry-pick sequence
    --continue            resume revert or cherry-pick sequence
    --abort               cancel revert or cherry-pick sequence
    -n, --no-commit       don't automatically commit
    -e, --edit            edit the commit message
    -s, --signoff         add Signed-off-by:
    -m, --mainline <parent-number>
                          select mainline parent
    --rerere-autoupdate   update the index with reused conflict resolution if possible
    --strategy <strategy>
                          merge strategy
    -X, --strategy-option <option>
                          option for merge strategy
    -S, --gpg-sign[=<key-id>]
                          GPG sign commit

Srinivass-MacBook-Pro:git darkknight$ git checkout ./*
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout -- flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git reset -- flag.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout -- flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/COMMIT_EDITMSG 
Revert
# 请为您的变更输入提交说明。以 '#' 开始的行将被忽略，而一个空的提交
# 说明将会终止提交。
#
# 位于分支 rctf
# 要提交的变更：
#	删除：     flag.txt
#
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/HEAD 
ref: refs/heads/rctf
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/rctf 
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/rctf 
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/rctf 
22d3349a5c6fe45758daba276108137382a01caa
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/
develop  master   rctf     
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/
develop  master   rctf     
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/master 
22d3349a5c6fe45758daba276108137382a01caa
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/heads/develop 
22d3349a5c6fe45758daba276108137382a01caa
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/
heads/ tags/  
Srinivass-MacBook-Pro:git darkknight$ cat .git/refs/tags/
cat: .git/refs/tags/: Is a directory
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git darkknight$ cat .git/logs/
HEAD  refs/ 
Srinivass-MacBook-Pro:git darkknight$ cat .git/logs/
HEAD  refs/ 
Srinivass-MacBook-Pro:git darkknight$ cat .git/logs/HEAD 
0000000000000000000000000000000000000000 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187274 +0800	commit (initial): Initial Commit
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187289 +0800	checkout: moving from master to rctf
22d3349a5c6fe45758daba276108137382a01caa f4d0f6ddf6660f5c9273c84f3de64840a407bef1 zsx <zsx@zsxsoft.com> 1526187319 +0800	commit: Flag
f4d0f6ddf6660f5c9273c84f3de64840a407bef1 f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187331 +0800	commit: Revert
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187346 +0800	checkout: moving from rctf to master
22d3349a5c6fe45758daba276108137382a01caa f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187455 +0800	checkout: moving from master to develop
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187488 +0800	checkout: moving from develop to master
22d3349a5c6fe45758daba276108137382a01caa f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187817 +0800	checkout: moving from master to develop
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187876 +0800	rebase -i (start): checkout 22d3349
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187876 +0800	rebase -i (finish): returning to refs/heads/develop
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187889 +0800	checkout: moving from develop to master
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802090 -0400	checkout: moving from master to rctf
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802119 -0400	reset: moving to head
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802124 -0400	reset: moving to head
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802295 -0400	checkout: moving from rctf to develop
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802469 -0400	checkout: moving from develop to master
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526802598 -0400	checkout: moving from master to rctf
Srinivass-MacBook-Pro:git darkknight$ git checkout -- <file>
-bash: syntax error near unexpected token `newline'
Srinivass-MacBook-Pro:git darkknight$ cd ..
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git
Srinivass-MacBook-Pro:git darkknight$ git checkout -- <file>
-bash: syntax error near unexpected token `newline'
Srinivass-MacBook-Pro:git darkknight$ git checkout -- <file>
-bash: syntax error near unexpected token `newline'
Srinivass-MacBook-Pro:git darkknight$ git ls-files --deleted
Srinivass-MacBook-Pro:git darkknight$ git ls-files --deleted
Srinivass-MacBook-Pro:git darkknight$ l
s-bash: l: command not found
Srinivass-MacBook-Pro:git darkknight$ git status
On branch rctf
nothing to commit, working tree clean
Srinivass-MacBook-Pro:git darkknight$ git checkout -- flag.txt
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git darkknight$ git status
On branch rctf
nothing to commit, working tree clean
Srinivass-MacBook-Pro:git darkknight$ git ls-files --deleted
Srinivass-MacBook-Pro:git darkknight$ git rev-list -n 1 HEAD -- flag.txt
Srinivass-MacBook-Pro:git darkknight$ git checkout <commit>^ -- flag.txt
-bash: commit: No such file or directory
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ 
Srinivass-MacBook-Pro:git darkknight$ git log --diff-filter=D --summary
Srinivass-MacBook-Pro:git darkknight$ git rever -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
git: 'rever' is not a git command. See 'git --help'.

The most similar command is
	revert
Srinivass-MacBook-Pro:git darkknight$ git revert -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
On branch rctf
nothing to commit, working tree clean
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cat fl
cat: fl: No such file or directory
Srinivass-MacBook-Pro:git darkknight$ cat flag.txt
cat: flag.txt: No such file or directory
Srinivass-MacBook-Pro:git darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git darkknight$ cd ..
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
fatal: Not a git repository (or any of the parent directories): .git
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git
Srinivass-MacBook-Pro:git darkknight$ git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
Srinivass-MacBook-Pro:git darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git darkknight$ cd ..
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git
git/                                          git_C2AD7E6A05C00E7026946A87AB501ADA (1).zip  git_C2AD7E6A05C00E7026946A87AB501ADA.zip
git 2/                                        git_C2AD7E6A05C00E7026946A87AB501ADA (2).zip  
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git
git/                                          git_C2AD7E6A05C00E7026946A87AB501ADA (1).zip  git_C2AD7E6A05C00E7026946A87AB501ADA.zip
git 2/                                        git_C2AD7E6A05C00E7026946A87AB501ADA (2).zip  
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git\ 2/
.git/           HelloWorld.txt  
Srinivass-MacBook-Pro:NewDownload10Oct darkknight$ cd git\ 2/
Srinivass-MacBook-Pro:git 2 darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git 2 darkknight$ git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
Srinivass-MacBook-Pro:git 2 darkknight$ ls
HelloWorld.txt
Srinivass-MacBook-Pro:git 2 darkknight$ git log --diff-filter=D --summary
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout $commit~1 flag.txt
error: pathspec '~1' did not match any file(s) known to git.
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git 2 darkknight$ git branch
  develop
* master
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout rctf
error: pathspec 'rctf' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout -b rctf
Switched to a new branch 'rctf'
Srinivass-MacBook-Pro:git 2 darkknight$ git log --diff-filter=D --summary
Srinivass-MacBook-Pro:git 2 darkknight$ git checkout $commit~1 flag.txt
error: pathspec '~1' did not match any file(s) known to git.
error: pathspec 'flag.txt' did not match any file(s) known to git.
Srinivass-MacBook-Pro:git 2 darkknight$ git log
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git 2 darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git 2 darkknight$ cat .git/
COMMIT_EDITMSG  ORIG_HEAD       config          hooks/          info/           objects/        
HEAD            branches/       description     index           logs/           refs/           
Srinivass-MacBook-Pro:git 2 darkknight$ cat .git/logs/
HEAD  refs/ 
Srinivass-MacBook-Pro:git 2 darkknight$ cat .git/logs/HEAD
0000000000000000000000000000000000000000 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187274 +0800	commit (initial): Initial Commit
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187289 +0800	checkout: moving from master to rctf
22d3349a5c6fe45758daba276108137382a01caa f4d0f6ddf6660f5c9273c84f3de64840a407bef1 zsx <zsx@zsxsoft.com> 1526187319 +0800	commit: Flag
f4d0f6ddf6660f5c9273c84f3de64840a407bef1 f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187331 +0800	commit: Revert
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187346 +0800	checkout: moving from rctf to master
22d3349a5c6fe45758daba276108137382a01caa f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187455 +0800	checkout: moving from master to develop
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187488 +0800	checkout: moving from develop to master
22d3349a5c6fe45758daba276108137382a01caa f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 zsx <zsx@zsxsoft.com> 1526187817 +0800	checkout: moving from master to develop
f671986f9aaa4fc49d8f3eba916d7947dc9f7e46 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187876 +0800	rebase -i (start): checkout 22d3349
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187876 +0800	rebase -i (finish): returning to refs/heads/develop
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa zsx <zsx@zsxsoft.com> 1526187889 +0800	checkout: moving from develop to master
22d3349a5c6fe45758daba276108137382a01caa 22d3349a5c6fe45758daba276108137382a01caa Srinivas <spg349@nyu.edu> 1526830942 -0400	checkout: moving from master to rctf
Srinivass-MacBook-Pro:git 2 darkknight$ git log -n 1 HEAD
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git 2 darkknight$ git log HEAD
commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
Author: zsx <zsx@zsxsoft.com>
Date:   Sun May 13 12:54:34 2018 +0800

    Initial Commit
Srinivass-MacBook-Pro:git 2 darkknight$ git log --all --graph
* commit 22d3349a5c6fe45758daba276108137382a01caa (HEAD -> rctf, master, develop)
  Author: zsx <zsx@zsxsoft.com>
  Date:   Sun May 13 12:54:34 2018 +0800
  
      Initial Commit





# Commands:
 1766  ls
 1767  cd git\ 3/
 1768  ls
 1769  ls -ltr
 1770  cd .git/COMMIT_EDITMSG 
 1771  cat .git/COMMIT_EDITMSG 
 1772  git pull
 1773  git 
 1774  vi .git/logs/HEAD
 1775  vi .git/logs/refs/heads/develop 
 1776  vi .git/logs/refs/heads/master 
 1777  vi .git/description 
 1778  vi .git/config 
 1779  vi .git/branches/
 1780  vi .git/ORIG_HEAD 
 1781  vi .git/ORIG_HEAD HelloWorld.txt 
 1782  vi .git/objects/02/cf5771b4db91f6e4949b428e32374ec6715085 
 1783  vi .git/COMMIT_EDITMSG 
 1784  git status
 1785  cd ..
 1786  ls
 1787  cd git
 1788  ls
 1789  git status
 1790  git branch
 1791  git checkout develop
 1792  git status
 1793  ls
 1794  git fetch
 1795  git pull
 1796  git status
 1797  git log
 1798  git status
 1799  git 
 1800  git branch
 1801  git show
 1802  git diff --git a/HelloWorld.txt b/HelloWorld.txt
 1803   diff --git a/HelloWorld.txt b/HelloWorld.txt
 1804  diff --git a/HelloWorld.txt b/HelloWorld.txt
 1805  git show
 1806  git log
 1807  git checkout master
 1808  git status
 1809  git lg
 1810  git log
 1811  git 
 1812  git diff
 1813  git status
 1814  git show
 1815  git bisect
 1816  cat .git/COMMIT_EDITMSG 
 1817  git revert
 1818  git revert --continue
 1819  git revert --continue 
 1820  git revert -m
 1821  cat .git/branches/
 1822  cat .git/index
 1823  cat .git/info/exclude 
 1824  cat .git/refs/heads/develop 
 1825  cat .git/ORIG_HEAD 
 1826  cat .git/description 
 1827  cat .git/hooks/prepare-commit-msg.sample 
 1828  ls
 1829  cat HelloWorld.txt 
 1830  git status
 1831  ls
 1832  cd ..
 1833  pwd
 1834  cd git
 1835  ls
 1836  ls
 1837  ls
 1838  cat .git/info/exclude 
 1839  cat .git/index 
 1840  cat .git/description 
 1841  cat .git/COMMIT_EDITMSG 
 1842  git commit --amend
 1843  ls
 1844  cat HelloWorld.txt 
 1845  cat HelloWorld.txt 
 1846  vi HelloWorld.txt 
 1847  ls
 1848  cat .git/COMMIT_EDITMSG 
 1849  q
 1850  git log
 1851  cd ..
 1852  cd git\ 3/
 1853  ls
 1854  git status
 1855  cat .git/COMMIT_EDITMSG 
 1856  git log
 1857  git revert 22d3349a5c6fe45758daba276108137382a01caa
 1858  ls
 1859  git status
 1860  ls
 1861  cat .git/config .git/
 1862  cat .git/index 
 1863  ls
 1864  cd ..
 1865  cd git\ 2/
 1866  git rev-list -n 1 HEAD -- <file_path>
 1867  git rev-list -n 1 HEAD
 1868  ls
 1869  git checkout <deleting_commit>^ 
 1870  git checkout <deleting_commit>^
 1871  git checkout 
 1872  ls
 1873  git checkout 22d3349a5c6fe45758daba276108137382a01caa
 1874  ls
 1875  ks
 1876  ;s
 1877  ls
 1878  cat HelloWorld.txt 
 1879  ls
 1880  cd ../git\ 4/
 1881  ls
 1882  git checkout $commit~1 flag.txt
 1883  cat .git/COMMIT_EDITMSG 
 1884  git checkout $commit~1 "flag.txt"
 1885  git commit --amend
 1886  git checkout $commit~1 "flag.txt"
 1887  git checkout $commit~1 "flag.txt"
 1888  cd ..
 1889  cd git\ 5/
 1890  ls
 1891  git checkout HEAD -- flag.txt
 1892  ls
 1893  cat .git/COMMIT_EDITMSG 
 1894  ;s
 1895  ls
 1896  cd ..
 1897  ls
 1898  cd git\ 5/
 1899  ls
 1900  cat .git/HEAD 
 1901  cat .git/HEAD 
 1902  cat .git/ORIG_HEAD 
 1903  cat .git/branches/
 1904  cd .git/branches/
 1905  ls
 1906  cd ..
 1907  cd ..
 1908  cd .git/description 
 1909  cat .git/description
 1910  cat .git/config
 1911  cat .git/index
 1912  cat .git/in
 1913  cat .git/info/
 1914  cat .git/info/exclude 
 1915  cat .git/objects/02/
 1916  cat .git/objects/02/cf5771b4db91f6e4949b428e32374ec6715085 
 1917  cat .git/objects/f4/d0f6ddf6660f5c9273c84f3de64840a407bef1 
 1918  cat .git/objects/info/
 1919  cat .git/objects/82/a7a337a2cdb9d2b58837b5a858be7ba3fa6779 
 1920  git bisect start
 1921  git bisect bad
 1922  git restore flag.txt
 1923  ls
 1924  git config alias.restore '!f() { git checkout $(git rev-list -n 1 HEAD -- $1)~1 -- $(git diff --name-status $(git rev-list -n 1 HEAD -- $1)~1 | grep '^D' | cut -f 2); }; f
 1925  git config alias.restore '!f() { git checkout $(git rev-list -n 1 HEAD -- $1)~1 -- $(git diff --name-status $(git rev-list -n 1 HEAD -- $1)~1 | grep '^D' | cut -f 2); }; f'
 1926  ls
 1927  cat HelloWorld.txt 
 1928  git log -- flag.txt
 1929  git log
 1930  git status
 1931  git bisect reset
 1932  git status
 1933  fir lof
 1934  fir log
 1935  git log
 1936  git checkout develop
 1937  git statu
 1938  git status
 1939  git log
 1940  git restore flag.txt
 1941  git log -- flag.txt
 1942  git config alias.restore '!f() { git checkout $(git rev-list -n 1 HEAD -- $1)~1 -- $(git diff --name-status $(git rev-list -n 1 HEAD -- $1)~1 | grep '^D' | cut -f 2); }; f'
 1943  ls
 1944  git checkout $commit~1 "flag.txt"
 1945  git log
 1946  git commit
 1947  git commit --amend
 1948  cat HelloWorld.txt 
 1949  ls
 1950  cd ..
 1951  git log
 1952  cd git\ 5/
 1953  git log
 1954  git log --flag.txt
 1955  git log -- flag.txt
 1956  cat .git/COMMIT_EDITMSG 
 1957  cd ..
 1958  rm -rf git
 1959  rm -rf git\ 2
 1960  rm -rf git\ 3
 1961  rm -rf git\ 4
 1962  rm -rf git\ 5/
 1963  cd git
 1964  ls
 1965  git log
 1966  cat .git/COMMIT_EDITMSG 
 1967  git checkout rctf
 1968  git bramcnch
 1969  git branch
 1970  git log
 1971  git checkout .
 1972  ls
 1973  git branch
 1974  git checkout -b rctf
 1975  ls
 1976  git status
 1977  git log
 1978  git checkout .
 1979  ls
 1980  git reset head
 1981  ls 
 1982  git reset head --hard
 1983  ls
 1984  cat HelloWorld.txt 
 1985  ls
 1986  cat HelloWorld.txt 
 1987  ls
 1988  pwd
 1989  ls -ltr
 1990  git checkout flag.txt
 1991  git checkout 
 1992  ls
 1993  git checkout HEAD^ flag.txt
 1994  ls
 1995  git reset HEAD .
 1996  ls
 1997  git checkout .
 1998  ;ls
 1999  ls
 2000  cat HelloWorld.txt 
 2001  ;s
 2002  git clean
 2003  ls 
 2004  git clean --force
 2005  ls
 2006  cat HelloWorld.txt 
 2007  git log
 2008  cat .git/COMMIT_EDITMSG `
 2009  cat .git/COMMIT_EDITMSG `
 2010  cat .git/COMMIT_EDITMSG 
 2011  git checkout ./*
 2012  ls
 2013  git checkout develop
 2014  git checkout ./*
 2015  ls
 2016  git log
 2017  git reset HEAD .
 2018  ls
 2019  git checkout .
 2020  ls
 2021  git checkout flag.txt
 2022  git reset -- flag.txt
 2023  git checkout -- flag.txt
 2024  ls
 2025  cat HelloWorld.txt 
 2026  ls
 2027  git checkout -- flag.txt
 2028  git checkout ./*
 2029  ls
 2030  git stash
 2031  ls
 2032  git ls-files -d | xargs git checkout --
 2033  ls
 2034  cd ..
 2035  cd gti
 2036  cd git
 2037  ls
 2038  git status
 2039  git checkout master
 2040  git ls-files -d | xargs git checkout --
 2041  ls
 2042  cat .git/COMMIT_EDITMSG 
 2043  git checkout rctf
 2044  ls
 2045  git ls-files -d | xargs git checkout --
 2046  ls
 2047  git log
 2048  git revert
 2049  git revert -n
 2050  git checkout ./*
 2051  ls
 2052  git checkout -- flag.txt
 2053  git reset -- flag.txt
 2054  git checkout -- flag.txt
 2055  ls
 2056  cat .git/COMMIT_EDITMSG 
 2057  cat .git/HEAD 
 2058  cat .git/refs/heads/rctf 
 2059  cat .git/refs/heads/master 
 2060  cat .git/refs/heads/develop 
 2061  cat .git/refs/tags/
 2062  cat .git/logs/HEAD 
 2063  git checkout -- <file>
 2064  cd ..
 2065  cd git
 2066  git checkout -- <file>
 2067  git checkout -- <file>
 2068  git ls-files --deleted
 2069  git ls-files --deleted
 2070  l
 2071  git status
 2072  git checkout -- flag.txt
 2073  git status
 2074  git ls-files --deleted
 2075  git rev-list -n 1 HEAD -- flag.txt
 2076  git checkout <commit>^ -- flag.txt
 2077  ls
 2078  git log --diff-filter=D --summary
 2079  git rever -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
 2080  git revert -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
 2081  ls
 2082  cat fl
 2083  cat flag.txt
 2084  git log
 2085  cd ..
 2086  git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
 2087  cd git
 2088  git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
 2089  ls
 2090  cd ..
 2091  cd git\ 2/
 2092  ls
 2093  git reset -- f4d0f6ddf6660f5c9273c84f3de64840a407bef1
 2094  ls
 2095  git log --diff-filter=D --summary
 2096  git checkout $commit~1 flag.txt
 2097  git branch
 2098  git checkout rctf
 2099  git checkout -b rctf
 2100  git log --diff-filter=D --summary
 2101  git checkout $commit~1 flag.txt
 2102  git log
 2103  cat .git/logs/HEAD
 2104  git log -n 1 HEAD
 2105  git log HEAD
 2106  git log --all --graph
 2107  git reflog
 2108  git checkout -b rctf f4d0f6d
 2109  git checkout -b rctf1 f4d0f6d
 2110  ls
 2111  cat flag.txt 
 2112  history
