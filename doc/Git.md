## git 开发流程

以下流程的原则：本地不能直接修改 master 分支，仅仅作为主干分支

注意`主干分支`与`开发分支`的区别

### 开新分支
```
$ git checkout master
$ git pull origin master
$ git checkout -b dev
```

### 更新本地分支
```
$ git checkout dev
$ git add .
$ git commit -m "更新dev分支"
```

### 合并分支（`本地主干分支`合并到`本地开发分支`）

#### merge 方式

合并分支
```
$ git checkout master
$ git pull origin master
$ git checkout dev
$ git merge master
```

解决冲突
```
$ git add .
$ git commit -m "合并dev分支"
```

#### rebase 方式

合并分支
```
$ git checkout master
$ git pull --rebase origin master
$ git checkout dev
$ git rebase master
```

解决冲突
```
$ git add .
$ git rebase --continue
```

注意：
使用`rebase`合并，修改冲突后的提交，`rebase --continue` 替代 `commit`

### 合并分支（`本地主干分支`合并到`远程主干分支`）
```
$ git checkout master
$ git fetch origin master
$ git rebase origin/master
```

### 演示流程

模拟 新开分支，解决冲突，合并分支

通过 graph 可以看出，主干分支不会出现交叉

```
➜  ~ cd code
➜  code git clone git@gitee.com:v__v/test.git test_rebase
Cloning into 'test_rebase'...
The authenticity of host 'gitee.com (120.55.226.24)' can't be established.
ECDSA key fingerprint is SHA256:FQGC9Kn/eye1W8icdBgrQp+KkGYoFgbVr17bmjey0Wc.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added 'gitee.com' (ECDSA) to the list of known hosts.
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
➜  code cd test_rebase
➜  test_rebase git:(master) git st
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working tree clean
➜  test_rebase git:(master) git br
* master
➜  test_rebase git:(master) git br -a
* master
  remotes/origin/HEAD -> origin/master
  remotes/origin/master
➜  test_rebase git:(master) git co -b dev
Switched to a new branch 'dev'
➜  test_rebase git:(dev) git br -a
* dev
  master
  remotes/origin/HEAD -> origin/master

  remotes/origin/master
➜  test_rebase git:(dev) ls
README.md
➜  test_rebase git:(dev) cat README.md
# test
git 测试%
➜  test_rebase git:(dev) echo "git 测试 dev" > README.md
➜  test_rebase git:(dev) ✗ git st
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  test_rebase git:(dev) ✗ git add .
➜  test_rebase git:(dev) ✗ git ci -m 'dev更新README'
[dev 087e069] dev更新README
 1 file changed, 1 insertion(+), 2 deletions(-)
➜  test_rebase git:(dev) git st
On branch dev
nothing to commit, working tree clean
➜  test_rebase git:(dev) git co master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
➜  test_rebase git:(master) ls
README.md
➜  test_rebase git:(master) cat README.md
# test
git 测试% 
➜  test_rebase git:(master) echo "git 测试 master" > README.md
➜  test_rebase git:(master) ✗ git add .
➜  test_rebase git:(master) ✗ git ci -m 'master更新README'
[master 030d108] master更新README
 1 file changed, 1 insertion(+), 2 deletions(-)
➜  test_rebase git:(master) git co dev
Switched to branch 'dev'
➜  test_rebase git:(dev) git log --graph | cat
* commit 6b2b6c49f0b56a6dd600dfa7d0e77e8088d4a7ff
| Author: Zhang He <zhang_he06@163.com>
| Date:   Wed Oct 11 18:20:38 2017 +0800
|
|     dev更新README
|
* commit 074cfc25cbfea99e486b57c3fdd8b2cddcd384d8
  Author: 空ping子 <zhendime@gmail.com>
  Date:   Wed Oct 11 18:15:28 2017 +0800

      Initial commit
➜  test_rebase git:(dev) git rebase master
First, rewinding head to replay your work on top of it...
Applying: dev更新README
Using index info to reconstruct a base tree...
M	README.md
Falling back to patching base and 3-way merge...
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: Failed to merge in the changes.
Patch failed at 0001 dev更新README
The copy of the patch that failed is found in: .git/rebase-apply/patch

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".

➜  test_rebase git:(030d108) ✗ git st
rebase in progress; onto 030d108
You are currently rebasing branch 'dev' on '030d108'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git reset HEAD <file>..." to unstage)
  (use "git add <file>..." to mark resolution)

	both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  test_rebase git:(030d108) ✗ cat README.md
<<<<<<< HEAD
git 测试 master
=======
git 测试 dev
>>>>>>> dev更新README
➜  test_rebase git:(030d108) ✗ echo "git 测试 dev merge" > README.md
➜  test_rebase git:(030d108) ✗ git st
rebase in progress; onto 030d108
You are currently rebasing branch 'dev' on '030d108'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:

  (use "git reset HEAD <file>..." to unstage)
  (use "git add <file>..." to mark resolution)

	both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  test_rebase git:(030d108) ✗ git add .
➜  test_rebase git:(030d108) ✗ git st
rebase in progress; onto 030d108
You are currently rebasing branch 'dev' on '030d108'.
  (all conflicts fixed: run "git rebase --continue")

Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	modified:   README.md

➜  test_rebase git:(030d108) ✗ git rebase --continue
Applying: dev更新README
➜  test_rebase git:(dev) git st
On branch dev
nothing to commit, working tree clean
➜  test_rebase git:(dev) git log --graph | cat
* commit 6b2b6c49f0b56a6dd600dfa7d0e77e8088d4a7ff
| Author: Zhang He <zhang_he06@163.com>
| Date:   Wed Oct 11 18:20:38 2017 +0800
|
|     dev更新README
|
* commit 030d10849d1ab4163f75fdcdf030ba3aded52404
| Author: Zhang He <zhang_he06@163.com>
| Date:   Wed Oct 11 18:21:33 2017 +0800
|
|     master更新README
|
* commit 074cfc25cbfea99e486b57c3fdd8b2cddcd384d8
  Author: 空ping子 <zhendime@gmail.com>
  Date:   Wed Oct 11 18:15:28 2017 +0800

      Initial commit
➜  test_rebase git:(dev) git diff master | cat
diff --git a/README.md b/README.md
index 297160d..6fbe460 100644
--- a/README.md
+++ b/README.md
@@ -1 +1 @@
-git 测试 master
+git 测试 dev merge
➜  test_rebase git:(dev) git co master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
➜  test_rebase git:(master) git merge dev
Updating 030d108..6b2b6c4
Fast-forward
 README.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
➜  test_rebase git:(master) git log --graph | cat
* commit 6b2b6c49f0b56a6dd600dfa7d0e77e8088d4a7ff
| Author: Zhang He <zhang_he06@163.com>
| Date:   Wed Oct 11 18:20:38 2017 +0800
|
|     dev更新README
|
* commit 030d10849d1ab4163f75fdcdf030ba3aded52404
| Author: Zhang He <zhang_he06@163.com>
| Date:   Wed Oct 11 18:21:33 2017 +0800
|
|     master更新README
|
* commit 074cfc25cbfea99e486b57c3fdd8b2cddcd384d8
  Author: 空ping子 <zhendime@gmail.com>
  Date:   Wed Oct 11 18:15:28 2017 +0800

      Initial commit
```


