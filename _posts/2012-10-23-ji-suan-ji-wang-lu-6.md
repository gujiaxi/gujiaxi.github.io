---
layout: post
title: "計算機網路(6)"
date: 2012-10-23 14:55
---
接着上周的 HTTP ，本周的內容主要有 [FTP](http://en.wikipedia.org/wiki/FTP)( File Transfer Protocol ), [SMTP](http://en.wikipedia.org/wiki/SMTP)( Simple Mail Transfer Protocol ), [DNS](http://en.wikipedia.org/wiki/Domain_name_service)( Domain Name Service ) 。

## FTP

![FTP moves files between local and remote file systems.](/assets/img/20121023-1.jpg)

* **client-server model**：client 與 server 的模式。
* **out-of-band**：這也是 FTP 區別於 HTTP 的地方，也就是說 FTP 採用兩個平行的 TCP 連接，包括 control connection( port #21 ) 跟 data connection( port #20 )。
* **stateful operation**：FTP server 必須記錄下關於用戶的狀態，而 HTTP 則不同，它不需要記錄任何用戶的狀態，也就是 stateless 。
* **commands, status code, phrase**： FTP 的通信指令採用 7-bit ASCII 格式。

## SMTP

![Internet e-mail system](/assets/img/20121023-2.jpg)

由上圖可以看出，郵件操作主要依賴於 UA( User Agent ), Mail server, SMTP 三者。

SMTP 工作在 port #25

下面來看 SMTP 與 HTTP 的區別：

* SMTP: push technology; HTTP: pull technology.
* SMTP: multiple objects transmit; HTTP: one object per time
* SMTP: R/W; HTTP: Read only

當然 SMTP 與 HTTP 都是類似 request-response 的概念，都有 ASCII control, status code, phrase

## DNS
DNS 主要提供域名解析服務，將易讀的 hostname 解析成 IP address ，其功能類似於 Indirect 方式。而為了解決規模過大的問題，採用 divide and conquer algorithm ，具體來說是採用 hierarchical data structure ，分為 [root DNS server](http://en.wikipedia.org/wiki/Root_DNS_servers), [top-level domain](http://en.wikipedia.org/wiki/TLD)( TLD ), [authoritative DNS server](http://en.wikipedia.org/wiki/Authoritative_Name_Server)。

DNS 採用分散式架構的優點主要有：avoid single point of failure, keep load balance, reduce internet traffic

Recursive queries: 

![recursive queries](/assets/img/20121023-3.jpg)

Iterative queries: 

![iterative queries](/assets/img/20121023-4.jpg)

## 習題
* **解釋說明執行FTP的過程/運作流程**

  建立 TCP 連接，透過 TCP 連接發送 FTP 指令，前面說到，指令通過21端口傳輸，包括 *USER username*, *PASS password* 來驗證登錄，還有 *LIST* 指令來發送傳輸的文檔列表。之後返回的信息可能是 *331 Username OK, password required*, * 125 Data connection already open; transfer starting*... 如果一切順利就可以通過20端口進行資料的傳輸。

* **編寫程式比較 recursive 與 iterative 的區別**

  ``` c
  #include <stdio.h>
  int recursive(int i)
  {
      if (i > 1) i *= recursive(i-1);
      return i;
  }

  void main()
  {
      int n;
      scanf("%d", &n);
      printf("%d\n", recursive(n));
  }
  ```

  ```c
  void main()
  {
      int i, n;
      scanf("%d", &n);
      for (i = n-1; i > 0; i--)
      {
          n *= i;
      }
      printf("%d\n", n);
  }
  ```

  簡單來說， recursive 的程式越下層負擔越輕，最上層的負擔最重。而 iterative 程式的負擔是均等的，每一次都是一樣的運算。
