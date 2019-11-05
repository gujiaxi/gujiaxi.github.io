---
layout: post
title: "Git的基本用法"
date: 2014-11-18
---

![](/assets/img/20141118-1.jpg)

关于Git的用法网上各种手册、各种教程……多如牛毛，我就不废话了，这里主要是写一下我自己觉得容易忽略但是确实很好用的一些技巧。

## master跟origin的含义
master一般不会搞错，就是默认的一个分支名字；而origin是默认的远程仓库名称，可以用`git remote -v`查看。

## fetch与pull的区别
两者主要的区别是fetch只是取回相应分支的代码，而pull是在fetch的基础上还有一个merge的动作，即取回代码并与当前工作分支合并。保险起见我一般都用fetch。

```shell
git fetch <远程主机名> <远程分支名>
git pull <远程主机名> <远程分支名>:<本地分支名>
```

## push到底push了些什么
push一般都会省略一些东西，所以之前我也是迷迷糊糊。还有，分支推送顺序的写法总是<来源地>:<目的地>，所以git pull是<远程分支>:<本地分支>，而git push是<本地分支>:<远程分支>。

```shell
git push <远程主机名> <本地分支名>:<远程分支名>
git push origin master
git push origin master:master # 等价于上一条
```

## 获取分支

```shell
git branch <分支名> # 创建本地分支
git clone <远程主机地址> -b <远程分支名>
git fetch origin :<分支名> # 从远程主机获取分支，如果本地不存在该分支则创建一个新分支
```

## 删除分支
分支分为本地分支和远程分支。

```shell
git branch -d <本地分支名> # 如果该分支没有被merge则会失败
git branch -D <本地分支名> # 强制删除
git push origin :master # 通过推送空分支来删除远程分支
git push origin --delete master # 等价于上一条
```

## 重命名分支

```shell
git branch -m <本地旧分支名> <本地新分支名>
# 删除远程分支名如下
git fetch origin :oldname
git branch -m oldname newname
git push origin :oldname
git push origin newname
```

-----

- [Git Reference](http://gitref.org)
- [Git Cheatsheet](http://ndpsoftware.com/git-cheatsheet.html)
- [Git Documentation](http://git-scm.com/doc)
- [Getting Git Right](http://www.atlassian.com/git/)
