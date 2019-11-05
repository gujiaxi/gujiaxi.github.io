---
layout: post
title: "計算機網路(13)"
date: 2013-01-07 21:28
---
這周的課主要圍繞Hub, Switch, Router展開，詳細的說明可以參考[Bridges and Switches](http://is.gd/Wwe6rY)

Hub(集線器): ① 運用star方式的集線器架構可以避免bus型的故障情況。 ② Hub具有信號加強放大的功能。

![Ethernets interconnected with a hub.](/assets/img/20130107-1.jpg)

Switch(交換器): ① 屬於第二層的網路元件(data link layer)。 ② 連接switch的每個segment皆相互獨立。

![An institutional network using a combination of hubs, Ethernet switches and a router.](/assets/img/20130107-2.jpg)

Swith工作原理(Self-Learning Algorithm)，比如說從H1到H3：

1. H1封包到達switch.
2. switch檢查其table是否有H1的連結資訊，若無則建立，同樣檢查H3的連結資訊，若無則broadcasting至所有連結.
3. H3收到封包，便回應封包至switch，其他H不回應.
4. 回應封包到達switch，同步驟②原理.
5. 回應封包目的地為H1，經由switch table中的資訊，該封包便直接送往界面(1).

switch的最大缺點為可能造成broadcasting風暴，而router不會。（可以通過Spanning Tree Protocol解決）

MAC: Media Access (Ethnet), 48-bit 如同身份證字號。

IP: 32-bit 如同郵政區號。

在LAN中傳輸資料是依賴ethnet address (即網路界面卡的硬體address)，其工作原理如下（還是舉H1到H3的例子）：

1. H1發出request"請問IP3的MAC是多少？"
2. 在LAN中只有H3會回應"IP3的MAC是xx.xx.xx.xx.xx.xx"
3. H1收到回應的IP3的MAC3
4. H1直接將封包送往MAC3 (即H3)

ARP (Address Resolution Protocol): IP ==> MAC

RARP (Reverse ARP): MAC ==> IP

## 習題
* **如何採用Spanning Tree Protocol來解決switch造成的broadcasting風暴問題**

	當網路中存在環路，就會造成每一幀都在網絡中重復廣播(broadcasting)，引起廣播風暴。要消除這種網絡循環連接帶來的網絡廣播風暴可以使用STP協議(Spanning Tree Protocol)，以網絡中一台交換機為節點生成一棵轉發樹，這樣所有的數據都只在這棵樹所指示的路徑上傳輸，就不會產生廣播風暴——因為樹沒有環路。但因為STP算法開銷太大，交換機默認都沒啟用該協議。對策：在接入層啟用樹生成協議，或者在診斷故障時打開樹生成協議，以便協助確定故障點。在廣播風暴發生時，應首先了解發生故障前網絡的改動，建立完善的網絡文檔資料，包括：網絡布線圖、IP地址和MAC地址對應表等，現在可以通過局域網工具軟件來掃描獲取這些信息。
