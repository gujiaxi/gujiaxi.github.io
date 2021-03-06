---
layout: post
title: "可靠多播协议"
date: 2014-10-03
---
## 概述
通过ZeroMQ实现了基于EPGM的可靠多播协议。

## 架构
将一台服务器及多台客户端都绑定到同一个多播地址(如`234.5.6.7`)跟同一个端口(如`5555`)，基本的结构就是发布者(Publisher)跟订阅者们(Subscribers)的关系，由发布者向整个多播地址上的订阅者们进行可靠地多播。

## 图像发送
每次发送由三部分组成：图像相关信息、图像本身(*.jpg)、终止符（空字节）。

- 图像相关信息由一个结构体包装，其中包括一个标记位(**isSimilar**)，用来表示跟前一副图像相似。
- 对于jpg图像的发送，我考虑的是可能图像过大，所以将每一张图像分片了，每一片为256KB，依次发送。
- 结束符即为一个空字节。

## 测试
只进行了简单粗糙的测试，客户端将一张图片不断地对整个网络进行发送，各订阅者进行接收（并把每一次接收到的图片写入文件）。发现每次新客户端与服务器端建立连接会有一定程度的耗时，建立连接之后图片及其相关信息发送接收都完整，没有发现明显错误，接收的延迟不知道与读写硬盘还有机房的网络状态有没有关系。

## 整合
目前还不清楚服务器跟客户端各自的存储、发送、处理的细节。

-----

- [ZeroMQ](http://zeromq.org/)
- [OpenPGM](https://code.google.com/p/openpgm/)
- [Transferring Files](http://zguide.zeromq.org/page:all#Transferring-Files)
