---
layout: post
title: "計算機網路(10)"
date: 2012-12-12 13:47
---
本周的課程主要圍繞 Routing Algorithm 展開，相關的內容可以在[這裡](http://210.43.128.116/jsjwl/net/kurose/network/algor/algor.htm)看到。

## 習題
* **在 link state routing algorithm 常出現 oscillation problem ， 請說明所謂 oscillation problem 並提出一種解決方法。**

	link state routing algorithm 通過主動測試鄰接節點的狀態，定期地將相鄰節點的狀態信息傳送給所有節點，每個節點都有完整的網絡拓撲信息，然後計算到每個節點的最佳路徑。而 oscillation problem 是因為存在多個交通指揮中心而造成的問題，解決方案是盡可能地善用雙層式網路架構，並且切割成多個 Area ，這樣每個 Area 中的網路就會比較簡單，同一個 Area 中的 Link-State 路由演算法計算次數也會比較少，而且 Routing Table 和各種資料庫中的資料筆數也會比較少，但前提是這樣的網路設計會有很多很多限制，例如切割好的各個Area網路必須是連續性的，而且每個 Area 中的每一台路由器設備必須永遠都能接收並且發送 LSA 網路封包到同一個 Area 中的其他路由器設備。

* **在 distance vector routing algorithm 常出現 bad news travel slow problem ，請說明所謂 bad news travel slow problem 並提出一種解決方法。**

	Distance Vector路由演算法與Link State路由演算法最大的不同就是，Link State演算法只會傳遞少部分更新的路由資料，而且會把這樣的更新資料傳遞到各個路由器設備內，而Distance Vector路由演算法則會傳遞整份的資料，而且只會傳遞給鄰近的路由器設備而已。不過，即使路由資料沒有任何的改變，Distance Vector也會將整份路由資料發送出來，而這裡所謂的整份路由資料，指的就是發送端路由器設備中Routing Table的完整資料，當鄰近的路由器設備收到這整份路由資料後，會開始比較已知的路由路徑，並把有更新過的資料同步至本地端路由器設備中，因為這種方式都會假設接收到的資料一定是比自己還要新的資料，所以這種方式通常也被稱為「謠言路由方式」（Routing by rumor）。就是因為這樣類似「以訛傳訛」的運作方式，所以會產生很多問題。

	為此，出現了採用Distance Vector路由演算法和Link-State路由演算法的混合式路由協定。而Cisco專屬的EIGRP路由協定正是使用這種混合式的作法。

	大致而言，這種混合式的路由協定會採用Distance Vector路由演算法，將之套用在比較精確的資料上，以便於決定網路上的最佳路徑。何謂比較精確的資料？因為這種混合式的路由協定雖然在這方面是採用Distance Vector路由演算法的方式，但卻和一般的Distance Vector路由演算法不同，這種混合式的路由協定並不會定期發送網路的狀態與資訊的更新。

	這裡所採用的方式是當網路發生變化時，馬上發送相關的網路資訊給每個路由器，去觸發這種路由更新的動作，在這方面算是學習到Link-State路由演算法的優點，去除了Distance Vector路由演算法的缺點。
