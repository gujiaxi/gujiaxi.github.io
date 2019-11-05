---
layout: post
title: "計算機網路(12)"
date: 2012-12-26 18:07
---
這周的要點主要是LAN的通訊模式。

網路結構主要有**集中式**跟**分散式**兩種，要看此系統是否由一個clock source來驅動。

多部電腦群聚在一起的通訊方式有：point-to-point, broadcast (broadcast, multicast, unicast)。

LAN的通訊模式分為Sequential (TDM, FDM), Random, Token

TDM的優點：不會相互干擾；缺點：不使用造成浪費。

Random: CSMA (Carrier Same Multiple Access)

Token: Token bus擁有token才擁有通訊的權利，例如host A有token即可傳輸資料，若不想傳輸則將token交給下一個host。

## CSMA/CD
直接傳送資料，資料碰撞時，停止傳輸，節省後方繼續傳輸的時間。

1. 偵測carrier，若是busy則等待；若是idle則送出資料。
2. 送出資料後，偵測carrier，若是collision，則停止傳送並等待；若無collision，則繼續傳送直到結束。
3. 重複①,②。

若偵測到collision，則等待的方法稱為Binary Exponential Backoff。

1st:    back 2^-1    {0, 1}

2nd:    back 2^-2    {0, 1, 2, 3}

3rd:    back 2^-3    {0, 1, 2, 3, 4, 5, 6, 7}

...

kth:    back 2^-k    {0, 1, 2, 3, ... , k-1}

## CSMA/CA
藉由 RTS/CTS 機制，先行了解網路狀況、建立連線，藉此避免碰撞，增加網路效益。

1. 偵測頻道是否有別人在使用。偵測期間需為 IFS 時間加上一個亂數時間，若沒有人使用則繼續下一步。
2. 傳送端送出 RTS 給接收端，告訴對方想要傳送資料。
3. 接收端收到 RTS 封包後，會在IFS時間內回應 CTS 給傳送端。
4. 傳送端收到 CTS 封包後，會開始傳送資料。假若沒有收到，就假設碰撞回到第一步重新開始。
5. 接收端收到資料會回應ACK進行確認；若傳送端未收到 ACK 封包，就判定傳送失敗，回到第一步重新開始。

避免碰撞：其他節點如果偵測到媒體中存有 RTS 或 CTS 訊號時，則會因為處於延遲時間凍結的階段，因此不會在此時傳送資料。萬一正巧到達延遲時間，便會造成眾多RTS/CTS 訊號彼此發生碰撞，對於傳送資料的訊號來說，並不會造成任何影響。透過上述的策略，把發生碰撞的時機控制在 RTS 或 CTS 控制訊號發送期間上，便可大幅度降低碰撞機率，提高網路效率。
