---
layout: post
title: "Cygwin配置"
date: 2014-12-02
---

最近用公家的电脑，实在受不了Windows的那个console。于是装上了[Cygwin](https://www.cygwin.com/)，还有一个叫[Babun](http://babun.github.io/)的，没有用过，不知道怎么样。

首先是包管理，用的是[apt-cyg](https://github.com/transcode-open/apt-cyg)，很好用。

| Command | Description | Analog |
|:------------|:---------------|:-----|
| install | Install packages | apt-get install |
| remove | Remove packages | apt-get remove |
| update | Update setup.ini | apt-get update |
| show | Displays the package records for the named packages | apt-cache show |
| list | List packages matching given pattern. If no pattern is given, list all installed packages. | dpkg --list |
| search | Search for a filename from installed packages | dpkg --search |
| download | Download only - do NOT install or unpack archives | apt-get install --download-only |

然后就是可以用：

```sh
apt-cyg install vim
apt-cyg install git
```

安装上必要的工具了。

最后感觉默认的主题太丑了，于是找到了[mintty-colors-solarized](https://github.com/mavnn/mintty-colors-solarized)，之后配置vim就得心应手了~