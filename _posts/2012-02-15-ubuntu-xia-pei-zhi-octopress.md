---
layout: post
title:  "Ubuntu下配置Octopress"
date:   2012-02-15 00:24:58
---
> First, I want to stress that Octopress is a blogging framework for hackers. You should be comfortable running shell commands and familiar with the basics of Git. If that sounds daunting, Octopress probably isn’t for you.

关于[Octopress](http://octopress.org)，简单来说，就是一套基于Jekyll的静态博客站点生成系统。相对于Wordpress来说它有一些非常独特的优点：

1. 使用静态页面，免去了数据库的操作；
2. 像编程一样写博客，可以挑选自己惯用的文本编辑器写文章；
3. 使用[markdown](http://daringfireball.net/projects/markdown/)标记语言编写文章，易读易写；
4. 与git紧密集成，方便管理；
5. 书写->生成->(预览)->部署，简单、稳定、高效。

## 写在前面
就像Octopress在网站上写的那样，开始之前，要强调一下：Octopress是一套为黑客准备的博客框架，你应该要掌握一些shell命令，并且熟悉Git的一些基本操作，如果这已经吓到你了，那Octopress可能不适合你。

依我看吧，其实只要有一颗爱折腾的心就行了。命令的话只要会一个就行了，`man`嘛。好了,废话不多说，让我们开始吧。

其实官方就有很友好的[Octopress配置指导](http://octopress.org/docs/setup/)，如果你按照上面说的一步一步做的话理论上是可以实现的，不过……之后我发现没那么简单，遇到了很多问题，这篇文章记录下了我配置的全过程以及期间遇到的种种麻烦，基于Ubuntu 11.04，如果你是其他的系统，方案可能有所不同（多说一句，如果是Windows用户的话，看到这儿就可以了，因为这篇文章可能对你没有多大的帮助）。
## 配置本地环境
安装curl、git

```sh
sudo apt-get install curl git-core
```

安装RVM(Ruby Version Manager)

```sh
bash -s stable < <(curl -s https://raw.github.com/wayneeseguin/rvm/master/binscripts/rvm-installer)
```

将rvm指令变成shell function

```sh
echo '[[ -s "$HOME/.rvm/scripts/rvm" ]] && . "$HOME/.rvm/scripts/rvm"'>>~/.bashrc
```

完毕之后再运行

```sh
type rvm | head -1
```

如果显示`rvm is a function`就基本安装完毕了。

## rvm下安装Ruby 1.9.2, RubyGems
先安装ssl跟zlib，再安装Ruby，zlib如果没法儿下载的话，手动在[这儿](http://zlib.net)下载之后解压到`~/.rvm/src`目录即可。

```sh
rvm pkg install openssl
rvm pkg install zlib
rvm install 1.9.2
rvm use 1.9.2
rvm rubygems latest
```

再确认一下版本

```sh
ruby --version
```

至此，本地的环境就配置的差不多了，接下来就是Octopress跟Git的事情了。

## 配置本地的Octopress
下载octopress并切换到octopress目录中（目录名称随意，我这儿就用octopress了）

```sh
git clone git://github.com/imathis/octopress.git octopress
cd octopress
gem install bundler
bundle install
rake install
```

至此，本地的Octopress就差不多了。

## 建立本地Octopress到GitHub的联系
注册一个[GitHub](http://github.com)帐号，然后新建一个Repository，Repository的项目名称写`yourusername.github.com`，例如你的用户名是jack，那就将Repository命名为jack.github.com。

回到终端，输入：

```sh
[[ -f ~/.ssh/id_rsa.pub ]] || ssh-keygen -t rsa
```

按照提示一路确认，生成密钥，然后到[这儿](https://github.com/account/ssh)把密钥粘贴上去，Title没有必要填写。相关的帮助信息可以在[这里](http://help.github.com/mac-set-up-git/)看到。然后运行：

```sh
ssh -T git@github.com
```

第一次连接应该会需要确认，输入`yes`就可以了。然后出现*Hi yourusername! You've successfully anthenticated, but GitHub does not provide shell access.*。这样就可以了。

设定GitHub Pages

```sh
rake setup_github_pages
```

执行后会要求输入`read/write url for repository ：`输入`git@github.com:yourusername/yourusername.github.com.git`就行了。(其中的yourusername就是你的Github用户名，也就是上面例子中的jack)

好了，基本差不多了，写一篇文章测试一下：

```sh
rake new_post["test"] 
```

这会在`myblog/source/_post`下生成一个`*.markdown`文件，编辑文章即可。

生成、预览

```sh
rake generate
rake preview
```

在4000端口预览生成的内容，本地 http://127.0.0.1:4000 就可以看到效果了。

发布到GitHub上

```sh
rake deploy
```

OK，尝试浏览一下`http://yourusername.github.com`（其中的yourusername是你的GitHub用户名，还是那个jack）

最后，將 source 也加入 git

```sh
git add .
git commit -m 'initial source commit'
git push origin source
```
