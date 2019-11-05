---
layout: post
title: "Emacs Tips and Tricks"
date: 2015-06-12
---
I'm a Emacs newbie from Vim (I don't give vim up and I use [Evil](http://www.emacswiki.org/emacs/Evil) in Emacs). After using Emacs for about two months, I find it is as powerful as Vim. Below are some tips and tricks I find very useful.

## Format source code
Press `C-x h` to highlight the whole page and press `C-M-\` to format the whole buffer. Or you can use the `aggressive-indent` package to do it automatically. Besides, I use [AucTex](https://www.gnu.org/software/auctex/) to write $\LaTeX$. I usually press `C-c C-q C-s` to reformat the whole buffer.

## Preview Latex
Press `C-c C-p C-s` to preview a region of your paper.

## Jump out of the parentheses
[Smartparens](https://github.com/Fuco1/smartparens) or [yasnippet](https://github.com/capitaomorte/yasnippet) are great tools. They can complete the parentheses. When you complete your input, just press `C-f` to jump out of the parentheses. (Actually it's the emacs-way 'move forward')

## Run or return
`C-m` is bound to `RET` so it's another way to hit RETURN (In another word, you can replace RET with it). `C-j` is just RUN it. Let's take an example. When you use [IDO](http://emacswiki.org/emacs/InteractivelyDoThings) or [Smex](https://github.com/nonsequitur/smex), they will automatically complete your input, you can press `C-j` to stick into your input and reject the autocompletion. While `C-m` or `RET` will run the autocompletion command.
