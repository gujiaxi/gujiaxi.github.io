---
layout: post
title: "Fizz Weekly Issue #19"
date: 2017-11-25 11:45
---

## 睹·Reads

- [Three Developer Tools I'm Thankful For](https://developer.okta.com/blog/2017/11/22/three-developer-tools-im-thankful-for)

  Vim, Tmux, Zsh. 三大神器。

- [Modern Media Is a DoS Attack on Your Free Will](http://nautil.us/issue/52/the-hive/modern-media-is-a-dos-attack-on-your-free-will)

  > When information becomes abundant, attention becomes scarce. Advertising has dragged everybody down, even the wealthiest organizations with noble missions, to competing on the terms of click bait.

  后稀缺时代的担忧，信息过剩对于人的个人和社会带来了一系列的负面影响。

- [Living on the Plateau](http://blog.cleancoder.com/uncle-bob/2017/11/18/OnThePlateau.html)

  作者是软件开发老司机Uncle Bob，软件设计语言的进化是跟每个时代的计算机架构密切相关的，但是就目前来说，CPU的时钟频率在经过了快速增长之后开始停滞在一个水平，固然我们对核心数的增长仍抱有很大期望，但实际上来说八核的设备迟迟没有到来（可能是因为成本，也可能是因为需求）。这也就是为什么以“多线程友好”(这种说法不一定准确)为其一大亮点的函数式语言一直没有流行的原因。而目前这样的一个plateau时代流行的语言假设拥有无限的资源，它们也都确实顺应了时代的潮流。就软件设计语言的进化来说，在当今这个时代难道就没有继续向前发展，向前探索的动力了吗？如果有，应该是什么呢？

- [我们与电子科技的热恋结束了](https://cn.nytimes.com/opinion/20171122/internet-digital-technology-return-to-analog/)

  本文提出了一种“模拟技术”的说法（相对于电子化、信息化的“数字技术”），令我感到惊讶的是传统纸质书籍销量竟然一直在上涨而电子书销量在下滑。黑胶、拍立得、手账、桌游……其实我们还是对“模拟技术”有很深的感情的，联系近年来对互联网时代的担忧(e.g., distraction, privacy, censorship...)，我也觉得我们需要在数字技术和模拟技术之间取得一种平衡，才能更好地拥抱生活。

- [肆無忌憚的刪帖時代，「謠言」才是抵達真相的途徑？](https://theinitium.com/article/20171125-opinion-kindergarten/)

  > 如果中國有可信賴的、獨立運作的媒體，我同意我們應該先看調查報導再說話——可惜沒有，這是媒體的末法時代，普通人如果不說話，換來的只有沉默。

  国内互联网的审查制度由来已久，公众应该也已经习以为常了，但是这对于新闻媒体恰恰是致命的（我想这也是为什么国内充斥着大量无关痛痒的娱乐消遣类的热点新闻），有太多的不能说、不能写、不能播。当然我们在责怪删贴、屏蔽的同时，换个角度想想，国内网民人口基数大，教育程度差异也很大，有一些可以称得上是互联网时代的婴儿，如果没有审查，公众固然可以获得关于事件“全方位”、“多角度”的专业的、不专业的报道，但是自媒体盛行的年代，谁能保证没有人“胡说霸道”，有些民众在面对这样繁杂的信息轰炸的情况下或许还没有能力进行独立地思考。

## 研·Researches

- *Speech Activity Detection using Accelerometeri* [^1]
  - 本文的目的是要识别人日常生活中的说话活动（speech activity）。
  - 方法是在胸口贴一个加速度计。

- *Accurate and Privacy Preserving Cough Sensing using a Low-Cost Microphone* [^2]
  - 本文动机是要做咳嗽检测，在准确检测的基础上避免恢复语音泄露隐私
  - 把手机挂在胸口或者放在上衣胸口的口袋中，麦克风朝向嘴部

## 思·Thoughts

> 不使用——至少是不仅仅使用——例如微信、微博这种没有强加密保护，且众所周知受到严格言论审查的工具，发生种种恶性事件时，妳才会有可以自由讨论的空间。妳或许没有什么秘密、没有什么隐私，但所有事情都是相关的。妳不可能事到临头才忙着找新工具。
>
> --- *@liruyi*

-----

[^1]: Matic, Aleksandar, Venet Osmani, and Oscar Mayora. "Speech activity detection using accelerometer." Engineering in medicine and biology society (EMBC), 2012 annual international conference of the IEEE. IEEE, 2012.
[^2]: Larson, Eric C., et al. "Accurate and privacy preserving cough sensing using a low-cost microphone." Proceedings of the 13th international conference on Ubiquitous computing. ACM, 2011.
