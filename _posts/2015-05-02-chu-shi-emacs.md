---
layout: post
title: "初识Emacs"
date: 2015-05-02
---
Vim用久了想换换口味，习惯了Vim的模式之后Emacs的操作方式一开始真的很难适应，不过新鲜感十足。总的来说Emacs的功能确实强大，[org-mode](http://orgmode.org/)更是相见恨晚，只是作为“编辑器”来说，我还是更偏向于Vim，因为Emacs对“功能键”的使用真的超出了正常人手指的负荷，难怪有人要搞个[编程踏板](https://github.com/alevchuk/vim-clutch)对于Emacs党真是神器啊)出来，不过偶尔用Emacs写写文档什么的还是不错的，尤其是中文文档。

## 简介
安装、配置什么的就不多说了，[主页](http://www.gnu.org/software/emacs/)上面都有，在Emacs符号中，`C-<chr>`表示同时按下Ctrl跟某个键；`M-<chr>`表示同时按下Meta（有时候用EDIT或ALT来标示，也可以按一下Esc再放开以达到同样的效果）跟某个键；`S-<chr>`表示同时按下Shift跟某个键。

## 基础
* `C-g` 终止当前操作
* `C-/` 撤销
* `C-_` 与上一条等价
* `C-x u` 与上一条等价
* `C-u 数字` 数字参数表示重复次数，后面可以接任意操作/输入。
* `M-数字` 与上一条等价。
* `M-x 函数` 执行指定命令，可以Tab补全
* `C-v` 上一屏
* `M-v` 下一屏
* `C-l` 循环将当前光标所在行置于屏幕中、上、下位置
* `M-r` 将光标置于屏幕中间一行

## 帮助
* `C-h ?` 查看帮助
* `C-h f` 查看函数帮助
* `C-h v` 查看变量帮助
* `C-h k` 查看键绑定
* `C-h C-f` 查看函数的信息
* `C-h i` 查看info
* `C-h t` 打开教程

## 编辑
* `C-n/p/b/f` 移动光标到下一行、上一行、前一字符、后一字符
* `M-b/f` 移动光标到前一单词、后一单词
* `C-a/e` 移动光标到行首、行末
* `M-a/e` 移动光标到句首、句末
* `M-</>` 移动光标到文件首、文件末
* `M-g g` 移动光标到某一行
* `C-<SPC>` 可视化模式，用于选中文本
* `C-@` 效果同上（上一条可能会与输入法冲突）
* `C-x h` 选中全文
* `C-x r m` 设置书签
* `C-x r b` 跳到书签处
* `C-s/r` 向前搜索、向后搜索；继续重复该组合键以跳到下一个搜索目标，Backspace跳到上一个搜索目标
* `M-%` 查询替换
* `M-x replace-string` 普通替换
* `Backspace` 删除前一字符
* `C-d` 删除后一字符
* `M-Backspace` 删除前一单词
* `M-d` 删除（剪切）后一单词
* `C-k` 删除（剪切）到行末
* `M-k` 删除（剪切）到句末
* `M-w` 复制选定区域
* `C-y` 粘贴
* `M-y` 循环剪切版内容（必须跟在上一条后）

## 文件
* `C-x d` 目录管理
* `C-x C-f` 查找文件（或创建文件）并打开
* `C-x C-s` 保存
* `C-x C-c` 退出

## 窗格
* `C-x 1` 关闭除了光标所在窗格外所有窗格
* `C-x 2` 垂直拆分窗格
* `C-x 3` 水平拆分窗格
* `C-x 0` 关闭当前窗格
* `C-x o` 选择下一个窗格
* `C-M-v` 滚动下一个窗格
* `C-x ^` 增高当前窗格
* `C-x {` 将当前窗格变窄
* `C-x }` 将当前窗格变宽
* `C-x -` 如果窗口比缓冲大就缩小
* `C-x +` 所有窗口一样高

## 缓冲区
* `C-x C-b` 列出缓冲区列表
* `C-x b` 切换缓冲区
* `C-x k` 关闭当前缓冲区
* `C-x s` 保存多个缓冲区

## Org Mode
> Org mode is for keeping notes, maintaining TODO lists, planning projects, and authoring documents with a fast and effective plain-text system.

正因为功能强大，[org-mode](http://orgmode.org/)的内容实在是太多了，我就记录下常用的一些操作，更详细的可以看官网上完整的[教程](http://orgmode.org/org.html)。

```
#+STARTUP: showall
#+STARTUP: hidestars
#+TITLE: Document Title
#+OPTIONS: toc:nil
* Top level title
** Unordered List
- *bold*
- /italic/
- _underlined_
- =code=
- ~verbatim~
- +strike-through+
[[http://google.com/][Google]]

** Ordered List
1. [-] Task 1 [%]
   1. [X] sub task 1
   2. [ ] sub task 2
   3. [ ] sub task 3
2. Task 2
3. Task 3

** GTD
Some descrption here.[fn:1]
*** [#A] Task 1 						       :work:
*** [#B] Task 2 [/] 						      :study:
**** DONE sub task 1
**** DONE sub task 2
**** TODO sub 
*** TODO Task 3							       :work:
SCHEDULED: <2015-05-06 周三>
*** TODO Task 4							      :study:
DEADLINE: <2015-05-21 周四>

** Math
Inline equation: $a^2 + b^2 = c^2$ and then:
$$a^2 + b^2 = c^2$$

** Tables
#+CAPTION: Table Name
| Name   | Price | number | Total |
|--------+-------+--------+-------|
| Apple  |  1.20 |      2 |   2.4 |
| Banana |  1.30 |      3 |   3.9 |
| Orange |  1.10 | 4      |   4.4 |
#+TBLFM: $4=$2*$3

** Babel
#+BEGIN_SRC emacs-lisp
(+ 1 2 3)
#+END_SRC

#+RESULTS:
: 6

* Footnotes

[fn:1] footnote here
```

### 标题
* `S` 展开/折叠章节
* `S-<TAB>` 展开/折叠所有章节
* `C-c C-n` 下一标题
* `C-c C-p` 上一标题
* `C-c C-f` 下一同级标题
* `C-c C-b` 上一同级标题
* `C-c C-u` 回到上层标题
* `M-<LEFT>/<RIGHT>` 升/降级标题
* `M-S-<UP>/<DOWN>` 上/下移子树
* `C-c /` 根据提示创建稀疏树

### 列表
* `M-<RET>` 插入同级列表项
* `M-<LEFT>/<RIGHT>` 改变列表层级关系
* `M-<UP>/<DOWN>` 上下移动列表项
* `M-S-<RET>` 插入有checkbox的同级列表项

### 表格
可以通过输入`|文字|文字|<TAB>`的方式来插入表格，通过输入`|-<TAB>`来插入水平线。

* `C-c |` 通过输入大小的方式插入表格
* `C-c C-c` 调整表格
* `<TAB>` 切换到下一区域
* `<RET>` 切换到下一行
* `C-c <RET>` 在下面添加一个水平线
* `C-c ^` 排序，以当前位置所在的列作为依据
* `M-<UP>/<DOWN>/<LEFT>/<RIGHT>` 移动行/列
* `M-S-<UP>/<LEFT>` 删除行/列
* `M-S-<DOWN>/<RIGHT>` 插入行/列
* `=$2*$3` 表格中的数学计算
* `C-u C-c C-c` 强制为整个表格进行计算

### GTD
* `C-c C-t` 变换TODO状态
* `S-<LEFT>/<RIGHT>` 效果同上
* `C-c C-c` 改变checkbox状态
* `C-c ,` 设置优先级
* `S-<UP>/<DOWN>` 增减优先级
* `M-S-<RET>` 插入同级TODO标签
* `C-c C-q` 添加标签
* `C-c .` 插入时间戳
* `C-c C-s` 插入带“SCHEDULED”的时间戳
* `C-c C-d` 插入带“DEADLINE”的时间戳

### 代码
输入`<`后面跟一个字母，然后按`<TAB>`键，就可以生成对应的模板。（eg: `< s <TAB>`），在完成代码后按`C-c C-c`可以执行代码并插入运行结果。

```
s	#+BEGIN_SRC ... #+END_SRC
e	#+BEGIN_EXAMPLE ... #+END_EXAMPLE
q	#+BEGIN_QUOTE ... #+END_QUOTE
v	#+BEGIN_VERSE ... #+END_VERSE
c	#+BEGIN_CENTER ... #+END_CENTER
l	#+BEGIN_LaTeX ... #+END_LaTeX
L	#+LaTeX:
h	#+BEGIN_HTML ... #+END_HTML
H	#+HTML:
a	#+BEGIN_ASCII ... #+END_ASCII
A	#+ASCII:
i	#+INDEX: line
I	#+INCLUDE: line
```



### 其他
* `C-c C-l` 插入链接
* `C-c C-o` 打开链接
* `C-c C-x f` 插入注脚
* `C-c C-e` 导出

-----

- [一年成为Emacs高手(像神一样使用编辑器)](https://github.com/redguardtoo/mastering-emacs-in-one-year-guide/blob/master/guide-zh.org)
- [Aaron Bedra的Emacs配置](http://www.aaronbedra.com/emacs.d/)
- [Steve Purcell的Emacs配置](https://github.com/purcell/emacs.d)
- [How I use Emacs and Org-mode to implement GTD](http://members.optusnet.com.au/~charles57/GTD/gtd_workflow.html)
- [The Org Manual](http://orgmode.org/org.html)
- [The compact Org-mode Guide](http://orgmode.org/guide/)
- [Org-mode 简明手册](http://www.cnblogs.com/Open_Source/archive/2011/07/17/2108747.html)
