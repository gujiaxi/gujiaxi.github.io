---
layout: post
title: "計算機網路(3)"
date: 2012-10-03 18:21
---
> Structured programming is a programming paradigm aimed on improving the clarity, quality, and development time of a computer program by making extensive use of subroutines, block structures and for and while loops – in contrast to using simple tests and jumps such as the goto statement which could lead to "spaghetti code" which is both difficult to follow and to maintain.

結構化程式以一些簡單、有層次的程式流架構所組成，可分為循序( sequence )、選擇( select )及重複( repetition )。而計算機網路體系結構採用的是階層式架構( Hierarchical Architecture )。

網路層通訊協定( Network Layer Protocol )由五部分組成： Physical Layer, Data Link Layer, Network Layer, Transport Layer, Application Layer。

每一層都可以在軟體、硬體或者兩者之間實現。Application Layer 跟 Transport Layer 幾乎總是在程式或者是終端系統完成，而 Physical Layer 跟 Data Link Layer 負責處理鏈路之間的通訊問題，所以他們通常是在網路卡中實現。而剩下的 Network Layer 在軟體跟硬體中都有實現。

下面是對各層的簡單介紹：

* **Application Layer**: 應用層支持網路應用。 - HTPP, SMTP, FTP
* **Transport Layer**: 傳輸層負責主機進程間的數據傳遞。 - TCP, UDP
* **Network Layer**: 網路層將數據報從信源傳遞到信宿。 - IP
* **Data Link Layer**: 資料鏈結層負責數據在網路上的相鄰節點間的傳輸。 - PPP, Ethernet
* **Physical Layer**: 實體層負責信道上傳送的位流。

此外，還有一種參考模型叫 [OSI](http://en.wikipedia.org/wiki/OSI_model)( Open System Interconnection Reference Model )，它將計算機網路體系結構劃分為一下七層：應用層( Application Layer )、展現層( Presentation Layer )、會談層( Session Layer )、傳輸層( Transport Layer )、網路層( Network Layer )、資料鏈結層( Data Link Layer )、實體層( Physical Layer )。可以看到，相對於上面的一種劃分， OSI 模型將 Application Layer 劃分成了 Session Layer, Presentation Layer, Application Layer。

## Protocol 與 Interface
Protocol 是虛擬的( virtual )，實際是存在的但是使用時是不存在的，如 [HTTP](http://en.wikipedia.org/wiki/Http)( Hypertext Transfer Protocol ), [SMTP](http://en.wikipedia.org/wiki/Smtp)( Simple Mail Transfer Protocol )。而 Interface 是通透的( transparent )，實際是不存在的但是使用時是存在的，如 [GUI](http://en.wikipedia.org/wiki/Graphical_user_interface)( Grphical User Interface ), [CLI](http://en.wikipedia.org/wiki/Command-line_interface)( Command-line Interface )
