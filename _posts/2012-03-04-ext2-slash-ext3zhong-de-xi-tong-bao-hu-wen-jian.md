---
layout: post
title:  "Ext2/Ext3中的系统保护文件"
date:   2012-03-04 23:08
---
关于Linux下的文件操作很简单，权限的话用`chmod`很方便，不过我今天想说的是如何创建一些更安全的文件，就连root都无法进行操作。

首先创建一个普通的文件试试：

``` shell
touch file
```

查看一下文件属性先：

``` shell
lsattr file
```

可以看到输出：

```
-----------------e- file
```

好，现在使用`chattr`给文件加上一个特殊的标志：

``` shell
sudo chattr +i file
```

再查看一下文件属性，可以看到多了个`i`的标志：

```
----i------------e- file
```

现在来尝试对这个文件进行操作：

``` shell
sudo rm file
# rm: cannot remove `file': Operation not permitted
sudo mv file file1
# mv: cannot move `file' to `file1': Operation not permitted
sudo echo 'something' > file
# bash: file: Permission denied
sudo ln file file1
# ln: creating hard link `file1' => `file': Operation not permitted
```

可以看到，删除、重命名、写入甚至是设置硬连接都无法进行（就算是sudo也没用哦）。那要怎么样才能把这个“顽固的东西”赶走呢，只要把原来加的那个标志位去掉就可以了：

``` shell
sudo chattr -i file
```

原理：在ext2和ext3文件系统中，除了`chmod`可访问的标准属性位外，还有许多附加的文件属性。相关的内容可以查看`chattr`和`lsattr`的手册。文章中用到的是一个`i`属性，即系统保护标志。设置该标志后，会禁止对文件的删除、重命名、写入等操作，即使是root权限也没用。
