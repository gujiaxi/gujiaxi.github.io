---
layout: post
title: "Export Your Google Chat Logs"
date: 2013-03-22 21:12
---
近期Reader被Google无情杀害在网络上引起了不小的轰动，没想到一向名声不错的Google也有今天，大家对Google的服务一下子就没有了信心，鬼知道它啥时候又要来个什么**大扫除**。所以还是尽快把该备份的都给备份了吧，比如说Google Talk的聊天记录。

## 通过javascript来导出与指定好友的聊天记录
详细代码在[这里](https://github.com/IntuitiveUser/user-rule/tree/master/sites/gmail/exporters)，把它保存成书签，然后登录网页版Gmail，载入之后点一下书签然后会弹出提示输入好友名字，之后就会自动开始抓取了，最后完成之后把网页保存到本地即可。不过如果聊天记录太多的话可能时间会比较长甚至浏览器会崩溃。

## 基于Python来导出
直接给出[这里](https://github.com/gujiaxi/ChatDownloader)的代码吧，主要是分为两步，第一步是通过`download.py`把聊天记录逐条下载为单个的*txt*文件到本地，然后`convert.py`是对下载下来的*txt*们进行处理，可以合并导出到一整个*html*文件或者逐个转换。代码应该还算挺清楚的，如果要是需要对单独某个好友的聊天记录进行处理，其实有很多办法可以实现（比如说利用grep工具来筛选或者python的相关模块），当然输出的*html*格式也是可以是别的样子。
