---
layout: post
title: "計算機網路(11)"
date: 2012-12-17 21:33
---
這周的課主要涉及：fragmentation, Inter-AS, Subnet, DHCP, NAT

在每一個AS中執行相同的路徑演算法(LS/DV)叫做Intra-AS，而AS彼此間所執行的Routing Algorithm為Inter-AS。

運用AS1的Intra-AS routing algorithm可以決定A1至A2或A3的路徑，並建立其Intra-AS的forwarding table，但A1至AS2或AS3中的任一節點要如何決定所奏的路徑呢：① Learning(學習): 每個節點記錄外部AS的訊息，例如B1記錄到從AS1要送到AS3中C2的segment經過B1; ② broadcasting(分享): 將記錄的外部訊息廣播發送給同一AS的所有節點; ③ building(建立): 當節點收到各種外部訊息後，便可建立自己的Inter-AS的forwarding table

Host C有segment要傳送至Host B，在C3的外部forwarding table中有二條路徑（一個經由C1,一個經由C2）皆可選擇，那究竟選哪一條？這種情況下由AS3的Intra-AS來決定，稱為Host Potato Routing Algorithm。

我們稱有相同的net id的host在同一個subnet。

要上網的電腦如何取得一個IP address: ① fixed(固定IP) ② dynamic(動態IP) 或 floating(浮動)

[DHCP](http://en.wikipedia.org/wiki/Dhcp)(Dynamic Host Configuration Protocol)取得一個動態IP address

[NAT](http://en.wikipedia.org/wiki/Network_address_translation)(Network address translation)有以下優點: ① 增加IP使用空間運用不同的port number; ② LAN改變，WAN不變; ③ WAN改變，LAN不變; ④ WAN不知LAN的情形(security)
