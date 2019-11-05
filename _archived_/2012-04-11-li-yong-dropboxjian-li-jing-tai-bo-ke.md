---
layout: post
title:  "利用Dropbox建立静态博客"
date:   2012-04-11 09:47
---
Jekyll什么的太高深了？对于很多人似乎是的，至少跟傻瓜式的wordpress来说是这样的。不过静态博客对于wordpress等的优势还是很明显的，至少对于个人博客是这样子的，可能很多人都想尝试下静态博客而又不想太费神，通过下面的几个方法，应该会轻松不少。

## calepin.co
> Publishing for writers who love Markdown and Dropbox

基于*Dropbox*来发布更新，好处是你在哪儿都能写博客，因为只要能把文档修改同步过去就行了。评论是*Disqus*，只要把名字填上就行了，还可以显示Twitter的头像跟folow按钮，同样只要把用户名填上就行了，很简单吧。语法的话支持*markdown*，就是这么简单，其他的工作都不用你管，不需要任何命令行的操作，具体的情况可以看看[官网](http://calepin.co/)的介绍，指南可以看看[这里](http://jokull.calepin.co/calepin-guide.html)，同样是一个示范站点，博客的基础样式应该就差不多是这样的（小清新风格哦～），[这里](http://alberto.calepin.co/automate-posting-in-wordpress-from-calepin-using-ifttt.html)还有一篇教你用*ifttt*来同步文章到wordpress的。

## scriptogr.am
> A simple online tool that converts static Markdown text files located in your Dropbox, into a beautiful blog.

同样基于Dropbox，简单的方式完成复杂的操作，风格同样是简洁清新，没有什么多说的，按照[官网](http://scriptogr.am/)的指南做就行了，

## dl.cuoluo.me
由[易冰](http://twitter.com/lamengao)童鞋制作的一个小工具，仅仅是一个*nginx*配置文件。用法的话看[这里](http://www.v2ex.com/t/24961)。

1. 在你的Dropbox中的Public目录下新建一个名为 cuoluo 文件夹。
那么你现在就可以通过*http://dl.cuoluo.me/[your_dropbox_user_id]*来访问这个文件夹的内容。注意把括号中的内容换成你的dropbox用户id。（注：这里的用户id可以点自己*Public*目录下的任意文件，然后点*Copy public link*，*http://dl.dropbox.com/u/*后面的那传数字就是你的id。）

2. 你也可以使用自定义的网址。
首先访问*http://dl.cuoluo.me*，输入你的id和要绑定的域名。这里假定你要绑定的域名为"lamengao"。然后到你的Public目录下新建一个名为*cuoluo_lamengao*的文件夹。现在你就可以通过*http://dl.cuoluo.me/lamengao*访问你的那个文件夹。

小提示：*http://dl.cuoluo.me/lamengao*可以直接定向到*http://dl.cuoluo.me/lamengao/index.html*
