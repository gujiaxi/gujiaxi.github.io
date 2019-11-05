---
layout: post
title: "Fizz Weekly Issue #20"
date: 2017-12-03 11:24
---

## 睹·Reads

- [纪思道：天安门事件和我的道德困境](https://cn.nytimes.com/china/20160708/nicholas-kristof-china-tiananmen-times-insider/)

  让我想起了韩国的那部电影《出租车司机》，越来越感受到新闻传播对于这个世界的重要性。

- [给老师、学者、教授们的公开信](https://blog.yitianshijie.net/2017/07/24/open-letter-to-the-academics/)

  文化可能听起来太抽象，往狭义了说可以是大部分中国人对于政治、科技的冷感。

- [Indie Game Tide Vol.22 : What Remains of Edith Finch](https://www.indienova.com/indie-game-review/indie-game-tide-vol-22/)

  周六晚上玩了《艾迪芬奇的记忆》，设计非常巧妙，叙事也非常流畅、精彩，算是难得的一个好游戏，但总觉得跟马力欧、塞尔达之流相提并论的话有点对后两者不公平。

- [北京「切除」：11張圖帶你看懂「低端人口」清退行動](https://theinitium.com/article/20171201-mainland-Beijing-uprooted/)

  对于最近北京驱赶“低端人口”这一事件，在这周的《一天世界》播客里李如一也对此发表了评论，他由清理“低端人口”联想到了清理纽约的流浪汉（这里的联系仅仅是对于清理某类人以改善“城市面貌”这一措施来说的，就两个人群本身来说并不能完全对应）而其实很多人心里都排斥流浪汉（纳税人的钱被浪费在这帮无业游民身上……）。
  其次，舆论的激烈反应主要是来自当权者采取的强硬态度以及“低端人口”这一带有侮辱性的措辞，有意思的是，对于后者，他提到了市场营销上的“低（高）端市场”，对于“低端人口”这一说法，我粗略查了一下，中国人民政治协商会议北京市第十二届委员会第一次会议（2013）年相关的[报道](http://bjzx.gov.cn/html/lshg/meet2013/jy/jy_087.htm)中就已经采用了这一说法。

## 研·Researches

- *A Survey of Rate Adaptation Techniques for Dynamic Adaptive Streaming over HTTP* [^1]
  - 关于DASH比较新比较全的一个survey。
  - 为了避免视频的卡顿，主要的做法有以下几种 (市面上广泛采用的是1、4两种)：
    1. 在客户端使用缓冲区
    2. 在服务器端启用转码服务
    3. 在服务器端启用可扩展编码 (Scalable Video Coding)
    4. 多流切换的方法。

## 思·Thoughts

最近，北京除了“清理低端人口”这一举措外，其实还推行了一个规范建筑天际线的方案，这一方案的做法简单来说就是规定了商店的招牌应该怎么摆、不能怎么摆。听到这一消息，大部分人应该会第一时间想到香港、东京拥挤的街道和闪烁的霓虹灯，甚至科幻电影如银翼杀手中的场景，加上对强权习惯性的不信任，会觉得政府管得太宽了，甚至会过激到觉得规范化的审美即是集权的体现。我觉得本周《一天世界》中主播李如一的观点很独到，他由这个规定想到了苹果的[Human Interface Guidelines](https://developer.apple.com/design/)，简单来说就是对苹果系统下的人机交互设计规范（相比这个政府所推行的规定当然更加强硬），我觉得在大部分人看来，这样的规范是合理甚至值得遵守的，为什么在城市建设上就不容许出现统一的规范呢？另一方面，播客中提到了一个概念——现代社会简约主义的霸权，无印良品、优衣库、宜家……大家的审美似乎也在趋于统一——简约、简洁、极简。

-----

[^1]: Kua, Jonathan, Grenville Armitage, and Philip Branch. "A Survey of Rate Adaptation Techniques for Dynamic Adaptive Streaming over HTTP." IEEE Communications Surveys & Tutorials (2017).
