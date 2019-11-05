---
layout: post
title: "How to Install Sun Java JDK on Ubuntu"
date: 2012-03-01 09:05
---
这个学期开始学Java了，所以首先要做的就是给我的Ubuntu 11.04（Natty）配置Java的开发环境，不过Sun Java在Ubuntu 11.04的软件仓库里被移除了，所以不得不另想办法安装。

总结了几个方法：

## 通过PPA安装
添加PPA，更新安装即可：

```bash
sudo add-apt-repository ppa:ferramroberto/java
sudo apt-get update
sudo apt-get install sun-java6-jdk
```

## 通过Ubuntu 10.10（Maverick）的软件仓库安装
打开软件中心，添加maverick的软件源：

```bash
deb http://archive.canonical.com/ubuntu maverick partner
```

更新并安装JDK：

```bash
sudo apt-get update
sudo apt-get install sun-java6-jdk
```

## 在官网下载编译安装
在[这儿](http://www.oracle.com/technetwork/java/javase/downloads/jdk-7u3-download-1501626.html)下载对应的版本然后安装。
