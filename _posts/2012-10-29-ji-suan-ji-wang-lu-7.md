---
layout: post
title: "計算機網路(7)"
date: 2012-10-29 17:56
---
這周的課主要圍繞 [cookie](http://en.wikipedia.org/wiki/HTTP_cookie), file sharing( CS & P2P ), socket programming 展開。

## cookie
![HTTP cookie](/assets/img/20121029-1.png)
因此， cookie 的動作包含四個部分：

1. http request - cookie 的功能
2. http response - cookie 的 ID
3. client 的 browser 將此 cookie 值儲存
4. server 將指向 ID 的指標儲存

cookie 的過程皆是有狀態的但 http 是 stateless 的，因此就可以用 http 傳送 state 訊息。

但是 cookie 也有關於隱私權的問題。

## File Sharing
假設某 server 有檔案其大小為 F ，將其下載至 n 個 client ，則需時：

* CS: server 上傳檔案的時間為 nF/μ<sub>s</sub>, client 下載檔案的時間為 F/d<sub>i</sub>。因此 server 中的檔案 F 下載至 n 個 client 所需時間為 MAX{nF/μ<sub>s</sub>, F/MIN{d<sub>i</sub>}}
* P2P: server 上傳檔案的時間為 F/μ<sub>s</sub>, client 下載檔案的時間為 F/d<sub>i</sub>。所有 client 及 server 上傳至網網路的時間為 nF/(μ<sub>s</sub> + ∑μ<sub>i</sub>)

## Socket Programming
1. server 啟動
2. P1 要求 server 服務
3. server 開啟一個 child process S1 提供服務
4. P1 與 S1 建立連結
5. P1 與 S1 進行通訊
6. P2 要求 server 服務
7. server 啟動另一 child process S2 提供服務
8. S2 與 P2 建立連結
9. P2 與 S2 進行通訊

...如此這般，server 可以服務多個 process 。在 Internet 中區隔 process 是靠 IP address, port number

## 習題
* **cookie隱私權問題**

	Cookies在某種程度上說已經嚴重危及使用者的隱私和安全。其中的一種方法是：一些公司的高層人員為了某種目的（譬如市場調查）而存取了從未去過的網站（透過搜尋引擎查到的），而這些網站包含了一種叫做網頁臭蟲的圖片，該圖片透明，且只有一個象素大小（以便隱藏），它們的作用是將所有存取過此頁面的電腦寫入cookie。而後，電子商務網站將讀取這些cookie訊息，並尋找寫入這些cookie的網站，隨即發送包含了針對這個網站的相關產品廣告的垃圾郵件給這些高階人員。

* **試比較 C/S 與 P2P 的效率**

![CS & P2P](/assets/img/20121029-2.png)
