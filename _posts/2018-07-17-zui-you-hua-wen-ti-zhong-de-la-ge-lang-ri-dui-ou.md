---
layout: post
title: "最优化问题中的拉格朗日对偶"
date: 2018-07-17
---

## 原始问题与对偶问题

一切优化问题都可以表示成如下的标准形式：

$$
\begin{align}
\min_\boldsymbol{x} \; & f_0(\boldsymbol{x}) \\
s.t. \; & f_i(\boldsymbol{x}) \leq 0 \;\; i = 1, \cdots, m \\
& h_j(\boldsymbol{x}) = 0 \;\; j = 1, \cdots, n
\end{align}
$$

这样一个既包含不等式约束也包含不等式约束的表述比较麻烦，于是我们把这个问题重新表述成如下的优化问题：

$$
\min_\boldsymbol{x}\mathcal{L}(\boldsymbol{x})
$$

其中：

$$
\mathcal{L}(\boldsymbol{x}) =
\begin{cases}
f_0(\boldsymbol{x}) & \text{if} \; f_i(\boldsymbol{x}) \leq 0, \forall i \in \{1, \cdots, m\} \; \text{and} \; h_j(\boldsymbol{x}) = 0, \forall j \in \{1, \cdots, n\} \\
\infty & \text{otherwise}
\end{cases}
$$

注意，这里只是换了一种表述，优化问题还是跟原来的等价。我们发现即使是这样的表达式，后面还是跟着两个约束条件，接下来我们想办法把约束条件整合到优化目标表达式中，首先我们考虑等式约束$h_j(\boldsymbol{x})$：

$$
\min_{\boldsymbol{x}}\max_{\boldsymbol{\nu}} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\nu})
$$

其中：

$$
\mathcal{L}(\boldsymbol{x}, \boldsymbol{\nu}) =
\begin{cases}
f_0(\boldsymbol{x}) + \sum^n_{j=1}\nu_j h_j (\boldsymbol{x}) & \text{if} \; f_i(\boldsymbol{x}) \leq 0, \; \forall i \in \{1, \cdots, m\} \\
\infty & \text{otherwise}
\end{cases}
$$

我们称$\boldsymbol{x} \in \mathbb{R}^d$为原始变量（primal variables），这个引入了对偶变量（dual variables）$\boldsymbol{\nu} \in \mathbb{R}^n$的优化问题与原问题还是等价的，原因如下。假如存在$h_j(\boldsymbol{x}) \neq 0$，那么总可以取合适的$\nu_j$让它们的乘积达到$\infty$，即内层的最大化函数输出为无穷，导致外层的最小化函数直接抛弃这样的输出，因此，整个优化问题就只在$h_j(\boldsymbol{x})=0$的时候有合理的输出，这样就隐含了原始优化问题中的等式约束，于是，顺着类似的思路，我们把不等式约束也放到优化目标表达式中：

$$
p^{\ast} = \min_{\boldsymbol{x}}\max_{\boldsymbol{\lambda}\geq\boldsymbol{0}, \boldsymbol{\nu}} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}, \boldsymbol{\nu}) = f_0(\boldsymbol{x}) + \sum^m_{i=1}\lambda_i f_i(\boldsymbol{x}) + \sum^n_{j=1}\nu_j h_j(\boldsymbol{x})
$$

这个优化问题跟原问题还是等价的，原因如下。假如存在$f_i(\boldsymbol{x}) > 0$，那么总可以取合适的$\lambda_i$来使其乘积达到$\infty$从而使内层的最大化函数输出无穷，进而导致外层的最小化函数抛弃这样的输出。反之，在$f_i(\boldsymbol{x}) \leq 0$的情况下，由于$\lambda_i \geq 0$，内层的最大化函数保证了只有在$\lambda_i = 0$的情况下输出最大值为$f_0(\boldsymbol{x})$，这样就保证了原来的不等式约束条件，即$f_i(\boldsymbol{x}) \leq 0$，整个优化问题也跟原来的问题等价。因为这个优化问题最外层是有关原始变量的优化，所以被称为原始问题（primal），记作$p^{\ast}$。这里的优化目标$\mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}, \boldsymbol{\nu})$被称为拉格朗日算子（Lagrangian），其中包括了原始变量$\boldsymbol{x} \in \mathbb{R}^d$，以及对偶变量$\boldsymbol{\lambda} \in \mathbb{R}^n$和$\boldsymbol{\nu} \in \mathbb{R}^m$。

现在，我们原始问题中的两层最大最小化调换位置，这样最外层就是关于对偶变量的最优化，所以该最优化问题就叫做对偶问题（dual），记作$d^{\ast}$：

