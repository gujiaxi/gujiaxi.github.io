---
layout: post
title: "McCarthy 91 function"
date: 2014-10-22
---
今天下午数学课上老师讲到这个函数——[McCarthy 91 function](http://en.wikipedia.org/wiki/McCarthy_91_function)，原理是这样的：

$$
M(n)=
\begin{cases}
\begin{aligned}
& n-10 & (x > 100) \\
& M(M(n+11)) & (x \leq 100)
\end{aligned}
\end{cases}
$$

写成Lisp函数就是：

```elisp
(defun mc91(x) (if(> x 100)(- x 10)(mc91 (mc91 (+ x 11)))))
```
