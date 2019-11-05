---
layout: post
title: "字符编码转换"
date: 2014-02-07 15:05
---
每次 Windows 下的文档拿到 Linux 下来看就是乱码，好在有个比较方便的工具——*iconv*可以解决问题。

```shell
file -bi filename # 查看文件编码
iconv -f fromcodeset -t tocodeset filename # 将文件从fromcodeset编码转换为tocodeset编码
```

更加详细的用法见[手册](http://www.gnu.org/savannah-checkouts/gnu/libiconv/documentation/libiconv-1.13/iconv.1.html)。
