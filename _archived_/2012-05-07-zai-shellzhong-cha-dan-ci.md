---
layout: post
title: "在shell中查单词"
date: 2012-05-07 08:20
---
很简单，直接在`~/.bashrc`中添加下面的内容就行了：

```sh
function j() { dig $1.jianbing.org txt +short | perl -pe's/\\(\d{1,3})/chr $1/eg; s/"//g'; }
```

好了，现在打开终端可以直接查单词了，够方便够geek吧。

```sh
[isaac@halo ~]$ j arch
[ɑ:tʃ]
n.
拱门, 弓形结构, 拱形
v.
(使)弯成弓形
adj.
主要
```
