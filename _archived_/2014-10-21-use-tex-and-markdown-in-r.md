---
layout: post
title: "Use Tex and Markdown in R"
date: 2014-10-21 22:40
---
首先标题里的提到了三个东西：[TeX](http://en.wikipedia.org/wiki/TeX)、[Markdown](http://en.wikipedia.org/wiki/Markdown)、[R](http://en.wikipedia.org/w/index.php?title=R_(programming_language))，可以了解一下，简单的说TeX是在科技学术界非常流行的一种排版系统（**科技写作**），Markdown是一种简单易懂的让我们专注内容（而不是排版）的格式（**文艺写作**）、而R是一种用于统计绘图的语言（想想论文里面那些专业的**统计图表**）。所以呢，文科生的话学习一下Markdown就够用了（强烈推荐之，word那一套能不用则不用吧）。

要把这三个东西揉到一块儿，最方便的做法就是在R中安装一个叫做`knitr`的包，或者也可以使用[RStudio](http://www.rstudio.com/)一步到位，详细的我也不多写了，官网上资料很全，下面是几个例子，包括了主要的语法，源文件在R下使用`knitr`处理就行了。

{% highlight r %}
## I am a title

Bold text: **bold**

Italic text: *italic*

list:
- first item
- second item
- third item

table:

| Tables | Are | Cool |
| ------------- |:-------------:| -----:|
| col 1 | Hello | $1600 |
| col 2 | Hello | $12 |
| col 3 | Hello | $1 |

Below is an example of Latex:

$$latex
f(x;\mu,\sigma^2) = \frac{1}{\sigma\sqrt{2\pi}} e^{ -\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2 }
$$

Then, this is the inline version: $\alpha+\beta=\gamma$, $e=mc^2$.

Below is an example of R:
 
```{r block2, fig.width=8, fig.height=5, echo=FALSE}
plot(cars)
```
 
Then, this is the inline version: `r 2*pi`.
{% endhighlight %}

{% highlight r %}
%% LyX 2.0.3 created this file.  For more info, see http://www.lyx.org/.
%% Do not edit unless you really know what you are doing.
\documentclass{article}
\usepackage[sc]{mathpazo}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{verbose,tmargin=2.5cm,bmargin=2.5cm,lmargin=2.5cm,rmargin=2.5cm}
\setcounter{secnumdepth}{2}
\setcounter{tocdepth}{2}
\usepackage{url}
\usepackage[unicode=true,pdfusetitle,
 bookmarks=true,bookmarksnumbered=true,bookmarksopen=true,bookmarksopenlevel=2,
 breaklinks=false,pdfborder={0 0 1},backref=false,colorlinks=false]
 {hyperref}
\hypersetup{
 pdfstartview={XYZ null null 1}}
\begin{document}
<<setup, include=FALSE, cache=FALSE>>=
library(knitr)
# set global chunk options
opts_chunk$set(fig.path='figure/minimal-', fig.align='center', fig.show='hold')
options(formatR.arrow=TRUE,width=90)
@


\title{A Minimal Demo of knitr}


\author{Yihui Xie}

\maketitle
You can test if \textbf{knitr} works with this minimal demo. OK, let's
get started with some boring random numbers:

<<boring-random>>=
set.seed(1121)
(x=rnorm(20))
mean(x);var(x)
@

The first element of \texttt{x} is \Sexpr{x[1]}. Boring boxplots
and histograms recorded by the PDF device:

<<boring-plots, fig.width=4, fig.height=4, out.width='.4\\linewidth'>>=
## two plots side by side (option fig.show='hold')
par(mar=c(4,4,.1,.1),cex.lab=.95,cex.axis=.9,mgp=c(2,.7,0),tcl=-.3,las=1)
boxplot(x)
hist(x,main='')
@

Do the above chunks work? You should be able to compile the \TeX{}
document and get a PDF file like this one: \url{https://bitbucket.org/stat/knitr/downloads/knitr-minimal.pdf}.
The Rnw source of this document is at \url{https://github.com/yihui/knitr/blob/master/inst/examples/knitr-minimal.Rnw}.
\end{document}
{% endhighlight %}

{% highlight r %}
\documentclass{article}
\usepackage{graphicx}
%% for inline R code: if the inline code is not correctly parsed, you will see a message
\newcommand{\rinline}[1]{SOMETHING WRONG WITH knitr}
%% begin.rcode setup, include=FALSE
% library(knitr)
% opts_chunk$set(fig.path='figure/latex-', cache.path='cache/latex-')
%% end.rcode
\begin{document}

Boring stuff as usual:

%% a chunk with default options
%% begin.rcode
% 1+1
%
% x=rnorm(5)
%% end.rcode

For the cached chunk below, you will need to wait for 10 seconds for
the first time you compile this document, but it takes no time the
next time you run it again.

%% chunk options: cache this chunk
%% begin.rcode my-cache, cache=TRUE
% set.seed(123)
% x = runif(10)
% sd(x)  # standard deviation
%
% Sys.sleep(10) # test cache
%% end.rcode

Now we know the first element of x is \rinline{x[1]}. And we also know
the 26 letters are \rinline{LETTERS}. An expression that returns a
value of length 0 will be removed from the output, \rinline{x[1] =
  2011; NULL} but it was indeed evaluated, e.g. now the first element
of x becomes \rinline{x[1]}.

How about figures? Let's use the Cairo PDF device (assumes R $\geq$
2.14.0).

%% begin.rcode cairo-scatter, dev='cairo_pdf', fig.width=5, fig.height=5, out.width='.8\\textwidth'
% plot(cars) # a scatter plot
%% end.rcode

Warnings, messages and errors are preserved by default.

%% begin.rcode
% sqrt(-1) # here is a warning!
% message('this is a message you should know')
% 1+'a'  # impossible
%% end.rcode

\end{document}
{% endhighlight %}

-----

- [Markdown写作浅谈](http://www.yangzhiping.com/tech/r-markdown-knitr.html)
- [自动化报告](https://github.com/yihui/r-ninja/blob/master/11-auto-report.md)
- [knitr](http://yihui.name/knitr/)
