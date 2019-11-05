---
layout: post
title:  "Migrate from Wordpress to Octopress"
date:   2012-02-21 19:26:00
---
引子：本来不打算把Wordpress上的文章导入过来了，想在这儿重新开始，之前的那些文章不看也罢，没啥意思，不过昨天不知道中了什么邪（强迫症犯了吧），就想导入试试。导入的过程并没有我想象中的那么简单，遇到了点小麻烦，不过最终还是解决了。

> Octopress是个好东西，不过要是图片很多的话，可能Tumblr会更合适你。

## 导出Wordpress内容
这个没有难度，在`http://yourdomain/wp-admin/export.php`根据提示导出内容就可以了会得到一个xml文件。

## 转换xml
不妨把得到的xml文件重命名为wordpress.xml，然后到[这儿](https://gist.github.com/1274521)下载导出脚本（无意中发现作者的id——ikbear好熟悉的样子，如果没猜错的话，应该就是[何李石](http://www.helishi.net)童鞋啦），不妨重命名为migrate.rb，再把wordpress跟migrate.rb都放到`～/octopress/source/_post`下（octopress是我的Octopress所在位置），然后再进行如下操作：
```shell
cd ~/octopress/source/_post
ruby migrate.rb wordpress.xml
```
这儿报错了，提示：
```ruby
<internal:lib/rubygems/custom_require>:29:in `require': no such file to load -- ya2yaml (LoadError)
	from <internal:lib/rubygems/custom_require>:29:in `require'
	from wordpress.rb:5:in `<main>'
```
原因是缺少了一个包，可以这样安装：
```shell
gem install ya2yaml
```
然后再到之前的目录执行脚本，发现还是不行，报错：
```shell
/home/isaac/.rvm/rubies/ruby-1.9.2-p290/lib/ruby/1.9.1/rexml/parsers/baseparser.rb:412:in `block in pull': Undefined prefix atom found (REXML::UndefinedNamespaceException)
```
这应该是那个xml文件的问题了，纠结了一会儿，Google了一番，未果，尝试修改那个xml文件，删除某一行：`<atom:link rel='hub' href='http://heyisaac.blog.com/?pushpress=hub'/>`，之后再运行脚本就行了，成功之后`_post`目录下会生成一个`_post`目录，里面就是Wordpress上的文章了。

## 善后工作
先简单整理一下：
```shell
cd ~/octopress/source/_post
mv _post/* .
rmdir _post && rm wordpress.xml migrate.rb
```
生成的是一些`.textile`文件，需要进行改造，工程量还是挺大的，文章的链接、图片的路径……都要修改一下。就我自己的情况来说的话倒不是很复杂，因为之前的博客质量确实很低，这次我索性删了很多文章，中二文，还有那些没有啥营养牢骚，还有那种全是图片的，统统都删除了。说实话颜文字什么的导致各种各样的问题，排版变得一塌糊涂，索性全删了。

## 写在最后
昨天又犯懒了，自己不想动手了，邮件了[肖之慰](http://xoyo.name/)童鞋，想让他帮我处理一下那个xml文档，本来很简单嘛，就一个命令，可是他说帮我弄了就没意思了，只能帮我分析下那些错误，呵呵，“授人以渔不如授人以鱼”，还是谢谢他。
