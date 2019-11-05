---
layout: post
title: "Linux内核的编码风格"
date: 2014-11-26
---
缘起[这篇文章](https://www.kernel.org/doc/Documentation/CodingStyle)，整理一下Linux内核的编码风格（基本上是C语言的风格）。不过就像文中所说的，编码风格是极私人的，无意要每个人都遵守某种风格。

## 缩进
缩进是8个字符的Tab（注意是1个8个字符长度的Tab而不是8个空格），这可能跟大部分人的习惯不一样，大部分人可能习惯4个（或者2个）字符的缩进，他们的理由是如果缩进太多的话一行写不了多少就到屏幕边缘了。但是！如果你整天对着满屏幕的代码的话，那么就会发现更多的缩进能使代码更易读，而且如果发现代码嵌套太多层（这就是很快就到屏幕边缘的原因）你就得好好考虑你的代码了。

`swith`中的代码缩进通常是让`switch`跟`case`对齐：

```c
switch (suffix) {
case 'G':
case 'g':
		mem <<= 30;
		break;
case 'M':
case 'm':
		mem <<= 20;
		break;
case 'K':
case 'k':
		mem <<= 10;
		/* fall through */
default:
		break;
}
```

不要把多行代码放在一行上，除非你想要隐藏什么东西：

```c
if (condition) do_this;
		do_something_everytime;
```

## 花括号
花括号一直以来争论都比较大，主要纠结的是：左花括号该不该换行。

K&R (Kernighan & Ritchie)倡导的括号风格是这样的：如果是函数的左花括号，则换行；如果是非函数（如`if`, `switch`, `for`, `while`, `do`……）的左花括号，则不换行。还有，对于右花括号，一般是独占一行，除非后面接着的还是语句的一部分（如do语句中的`while`，还有if语句中的`else`）。概括起来如下：

```c
int power(int x, int y)
{
		int result;

		if (y < 0) {
				result = 0;
		} else {
				do {
						result += x;
						x--;
				} while (x > 0); 
		}
		return result;
}
```

这样起到了压缩代码长度的效果，此外，如果是单独的语句，就不用加花括号，但是也不一定，看下面的例子

```c
if (condition)
		do_this();
else
		do_that();

if (condition) {
		do_this();
		do_that();
} else {
		otherwise();
}
```

## 空格
下列关键词后应接空格：`if switch case for do while`……

下列关键词后不应接空格：`sizeof typeof alignof __attribute__`……

二元操作符前后加空格：`=  +  -  <  >  *  /  %  |  &  ^  <=  >=  ==  !=  ?  :`……

一元操作符后不应该加空格： `&  *  +  -  ~  !`……

此外，在定义指针的时候，`*`应紧跟数据名称：`char *linux_banner`。

## 命名
C是一种斯巴达式(Spartan)语言，所以命名也应该是斯巴达式的，遵循的准则是简洁易懂，如`tmp`，而不是`ThisVariableIsATemporaryCounter`。

全局函数是个特例，它需要一定的描述性，所以用`count_active_users()`而不要用`cntusr()`。

把变量类型放到变量名里面（所谓的匈牙利式）不是一种明智的命名风格，因为编译器本来就能知道变量类型，这么做只能让程序员更困惑。

本地变量应该尽量简短并且明确，比如在循环里面的计数变量，用`i`比`loop_counter`要好得多，类似的还有`tmp`来表示一些暂存变量。

## Typedef
尽量减少代码中的`typedef`，想想下面两行那个更清楚：

```c
vps_t a;
struct virtual_container *a;
```

很多人都觉得typedef能够增强代码的可读性，其实不然，只有在下列情况才推荐用typedef:

1. 完全不透名的对象。也就是说用typedef刚好可以把他们隐藏起来。

2. 确定的整型。用typedef可以不用关心到底是`int`还是`long`。

3. 避免拼写错误而创建一个新的类型。

4. 跟标准C99一致的类型。所以一般是`u32`而不是`uint32_t`。

5. 为了避免重名。

## 函数
函数应尽量简短且优美（sweet），始终遵循Linux哲学：*Do one thing and do that well.*

函数长度应保持在一到二屏之内（ISO/ANSI的屏幕尺寸为80*24），仔细想想也是，如果太长了就说明函数太复杂，可以考虑分拆到子函数。

函数中出现的本地变量不应超过5~10个，否则你就得考虑这个函数的写法了（人的大脑基本上同时只能追踪七个不同的东西）。

## goto
很多人都被老师跟教科书吓怕了，以至于从来没用过这个下手狠、见效快的函数，其实不必刻意避开她。如果函数中存在多处可能退出的情况，并且在退出前都需要做相同的清理工作（比如说`socketclose()`），那么就可以用`goto`。

```c
int fun(int a)
{
		int result = 0;
		char *buffer = kmalloc(SIZE);

		if (buffer == NULL)
				return -ENOMEM;

		if (condition1) {
				while (loop1) {
						...
				}
				result = 1;
				goto out;
		}
		...
out:
		kfree(buffer);
		return result;
}
```

goto能带来的好处是这样的：

* 整个流程更容易被理解
* 减少了多层嵌套
* 避免了在修改时候因为没有更新某个退出的点而发生错误
* 减轻了编译器的工作，去掉了一些冗余的代码

## 注释
准则就是：*You want your comments to tell WHAT your code does, not HOW.*

Linux使用C89的`/* ... */`风格，而不是C99的`// ...`风格。
