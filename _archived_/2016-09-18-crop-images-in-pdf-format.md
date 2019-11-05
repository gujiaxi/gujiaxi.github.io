---
layout: post
title: "Crop Images in PDF format"
date: 2016-09-18 16:50
---

在处理论文插图的时候通常需要把白边去掉，一般的$\LaTeX$发行版都提供了`pdfcrop`来实现根据bounding box的裁剪，下面是基于此的一个Windows批处理文件，直接把要裁剪的pdf文件拖放到这个批处理上就能行了。

```
@echo off
pdfcrop %~nx1 tmp.pdf
del %~nx1
ren tmp.pdf %~nx1
echo Done!
pause
```
