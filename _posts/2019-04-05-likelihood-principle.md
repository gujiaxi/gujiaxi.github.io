---
layout: post
title: "Likelihood Principle"
date: 2019-04-05
---

> **The likelihood principle**: given a generative model for data $d$ given
> parameters $\theta$, $P(d|\theta)$, and having observed a particular outcome
> $d_1$, all inferences and predictions should depend only on the function
> $P(d_1 | \theta)$.

## 问题一

盒子A里有1个黑球和1个白球，盒子B里有1个黑球和2个白球，某人从其中一个盒子里取出了一个黑球，问：该黑球来自盒子A的概率是多少？

### 错误解答

**解答**: 既然已经知道取出的是黑球了，那它不是来自A盒就是来自B盒，而A盒跟B盒里的黑球数是一样多的（都各有1个），那么问题的答案也就是$\text{A盒中的黑球数} / (\text{A盒中的黑球数} + \text{B盒中的黑球数}) = \frac{1}{2}$了。

**分析**: 既然该解答认为结论与白球数无关，那么不妨将B盒中的白球数增加到十万个，这种情况下的结论还是“该黑球来自A盒的概率是$1/2$”，但是直觉上来看：“B盒那么多球里只有一个黑球，我就 *不信* 你取出的这个黑球 *刚好* 是来自B盒！”

### 正确解答

**解答**: 我们用$x \in \{b, w\}$表示取出的球是黑球或白球，用$\theta \in \{A, B\}$表示从A盒或B盒取球，那么在没有取球这个实验之前，可以假设从A盒或B盒取球是等可能的，也就是$P(\theta = A) = P(\theta = B) = \frac{1}{2}$。那么根据题意，在已经取出一个黑球的情况下，问题可以表达为“在取出黑球的前提下，这个球是从A盒取的概率”$P(\theta = A \| x = b)$。根据贝叶斯公式：

$$
\begin{aligned}
P(\theta = A | x = b) &= \frac{P(x = b | \theta = A) P(\theta = A)}{\Sigma_{\theta^\prime \in \{A, B\}}P(x = b | \theta^\prime) P(\theta^\prime)} \\
&= \frac{\frac{1}{2} \cdot \frac{1}{2}}{\frac{1}{2} \cdot \frac{1}{2} + \frac{1}{3} \cdot \frac{1}{2}} \\
&= \frac{3}{5}
\end{aligned}
$$

## 问题二

盒子A里有1个黑球和1个白球，盒子B里有1个黑球和2个白球，问：从两个盒子里任取一球是黑球的概率是多少？

### 错误解答

**解答**: 既然问的是取黑球的概率，那么就跟从哪个盒子里取没有关系，只跟球的黑白有关，所以答案是：$\text{黑球总数} / \(\text{黑球总数} + \text{白球总数} ) = \frac{1}{2}$.

**分析**: 我们不妨将B盒中的白球数加到十万个，那么按照此种解答，取到一个黑球的概率应该是极小的。但是要注意，球是分盒子装的：“只要我选对了盒子，取到黑球不见得就很难吧！”

### 正确解答

我们仍采用上题的符号定义，那么：

$$
\begin{align*}
P(x = b) & = \Sigma_{\theta \in \{A, B\}}P(x = b | \theta)P(\theta) \\
& = \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{3} \cdot \frac{1}{2} \\
& = \frac{5}{12}
\end{align*}
$$
