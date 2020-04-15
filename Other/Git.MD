download:https://git-scm.com/  

git bash  
* $ git --version  

# command  
* git help  
* git help commit  
* git help + name  
* clear (clear all)

# config account  
* $ git config --global user.name "xxxx"  
* $ git config --global user.email "xxx@gmail.com"  
   config account   
* $ git config --list    
* $ git config --user.email  
* check git info. 

# creat a Repository  
* $ cd ~  
return home path  
*   $ pwd   
check the currently path 
*   $ cd ..  
back path  
* $ cd desktop   
forward path    
* $ cd ls  
check all info under current path  
* $ git init  
Initialized project  
Initialized empty Git repository in C:/Users/yzw/Desktop/git/.git/  


# commit
* $ ls  
check all document under current path   
* $ ls -la    
check all hide document under current path  
* $ git add .    
* $ git add 1.txt  
Add file contents to the index   
* $ git commit -m 'This is our first commit'   
Record changes to the repository   
[master dc35f8b] This is our first commit  
 1 file changed, 1 insertion(+)  
* $ git log  
$ git log --author='yangzongwu'  
check commit history  
* $ git status  
Show the working tree status  


# edit/update
working copy > staging area > repository  
not do any command in git-- working copy  
after $ git add .  ---staging area  
after git commit   ---repository  

* $ git-diff  
Show changes between commits, commit and working tree, etc  
* $ git diff --staged  
Show staged changes between commits, commit and working tree, etc  


# delete   
* $ git rm 2.txt   
* $ git commit -m'this is delete 2.txt'  
[master b602845] this is delete 2.txt  
 1 file changed, 0 insertions(+), 0 deletions(-)  
 delete mode 100644 2.txt  

# rename  
when wen change name, the git will wrong info.rename first to indext    
### first   
* $ git status  
On branch master  
Changes not staged for commit:   
        deleted:    first.txt  
Untracked files:  
        index.txt   
no changes added to commit (use "git add" and/or "git commit -a")  
<br />
* $ git add index.txt  
* $ git rm.first.txt  
* $ git status  
On branch master  
Changes to be committed:  
        renamed:    first.txt -> index.txt  

### second  
* $ git mv home.txt pudding.txt 

# move
* $ git mv paty.txt p/paty.txt  

# reset from stage area to working copy
* $ git reset HEAD pudding.txt  

# old version  
eg:first>second>third>second  
* $ git log  
commit 3d4b2e9864c915a234d0400d4955e71e752b13f9  
Author: yangzongwu <yangzong5@gmail.com>  
Date:   Mon Mar 11 22:27:57 2019 -0700  
    third  
commit 71dfbeb16ebc0f9c6ba37f869540dd17aced3aa3  
Author: yangzongwu <yangzong5@gmail.com>  
Date:   Mon Mar 11 22:27:15 2019 -0700  
    second  
* $  git checkout  71dfbeb16 -- test.txt  
* $ git commit -m'backto2'  
checkout+commit(only a few first letter is OK)