$$
d^{\ast} = \max_{\boldsymbol{\lambda} \geq \boldsymbol{0}, \boldsymbol{\nu}} \min_\boldsymbol{x} \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}, \boldsymbol{\nu})
$$

这里要特别注意，对偶问题跟原始问题并不是等价的，不过它们之间存在某些关系，下面会介绍。

## 强对偶与KKT条件

我们来看原始问题和对偶问题之间的关系，可以证明有如下的关系总是成立：

$$
p^{\ast} \geq d^{\ast}
$$

证明如下：

首先，我们知道

$$
\forall \boldsymbol{x}, \, \boldsymbol{\lambda} \geq \boldsymbol{0}, \, \boldsymbol{\nu} \;\; \max_{\tilde{\boldsymbol{\lambda}} \geq \boldsymbol{0}, \tilde{\boldsymbol{\nu}}} \mathcal{L}(\boldsymbol{x}, \tilde{\boldsymbol{\lambda}}, \tilde{\boldsymbol{\nu}}) \geq \mathcal{L}(\boldsymbol{x}, \boldsymbol{\lambda}, \boldsymbol{\nu}) \geq \min_{\tilde{\boldsymbol{x}}} \mathcal{L}(\tilde{\boldsymbol{x}}, \boldsymbol{\lambda}, \boldsymbol{\nu})
$$

既然上述关系是对于所有满足条件的$\boldsymbol{x}, \boldsymbol{\lambda} \geq \boldsymbol{0}, \boldsymbol{\nu}$都成立，那么我们可以如下设置变量：

$$
\begin{align}
\boldsymbol{x} = & \operatorname*{arg\,min}_{\tilde{\boldsymbol{x}}} \max_{\tilde{\boldsymbol{\lambda}} \geq \boldsymbol{0}, \tilde{\boldsymbol{\nu}}} \mathcal{L}(\tilde{\boldsymbol{x}}, \tilde{\boldsymbol{\lambda}}, \tilde{\boldsymbol{\nu}}) \\
\boldsymbol{\lambda}, \boldsymbol{\nu} = & \operatorname*{arg\,max}_{\tilde{\boldsymbol{\lambda}} \geq \boldsymbol{0}, \tilde{\boldsymbol{\nu}}} \min_{\tilde{\boldsymbol{x}}} \mathcal{L}(\tilde{\boldsymbol{x}}, \tilde{\boldsymbol{\lambda}}, \tilde{\boldsymbol{\nu}})
\end{align}
$$

因此就有：

$$
p^{\ast} = \min_{\tilde{\boldsymbol{x}}} \max_{\tilde{\boldsymbol{\lambda}} \geq \boldsymbol{0}, \tilde{\boldsymbol{\nu}}} \mathcal{L}(\tilde{\boldsymbol{x}}, \tilde{\boldsymbol{\lambda}}, \tilde{\boldsymbol{\nu}}) \geq \max_{\tilde{\boldsymbol{\lambda}} \geq \boldsymbol{0}, \tilde{\boldsymbol{\nu}}} \min_{\tilde{\boldsymbol{x}}} \mathcal{L}(\tilde{\boldsymbol{x}}, \tilde{\boldsymbol{\lambda}}, \tilde{\boldsymbol{\nu}}) = d^{\ast}
$$

$p^{\ast} \geq d^{\ast}$证毕。

原始跟对偶之间的差值$p^{\ast} - d^{\ast}$称为对偶间隔（duality gap），如果对偶间隔为0，那么我们就称之为强对偶（strong duality），强对偶是一个比较强的约束，KKT条件（Karush-Kuhn-Tucker conditions）是它的一个必要不充分条件，具体的KKT条件表述为以下五个式子：

1. $f_i(\boldsymbol{x}) \leq 0, \; \forall i \in \{1, \cdots, m\}$
2. $h_j(\boldsymbol{x}) = 0, \; \forall j \in \{1, \cdots, n\}$
3. $\lambda_i \geq 0, \; \forall i \in \{1, \cdots, m\}$
4. $\lambda_i f_i(\boldsymbol{x}) = 0, \; \forall i \in \{1, \cdots, m\}$
5. $\nabla_\boldsymbol{x}f_0(\boldsymbol{x}) + \sum^m_{i=1}\lambda_i \nabla_{\boldsymbol{x}}f_i(\boldsymbol{x}) + \sum^n_{j=1}\nu_j \nabla_{\boldsymbol{x}} h_j(\boldsymbol{x}) = 0$
