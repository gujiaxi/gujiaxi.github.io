---
layout: post
title: "File Transfer between Galaxy Nexus and Arch Linux"
date: 2012-08-26 17:21
---

*Update on: 5 Aug, 2015*

再回头看一下[wiki](https://wiki.archlinux.org/index.php/MTP)，现在MTP跟PTP都可以很好地支持了。

```shell
pacman -S libmtp gvfs-mtp
pacman -S gphoto2 gvfs-gphoto2
```

-----

Jelly Bean的文件传输协议貌似比较奇特（支持的USB连接数据传输可选的有**MTP**跟**PTP**两种，而不是传统的**USB mass storage**），所以导致的问题呢，在ArchLinux下插上USB没有反应，当然如果允许的话可以使用[Airdroid](http://airdroid.com/)这样的app来进行数据传输，不过那样要依赖网络了。

看了下[Archlinux论坛](https://bbs.archlinux.org/)，好像讨论这个问题的人还是蛮多的，解决方案也有不少，不过大致就是围绕[MTP](https://wiki.archlinux.org/index.php/MTP)这个协议来发散，我也没有一一试验，还有一种方案是[jmtpfs](http://research.jacquette.com/jmtpfs-exchanging-files-between-android-devices-and-linux/)，不过据说速度很不理想（在终端下面操作好像要快不少，可能和Nautilus也有关）。

不过说实话我的需求并不高，手机连接电脑也就是传几张图片而已，所以我的解决方案也比较简单，直接安装`gvfs-gphoto2`这个包，然后在手机上设置USB连接模式为**PTP**，然后插上USB到电脑就行了。当然这样做只能够传输图片，不过对于我足矣。
