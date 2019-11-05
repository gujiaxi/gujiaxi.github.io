---
layout: post
title: "計算機網路(5)"
date: 2012-10-17 19:45
---
> The Hypertext Transfer Protocol (HTTP), the Web's application-layer protocol, is at the heart of the Web. HTTP is implemented in two programs: a client program and server program. The client program and server programs, executing on different end systems,  talk to each other by exchanging HTTP messages. HTTP defines the structure of these messages and how the client and server exchange the messages.

![HTTP request-response behavior](/assets/img/20121017-1.jpg)

[HTTP](http://en.wikipedia.org/wiki/Http) ( Hypertext Transfer Protocol ) 是網際網路上應用最為廣泛的一種網路協議。所有的WWW檔案都必須遵守這個標準。設計HTTP最初的目的是為了提供一種發行和接收HTML頁面的方法。

Multimedia包括：text, graphic, image, animation, video, voice, music, effect

[HTML](http://en.wikipedia.org/wiki/HTML) ( HyperText Markup Language ) 是为「网页创建和其它可在网页浏览器中看到的信息」设计的一种标记语言。

HTTP 分成 Nonpersistent HTTP 與 Persistent HTTP 。Nonpersistent HTTP：當每傳送一個物件， TCP connection 就必須做一次，假設 client 跟 server 要求多個檔案，當第一個檔案傳輸後會關閉連線，要下載第二個檔案的時候必須再對 server 做一次要求(要求->回應->接收，整個步驟都會重新做)。這種模式主要為 HTTP1.0 使用 ( HTTP 現存的主要有 1.0 和 1.1 兩種 ) ，相較於 HTTP1.1 較費時，因為有一部份的時間都花在建立連線上。Persistent HTTP：接收多個物件時， client 只需要向 server 建立一次連線即可，較省時。

Port number 80 is used as the default port number at which the HTTP server will be listening for HTTP clients that want to retrieve documents using HTTP.

![Clients requesting objects through a Web cache.](/assets/img/20121017-2.jpg)

[Web cache](http://en.wikipedia.org/wiki/Web_cache) ( 又稱 proxy server ) 是一個滿足 HTTP 請求的網路實體，有自己的磁盤存儲空間，並保持最近請求對象的副本。一個 Web cache 既是一個 server 也是一個 client ， 當它與瀏覽器進行接收請求或者發送回應的動作時是一個 server ，而當它與原始服務器進行發送請求或者接收回應的動作時則是一個 client 。顯然， Web cache 的作用主要有三點：降低頻寬、加快響應、提升 server 的性能。

假設每個要求的物件大小為 100 Kbits ，而每秒有 15 個無間的需求量產生，也就是 client 端要求 server 的量為 100 Kbits * 15 = 1.5 Mbps，因此，LAN 的使用率為 1.5 / 10 = 15%，而 Internet 的使用率為 1.5 / 1.5 = 100%，而相應的 traffic intensity 為 15%

假設每個要求的物件大小為 100 Kbits ，而每秒有 15 個無間的需求量產生，也就是 client 端要求 server 的量為 100 Kbits * 15 = 1.5 Mbps，因此，LAN 的使用率為 1.5 / 10 = 15% ，而 Internet 的使用率為 1.5 / 1.5 = 100% ，而相應的 traffic intensity 為 15% 。因此這樣將造成相當大的 delay ，必須加以改善。如果在原有的 LAN 架構上增加建置一個 proxy server ，假設此 proxy server 的 hit rate 為 40% ，其Internet 的使用率就由 100% 降為 60% 。

## 習題
1. **搜尋html主程式呼叫另一html副程式的程式，並解釋說明之。**

   ```html
   <!DOCTYPE html>
   <html lang=en>
   <meta charset=utf-8>
   <meta name=viewport content="initial-scale=1, minimum-scale=1, width=device-width">
   <title>Error 503 (Server Error)!!!</title>
   <style>
   *{margin:0;padding:0}html,code{font:15px/22px arial,sans-serif}html{background:#fff;color:#222;padding:15px}body{margin:7% auto 0;max-width:390px;min-height:180px;padding:30px 0 15px}* > body{background:url(//www.google.com/images/errors/robot.png) 100% 5px no-repeat;padding-right:205px}p{margin:11px 0 22px;overflow:hidden}ins{color:#777;text-decoration:none}a img{border:0}@media screen and (max-width:772px){body{background:none;margin-top:0;max-width:none;padding-right:0}}
   </style>
   <a href=//www.google.com/><img src=//www.google.com/images/errors/logo_sm.gif alt=Google></a>
   <p><b>503.</b> <ins>That’s an error.</ins>
   <p>The service you requested is not available at this time.<p>Service error -27. <ins>That’s all we know.</ins>
   ```

   可以看到，該 html 程式 呼叫了另外的一個 html 程式，而且還呼叫了幾張圖片。

2. **試描述web cache/proxy server所遇到的upadte problem。**

   Web cache 上的資料需要保持與 origin server 上的資料同步才能保證與 client 端進行正確的響應，因此必須保證 Web cache 上的資料能夠及時的更新。
