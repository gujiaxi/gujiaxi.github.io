---
layout: post
title:  "OS X下的锐捷认证"
date:   2012-02-18 00:24:58
---

写在前面：大陆的很多学校都是使用的锐捷认证，不过各个高校的认证因为种种原因都会有所不同，我只是就我们学校的认证来说的，系统是OS X Lion。另外，至于锐捷官方提供的客户端，只有Windows版本是值得推荐的。

首先说一下用于锐捷认证的MentoHUST，项目主页在[这儿](http://code.google.com/p/mentohust/)。

> 官方的锐捷Linux版久无更新，使用官方程序很多同学无法通过认证，有些能通过但容易掉线。虽然网上第三方Linux版锐捷客户端不少，但都大同小异，不能通过锐捷的客户端校验。本项目旨在提供一个Linux下与锐捷兼容性很好的认证客户端，方便使用Linux和锐捷的同学使用校园网。

主要功能：

* 支持锐捷客户端校验算法
* 支持多网卡 
* 较好模拟锐捷各版本数据，支持锐捷所有版本 
* 支持静态IP和DHCP（动态IP）认证 
* 支持静态IP用户自定义IP（即绑定IP可与上网IP不同） 
* 支持服务器消息提示和计费信息提示 
* 认证成功稳定在线，即使掉线也可自动重连 
* 有相关工具支持，可自定义数据文件以实现尽可能的兼容，无需修改代码即可兼容所有版本 
* 支持赛尔认证

首先到项目主页去下载个`mentohust_mac.tar.gz`，至于还有一个描述为*Mac OS下带图形界面的mentohust*的`CocoaMento.dmg`，我不知道到底是怎么回事，下载下来是个Microsoft Word。不管它。解压出来有几个文件，把其中的`dhcping`和`mentohust`这两个文件拷贝到`/usr/bin`目录下，可以在终端下`cp`，也可以直接复制粘贴过去。然后打开终端：
	sudo mentohust
根据提示输入相关信息就可以了，配置信息将会被保存到`/etc/mentohust.conf`中，随时可以查看并修改。

最后……顺手写了个脚本：

```sh
#!/bin/bash
echo "Tell me what you wanna do: Connect - Input c || Disconnect - Input d"
read
if [ $REPLY = "c" ]
then sudo mentohust -b1<<EOF
	Input your password
EOF
elif [ $REPLY = "d" ]
then sudo mentohust -k<<EOF
	Input your password
EOF
else echo "Are you kidding me!!!"
fi
```
