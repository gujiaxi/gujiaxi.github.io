---
layout: post
title: "計算機網路(1)"
date: 2012-09-19 19:30
---
這周的課程比較簡單，大致回顧了一下計算機的組成、資料結構、演算法則、網路……

## 計算機的組成
計算機大致由I/O、CPU、Memory組成，分別實現輸入/輸出、運算、存儲功能。而冯·诺依曼将计算机分成五大基本部分：输入设备、存储设备、运算器、控制器和输出设备。然後計算機（Computer）跟計算器（Calculator）的區別就在於記憶體（Memory），就像數學（Mathematics）跟算術（Arithmetic）的區別在於數學中有變數的運用，從某種程度上來說也就是記憶（Memory）的問題。

## 資料結構
資料結構與記憶體有着密不可分的聯繫，抽象來說就是空間的利用，好的資料結構可以節省記憶體的空間，而相對的，不合理的資料結構會影響到記憶體的利用率。

## 演算法則
與專註存儲而言的資料結構相對的，演算法則對應的是數據的處理，好的演算法則可以節省時間，而不良的演算法則會浪費時間，不過從個人經驗來看，精彩的演算法則往往不容易想到哦～

## 計算機網路
網路架構大致可以分為兩種：一種是點對點架構（per-to-peer architecture），就是俗稱的P2P，另外一種是主從式架構（client-server model）。如今常用的還是P2P。

**Network Edge**: Host, Communication Link/Access Line, Node

**Network Core**: Circuit Switching（線路交換）, Packet Switching（分封交換）

分封交換將資料分割為許多固定長度的封包再送出，解決了線路交換中出現的**佔線**問題。

## 習題
* **雞兔同籠問題**

問題重述：把雞跟兔子放在一個籠子里，從上面看可以看到32個頭，下面看可以看到108只腳，問有幾隻兔子幾隻雞？

解決方案：首先如果用算術的方法來解的話，可以先把所有的雞跟兔子都看成兩隻腳，這樣可以得到的就是（腳-頭\*2）/2=兔子的數目，然後雞的數目就可想而知了。如果用數學的方法引進變數，可以假設雞有x只，兔有y只，然後就可以列出兩個方程：2\*x+4\*y=108, x+y=32。同樣可以得到答案。

* **資料結構與演算法則之間的矛盾**

以簡單的搜索來看：一種是對應已排序的數據進行二分搜尋，另外一種是以二元樹為資料結構的直接搜索。下面我們來看看兩種搜尋方式有什麼不同。

二分搜尋對於資料結構的要求比較高，必須要是已經排序的數據才行，但是搜索的時間複雜度較低。下面是二分搜尋的C語言實現：
```c
int BinarySearch(int *sorted, int n, int k)
{
	int left = 0, right = n-1, mid;
	mid = (left + right) / 2;
	while (left <= right) {
		if (sorted[mid] == k) return mid;
		if (sorted[mid] > k) right = mid - 1;
		else (sorted[mid] < k) left = mid + 1;
	}
	return -1;
}
```

再來看二元搜尋樹，二元搜尋樹對於數據的結構沒有二分搜索來得嚴格，不過效率也會因為資料結構的差異而有所變化：
```c
bool SearchBTree(BTree root, int data)
{
	if(!root) return false;
	else if (root->data == data) return true;
	else if (root->data > data) return SearchBTree(root->LChild.data);
	else return SearchBTree(root->RChild.data);
}
```

## TDM 與 FDM
TDM(分時多工)的原理是採用同一物理鏈接，把時間分割成小段，不同時段來傳輸不同的信號，所以更適合傳輸數字信號。

FDM(分頻多工)的原理是將整個頻帶劃分為不同的頻率，不同的信號在不同的頻率下傳輸，因此適合傳輸模擬信號。

![](/assets/img/20120919-1.jpg)
上面的圖片可以很清楚的看出兩者的區別。


## Circuit Switching 與 Packet Switching
Circuit Switching(線路交換)是按時計價，先建立再傳輸，所以成本會比較高，但是相對來說效果要更好。

Packet Switching(分封交換)是按量計價，先存儲再發送(store and forward)，這樣的優點是不需要線路交換中花費的overhead，成本降低了，但是就請求與響應來說，一般頻率會不一致，因此需要buffer來控制。

## 幾個名詞
* **Overhead**: 在計算機網路中，除了實際有效的開銷以外，還有很多額外的為了保證通信的完成而必不可少的開銷，這些開銷稱為overhead。

* **Buffer**: 在數據傳輸中，用來彌補不同數據處理速率差距而建立的暫存區稱為buffer。

* **Delay Time**: 1/(μ-λ). μ: Service Rate; λ: Arrival Rate
