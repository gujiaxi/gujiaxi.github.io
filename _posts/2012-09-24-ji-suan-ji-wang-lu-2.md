---
layout: post
title: "計算機網路(2)"
date: 2012-09-24 18:25
---
> How long does it take to send a file of 640,000 bits from host A to host B over a circuit-switched network? All links are 1.536 Mb/s and each link uses TDM with 24 slots/sec.

這是今天的第一個題目，正確的解答應該是這樣的：因為是 Circuit Switching ，所以可以計算得到每個 slot 被分配到的傳輸速率為 1.536Mbps / 24 = 64Kbps ，故而要傳送640Kb的數據需要 640Kb / 64Kbps = 10s。

> Suppose users share a 1Mbps link. Also suppose each user requires 100Kbps when transmitting, but each user transmits only 10 percent of the time.
> a) Suppose there are 40 users. Find the probability that at any given time, exactly n users are transmitting simultaneously.
> b) Find the probability that there are 10 or more users transmitting simultaneously. 

這是第二題，很顯然，每個主機傳送數據的概率是 0.1 ，這裡要注意的是傳輸資料的概率與主機的數量無關，而只與時間段的分割有關。所以接下來的 a 題就容易解答了： p(n) = C(40,n) \* 0.1^n \* (1 - 0.1)^(40-n) 。然後 b 題的答案很清楚了。

## ASCII 與 EBCDIC
* **[ASCII](http://en.wikipedia.org/wiki/ASCII)**: American Standard Code for Information Interchange, 它是基於拉丁字母的一套電腦編碼系統。主要用於顯示現代英語和其他西歐語言。它是現今最通用的單字節編碼系統，並等同於國際標準 ISO/IEC 646。

* **[EBCDIC](http://en.wikipedia.org/wiki/EBCDIC)**: Extended Binary Coded Decimal Interchange Code, 它是 IBM 公司推出的字符編碼表，根據早起打孔機式的二進化十進制數( BCD, Binary Coded Decimal )排列而成。它的缺点是：英文字母不是连续地排列，中间出现多次断续，为撰写程式的人带来了一些困难。

## Delay
關於這一節，可以參考[這篇文章](http://210.43.128.116/jsjwl/net/kurose/introduction/delay.htm)，我在這裡稍作整理以便學習。 Delay 主要可以分為四種： **nodal processing delay**, **queuing delay**, **transmission delay**, **propagation delay**。

* **nodal processing delay**: 路由器處理Header與找路徑等所花費的時間。

* **queuing delay**: 在路由器上因為某些因素無法立刻將傳送封包到網路上造成封包停留在buffer上所花費的時間。

* **transmission delay**: 網路卡將資料傳送(或接收)資料到網路線上所花的時間，與網路卡的傳送速度有關(如
高速乙太網路傳送速度為100Mbps)。假設頻寬為 **L** (bits)，數據傳輸速率為 **R** (bits/sec)，這樣產生的 transmission delay 就是 **L/R**。

* **propagation delay**: 在網路線上傳輸所花費的時間，與網路線上電子訊號跑的速度有關。主要由傳輸的物理介質決定，假設距離為 d ，傳輸的速率為 s (2\*10^8 meters/sec ~ 3\*10^8 meters/sec)，那麼 propagation delay 就是 d/s。

在網路上， nodal processing delay 、 transmission delay 與 propagation delay 都可根據相關參數(如封包大小、網路卡傳送速度等)計算所需時間，只有 queuing delay 必須根據網路當時情形才能獲知所需時間，因此 queuing delay 的變動性最大。描述 queuing delay 程度可以用 traffic intensity ，也就是 **La/R** *(L: the length of the packet, a(packets/sec): the average rate at which packets arrive to the queue, R(bits/sec): the transmission rate)*

![](/assets/img/20120924-1.jpg)

顯然，只有當 traffic intensity 小於1的時候才是順暢的，接近於1已經是擁擠了，而超過1太多的話……因為隊列不可能是無限的，所以必然會導致包的丟失。
