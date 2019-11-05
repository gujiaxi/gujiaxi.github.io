---
layout: post
title:  "Arch Linux的安装"
date:   2012-03-26 23:18
---
> Keep It Simple, Stupid.

作为一名不安份的Ubuntu用户，前两天终于还是叛逃到了传说中的Arch阵营。写下这篇文章记录一下，也希望能对未来的Archer有所帮助。确实，可能Arch并不适合Linux新人，单从安装来看，也许大部分新手用户更愿意接受的是图形界面、点击鼠标、全自动配置……Arch不会并且永远不会（not and will not）满足这些要求，请不要误会它的简单（simple），更不要误会它的KISS（Keep it Simple, Stupid.）哲学，它所主张的纯粹、自由……这些都注定它不可能变成某些人想象的样子。好了，废话说得有点多，现在开始正题。

## 准备工作
* [下载](http://www.archlinux.org/download/)镜像刻盘（或者也可以用U盘，工具的话找一个合适的就行了）。
* 把该备份的都备份了，不怕一万就怕万一。
* 分区，或者有一块新的硬盘。
* 准备网络，如果你跟我们学校用的是锐捷认证，最好把[mentohust](http://code.google.com/p/mentohust/)的包也准备好，下载那个*.pkg.tar.gz放到U盘就行了。不过有IPV6的话可以省去不少的麻烦，因为Arch有IPV6的源。

## 开始安装
* 把光盘放入光驱（或者把U盘插上），设置BIOS从光驱（或者U盘）启动。
* 启动完毕之后应该有个选单，具体记不清了，让他引导Arch就行了，然后按照提示输入`/arch/setup`会启动安装。
* source就选CD-ROM好了。时区的话根据自己情况选，然后选local。
* 对硬盘进行分区的时候注意的是如果有其他系统在的话不要手贱了！大致可以分为/、/boot、/home、swap，挂载点的话就ext4吧，具体还是自己谷歌吧。
* 然后选择包，把base跟base-devel都勾上吧（按空格），安装完包之后开始进行必要配置。
* rc.conf里面东西比较多，时区、系统语言、键盘布局……现在都可以不管，HOSTNAME可以取一个名字，最主要的是配置一下网络，注释都很清楚，根据自己的情况改。然后MODULES()里面是开机需要加载的模块，DAEMONS()是开机自动加载的服务，前面加上`!`表示禁用，加上`@`表示后台运行，目前都不需要改动。
* 然后是`pacman.conf`，[pacman](https://wiki.archlinux.org/index.php/Pacman)是Arch的包管理工具，也可以以后再说。
* 然后是`mirrorlist`，这个是选择镜像源（在[这里](http://www.archlinux.org/mirrors/status/)可以看到各个镜像源的同步状态），把中国的源前面的注释去掉就行了（163的源速度很快的）。
* 有关于中文本地化的配置先不管，以后再说（其实我一直都没改，英文的挺好啊）。
* 设置Root密码，同样，密码是不会显示到屏幕上的，所以大胆的输吧。
* 安装grub（我没用lilo），直接回车就行了。
* 要跟Windows组成双系统的话还要注意一下`menu.lst`，把最后那几行的注释去掉就行了，大致就是下面这样：

  ```sh
  # (2) Windows
  title Windows
  rootnoverify (hd0,0)
  makeactive
  chainloader +1
  ```

* 等全部完成了之后输入`reboot`重启。

## 简单配置
好了，现在重新引导应该可以进入系统了，先`ping`一下，看看网络通不通，通的话运行两遍`pacman -Syu`，如果提示什么依赖问题的话可以加上`-f`参数来强制更新，虽然说不推荐这样做，但是我发现如果不强制的话后面会出现很奇怪的问题，我不知道这是我的个例还是……总之看着办吧，一般不会有问题的。

OK，搞定，Arch安装完毕，真的，真的就这么Simple。

写在最后：因为写这篇文章跟实际安装Arch已经隔了几天了（本来可以早点写下来的，无奈最近课比较多），很多配置不记得了，过程中参考了下[wiki](https://wiki.archlinux.org/index.php/Beginners%27_Guide)（当然更推荐要安装的童鞋直接看[wiki](https://wiki.archlinux.org/index.php/Beginners%27_Guide)），我只是大概写一下关键的地方，可能文章中“自己看着办”、“以后再说”……这些出现得有点多，如果有不清楚的话还请见谅，没办法，文笔不好，思路也比较乱，最近也没太多的时间整理，可能之后还会写点关于Arch配置的文章，敬请期待咯～

**Ps.** 今年正好是Arch Linux发行十周年，**Happy birthday, Arch!**
