---
layout: post
title: "計算機網路(8)"
date: 2012-11-05 20:17
---
今天的課程主要圍繞 transport/network, TCP/UDP, Multiplexing/Demultiplexing 展開。

## 如何區隔 transport 與 network 的功能與原理
基本上就是通信與傳輸的概念：

* transport 是 end-to-end ，而 network 是 point-to-point。 network layer 提供 service 給 transport layer 使用， transport layer 呼叫 network layer 執行其服務的功能。
* network layer 提供 host-to-host connection ， transport layer 提供 process-to-process connection。
* Addressing identifies of socket address: transort - port number, network - IP address

## 通訊的服務有哪些功能

* Data loss( Reliable )
* Timing( Delay )
* Throughput( Bandwidth )

**Data loss**: 對於通訊，錯誤主要有：遺失、污染、重複。解決的辦法是重送。可靠的傳輸： TCP ( 例如FTP )；不在乎的傳輸： UDP ( 例如SIP )。要求資料傳輸正確性的應用，就必須仰賴可靠的 transport 功能，例如：email, web, FTP... 另外無需可靠傳輸服務的例如：Youtube, Skype...

**Timing**：有些應用不在乎，例如：web, email, FTP... 但有些應用在乎，例如：online-game

**Throughput**：有些應用不在乎，例如：email, web, FTP... 但有些應用在乎，例如：real video...

由應用面或協定來看：

FTP, email, web document: ① reliable (no loss); ② 不在乎 timing; ③ 不在乎 throughput。 →→→→→ FTP/TCP， SMTP/TCP， HTTP/TCP

Internet telephone: ① unreliable (loss toralent); ②  time sensitive; ③ few Kbps up (throughput)。 →→→→→ SIP/UDP

## TCP vs. UDP
TCP特有的包括：① reliable ② connection setup ③flow control ④ congestion control

在 socket programming 中 identify process：TCP 有四個 tuple (source IP, source port number, destination IP, destination port number)， UDP 有兩個 tuple (destination IP, destination port number)

**flow control**：傳送端傳送資料的速率不可以超過接收端接收資料的速率。

**congestion conrol**：傳送端傳送資料的速率不可以超過網路所能笑話的資料量速率。

S<sub>t</sub> ≤ R<sub>t</sub>, R<sub>t</sub> ≤ N<sub>t</sub>, S<sub>t</sub> = f(R<sub>t</sub>, N<sub>t</sub>)

## Multiplexing / Demultiplexing
![Multipexing & Demultiplexing](/assets/img/20121105-1.png)

## 習題
* **解釋[RS-232](http://en.wikipedia.org/wiki/RS_232)通訊介面**

	RS-232是美國電子工業聯盟（EIA）制定的序列資料通訊的介面標準，原始編號全稱是EIA-RS-232（簡稱232，RS232）。它被廣泛用於電腦串列埠外設連線。

	RS-232C標準，其中EIA（Electronic Industry Association）代表美國電子工業聯盟RS（Recommended standard）代表推薦標準，232是標識號，C代表RS232的第三次修改（1969年），在這之前，還有RS232B、RS232A。

* **解釋[encapsulation](http://en.wikipedia.org/wiki/Encapsulation_(networking))**

	In computer networking, encapsulation is a method of designing modular communication protocols in which logically separate functions in the network are abstracted from their underlying structures by inclusion or information hiding within higher level objects.
