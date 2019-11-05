---
layout: post
title:  "LibreOffice使用Windows字体"
date:   2012-04-11 13:40
---
最近要填一堆材料，都是比较重要的材料，当然字体也是有严格要求的，不过我的ArchLinux只安装了文泉译字体，当然就不符合规范咯，当然我可以在AUR上下载相应的字体安装，不过那样全局的字体就都被修改了，而且也不符合极简主义，所以我打算只修改LibreOffice下面可选的中文字体。

很简单，直接用Windows下的字体就行了，Windows下字体的存放路径是`c:\windows\Fonts`。里边儿有很多字体，我选择了几个：

```
msyh.ttf    # 微软雅黑
simfang.ttf # 仿宋体
simhei.ttf  # 黑体
simkai.ttf  # 楷体
simsun.ttf  # 宋体
STKAITI.TTF # 华文楷体
STLITI.TTF  # 华文隶书
STSONG.TTF  # 华文宋体
```

然后再在`~/.config/libreoffice/3/user/`目录（路径可能因发行版不同而不同）下新建一个`fonts`目录，把复制过来的字体文件放进去就行了。