对比一下简单粗暴的 merge 方式

产生了一个无意义的 Merge

```
➜  code git clone git@gitee.com:v__v/test.git test_merge
Cloning into 'test_merge'...
remote: Counting objects: 3, done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
➜  code cd test_merge
➜  test_merge git:(master) ls
README.md
➜  test_merge git:(master) git co -b dev
Switched to a new branch 'dev'
➜  test_merge git:(dev) cat README.md
# test
git 测试%                                                                                                                                                                         ➜  test_merge git:(dev) echo "git 测试 dev" > README.md
➜  test_merge git:(dev) ✗ git add .
➜  test_merge git:(dev) ✗ git ci -m 'dev更新README'
[dev 6c85b19] dev更新README
 1 file changed, 1 insertion(+), 2 deletions(-)
➜  test_merge git:(dev) git co master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
➜  test_merge git:(master) echo "git 测试 master" > README.md
➜  test_merge git:(master) ✗ git add .
➜  test_merge git:(master) ✗ git ci -m 'master更新README'
[master 44aa754] master更新README
 1 file changed, 1 insertion(+), 2 deletions(-)
➜  test_merge git:(master) git co dev
Switched to branch 'dev'
➜  test_merge git:(dev) git merge master
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.
➜  test_merge git:(dev) ✗ git st
On branch dev
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  test_merge git:(dev) ✗ echo "git 测试 dev merge" > README.md
➜  test_merge git:(dev) ✗ git st
On branch dev
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
➜  test_merge git:(dev) ✗ git add .
➜  test_merge git:(dev) ✗ git st
On branch dev
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:

	modified:   README.md

➜  test_merge git:(dev) ✗ git ci -m 'dev Merge README'
[dev 0e8fa0e] dev Merge README
➜  test_merge git:(dev) git st
On branch dev
nothing to commit, working tree clean
➜  test_merge git:(dev) git log --graph | cat
*   commit 0e8fa0ed7ce77827cec82bdda1fcca42c3a22330
|\  Merge: 6c85b19 44aa754
| | Author: Zhang He <zhang_he06@163.com>
| | Date:   Wed Oct 11 19:14:44 2017 +0800
| |
| |     dev Merge README
| |
| * commit 44aa75419691f7496d4e2d6c37c0eb6098078ed2
| | Author: Zhang He <zhang_he06@163.com>
| | Date:   Wed Oct 11 19:12:54 2017 +0800
| |
| |     master更新README
| |
* | commit 6c85b190593fb39e6fc3490675983f04dfb10d89
|/  Author: Zhang He <zhang_he06@163.com>
|   Date:   Wed Oct 11 19:12:12 2017 +0800
|
|       dev更新README
|
* commit 074cfc25cbfea99e486b57c3fdd8b2cddcd384d8
  Author: 空ping子 <zhendime@gmail.com>
  Date:   Wed Oct 11 18:15:28 2017 +0800

      Initial commit
```
