---
layout: post
title: "計算機網路(9)"
date: 2012-11-29 00:22
---
這周的課主要圍繞[Go-Back-N](http://en.wikipedia.org/wiki/Go-Back-N_ARQ)跟[Selective Repeat](http://en.wikipedia.org/wiki/Selective_Repeat_ARQ)來展開。

相關的內容在[這裡](http://www3.gdin.edu.cn/jpkc/dzxnw/jsjkj/chapter3/34.htm)可以找到。

## Go-Back-N
![Go-Back-N](/assets/img/20121129-1.gif)

## Selective Repeat
![Selective Repeat](/assets/img/20121129-2.gif)

## 習題
* **試解釋[ping](http://en.wikipedia.org/wiki/Ping_(networking_utility))**

	ping是：一个电脑网络工具，用来测试特定主机能否通过IP到达。ping的运作原理是：向目标主机传出一个ICMPecho要求分组，等待接收echo回应分组。程序会按时间和反应成功的次数，估计失去分组率（丢包率）和分组来回时间（网络时延）(Round-trip delay time)。

* **試解釋three-way handshake**

	TCP利用三路握手(three-way handshake)建立一个相对可靠的连接：
	1. 客户端发送一个SYN（客户端的序列号）报文给服务器
	2. 服务器收到SYN报文后，回应给客户端一个SYN和ACK都为1的报文，其中SYN为服务器自己的序列号，ACK是客户端的序列号的确认，为客户端序列号+1。
	3. 客户端收到服务器的SYN+ACK报文后，再发送给服务器一个只有ACK为1的报文，确认号就是服务器序列号+1，就完成了TCP连接建立。
