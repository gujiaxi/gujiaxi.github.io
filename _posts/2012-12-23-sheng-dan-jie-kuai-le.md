---
layout: post
title: "圣诞节快乐"
date: 2012-12-23 17:39
---
聖誕節到了，自己動手做了一張賀卡送給朋友，不過鑒於本人動手能力實在抱歉，所以還望大家輕拍……輕拍……

![Christmas Card](/assets/img/20121223-1.png)

上面是賀卡設計圖，樣式很簡單，就是傳統的賀卡形式，四個面（不妨分別喚作ABCD面）內容都挺簡單，不過我還是大致分開寫一下各個面都是些什麼吧。

首先是封面（也就是A面），封面當然是最重要的，但是又要避免落入俗套，所以還是玩了點兒小花樣，借用點陣字體的方式匯出`4A 69 6E 67`，同時為了看起來不那麼單調，四組分了兩排，兩排字體分別採用了一陰一陽的點陣（或許這裡還有一個考慮，因為要送的那個朋友是雙子座。:p）。至於這四組碼是什麼意思想必大家都猜到了，不過還是稍微提醒一下：ASCII。

然後是裡面打開之後的B面，這個沒有什麼特別的，就是一個QR Code，解開就行了，答案我就不公布了。

再下來是C面，C面……本來想寫些祝福語之類的，但是這顯然不是我的style嘛，所以……

```perl
#!/usr/bin/env perl
use strict;
use warnings;
use Encode 'encode_utf8';

my $s = ' ' . encode_utf8(pack 'U', 0x2605);
my $f = encode_utf8(pack 'U', 0xFF0F);
my $b = encode_utf8(pack 'U', 0xFF3C);
my $o = [ map { encode_utf8(pack 'U', $_) } (
    0x0069, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020,
    0x0020, 0x0020, 0x0020, 0x0020, 0x0020, 0x0020,
    0x0020, 0x2E1B, 0x2042, 0x2E2E, 0x0026, 0x0040, 0xFF61,
) ];
my $oc = [ 21, 33, 34, 35, 36, 37 ];
my $l  = pack 'U', 0x005e;

sub tree {
    my ($H) = @_;

    print("\n");
    print(" " x $H);
    print("\033[33m" . $s . "\n");
    my $M = $H * 2 - 1;
    for my $L (1 .. $H) {
        my $O = $L * 2 - 2;
        my $S = ($M - $O) / 2 + 1;
        print(" " x $S);
        print("\033[32m" . $f);
        for (1 .. $O) {
            print("\033[" . $oc->[ int(rand @$oc) ] . "m" . $o->[ int(rand @$o) ]);
        }
        print("\033[32m" . $b . "\n");
    }
    print(" ");
    print("\033[32m" . $l) for 1 .. $H - 1;
    print("|  |");
    print("\033[32m" . $l) for 1 .. $H - 1;
    if ($H > 10) {
        print("\n ");
        print(" ") for 1 .. $H - 1;
        print("|  |");
        print(" ") for 1 .. $H - 1;
    }
    print("\n\n");
}

tree(20);
```

運行結果應該是類似於下圖的一棵由各種字符組成的聖誕樹。

![](/assets/img/20121223-2.png)

最後是封底（也就是D面），為了貫徹極簡的人生哲學，就索性只寫上了一句：

```sh
[isaac@thu ~]$ echo "aHR0cDovL2lzLmdkL3lqbmdqeAo=" | base64 -d
```

唉我也不賣關子了，其實大致就是作者信息啦（not exactly），base64解開就得到答案了：[http://is.gd/yjngjx](http://is.gd/yjngjx) （btw. **thu**是我們學校的縮寫）

好了，大致就是這樣，不過……其實……總之實踐起來比我想象的要難得多，本來打算是用有格子的紙的（因為比較適合畫點陣圖還有QR碼）不過因為一些原因最後用了純白的紙板，然後就是布局跟字體比例大小的問題，確實挺傷腦筋的。筆的話……因為沒有太多時間，就用了一隻2B鉛筆，要是有時間的話還打算用彩筆給代碼加亮呢哈哈。

最後再上一張圖，Merry Christmas to you all!

![](/assets/img/20121223-3.jpg)
