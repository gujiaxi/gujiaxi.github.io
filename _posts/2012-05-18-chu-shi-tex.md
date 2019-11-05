---
layout: post
title:  "初识TeX"
date:   2012-05-18 23:42
---
> 高德纳最早开始自行编写TeX的原因是当时十分粗糙的排版水平已经影响到他的巨著《计算机程序设计艺术》（The Art of Computer Programming）的印刷质量。他以典型的黑客思维模式，最终决定自行编写一个排版软件：TeX。他原本以为他只需要半年时间，在1978年下半年就能完成，但最终他用了超过十年时间，直到1989年TeX才最终停止修改。

[TeX](http://en.wikipedia.org/wiki/TeX)，具有传奇色彩的一个工具，历史相当悠久（年纪竟然比我还大？！），它的版本号是按照圆周率来算的，越接近圆周率，版本号越高，目前最新的稳定版本是3.1415926。总之，我想说的是……这实在是一款博大精深的杰作，当然学习曲线也不是一般得高咯，我等小白只能沾点皮毛。

## 安装
我使用的是ArchLinux+TeX Live的组合，关于TeX Live，Arch的[wiki](https://wiki.archlinux.org/index.php/TeX_Live)上面也有写到，按照上面说的，可以安装`texlive-most`这个软件包组或者只安装`texlive-core`这个包，都可以，当然你也可以按照[tug.org](http://tug.org/texlive/)上面的方法完整安装。

## 开始使用
因为我也是初学，对于它的使用实在不敢多说，就给一个书上看来的例子吧，保存为`filename.tex`然后运行`pdflatex filename.tex`应该就可以看到生成的pdf文档了。

```tex
\documentclass{article}
\begin{document}
Hello World!
\end{document}
```

## 中文化
中文化也是一个很复杂的问题，有很多很多方面我也不太清楚。我就说一下中文字体的设置吧。

### xeCJK
使用`xeCJK`宏包可以直接调用系统的字体，不过如果你跟我一样，系统里面的中文字体就只有一种，可以把需要的中文字体文件拷贝过来再直接引用字体文件名，下面是一个引用宋体的例子，注意，这时候要用`xelatex`而不是`pdflatex`来生成。

``` tex
\documentclass{article}
\usepackage{xeCJK}
\setCJKmainfont{simsun.ttc}
\begin{document}
Hello World!你好世界！
\end{document}
```

### CJK
也可以利用`CJK`宏包来实现

``` tex
\documentclass{article}
\usepackage{CJK}
\begin{document}
\begin{CJK}{UTF8}{gkai}
这是一个楷体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{gbsn}
这是一个宋体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{bkai}
這是一個big5編碼的楷體中文測試，處理繁體文字。
\end{CJK}
\begin{CJK}{UTF8}{bsmi}
這是一個个big5編碼的明體中文測試，處理繁體文字。
\end{CJK}
\end{document}
```

### ctex
这个是最推荐的一个方案。

``` tex
\documentclass{article}
\usepackage[UTF8]{ctex}
\begin{document}
中文测试。
\end{document}
```

## 继续学习
网络上关于TeX的资源有很多，一起努力吧！！

-----

- [TeX 参考资料](http://www.math.zju.edu.cn/ligangliu/LaTeXForum/tex_doc.htm)
