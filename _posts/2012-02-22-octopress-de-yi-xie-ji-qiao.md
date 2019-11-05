---
layout: post
title:  "Octopress的一些技巧"
date:   2012-02-22 23:24:00
---

写在前面：换到Octopress还没几天，一步一步地配置，一步一步地学习，不得不承认，Octopress不愧是**A blogging framework for hackers.**，期间遇到了很多问题，很是让人头疼，而且可能还是比较小众吧，在搜索引擎中中文的帮助信息相当有限，所以也逼我看英文的文档跟手册，以往看到大段的英文总是头疼，现在也算是适应了吧。顺带提一句，*Stack Overflow*真的很好用，能够有效地获取帮助，*IRC*也是不错的选择，上面的技术牛人很nice的，获取帮助快速有效。还认识了几位靠谱的Geek，也给了我不少的帮助，谢谢啦～

> Octopress is an obsessively designed framework for Jekyll blogging. It’s easy to configure and easy to deploy. Sweet huh?

## Octopress目录结构

```bash
source/
  _includes/    # Main layout partials
    custom/     # <- Customize head, header, navigation, footer, and sidebar here
    asides/     # Theme sidebar partials
    post/       # post metadata, sharing & comment partials
  _layouts/     # layouts for pages, posts & category archives
```

## Octopress相关
生成及发布：

```ruby
rake generate   # Generates posts and pages into the public directory
rake watch      # Watches source/ and sass/ for changes and regenerates
rake preview    # Watches, and mounts a webserver at http://localhost:4000
```
更新Octopress：

```bash
git pull octopress master     # Get the latest Octopress
bundle install                # Keep gems updated
rake update_source            # update the template's source
rake update_style             # update the template's style
```

## Git相关
详见官网的[帮助文档](http://help.github.com/)

## Markdown语法
号称最简单易学的标记语言，在[这儿](http://daringfireball.net/projects/markdown/syntax)可以查看到完整的说明文档，[这儿](http://wowubuntu.com/markdown/)是中文版的。然后还有[这里](http://dillinger.io/)是在线的Markdown编辑器。

## 个性化设置
在Octopress官网的[Theming & Customization](http://octopress.org/docs/theme/)可以查看到详细说明。

在`_config.yml`（这个配置文件的语法是[yaml](http://www.yaml.org/)，有兴趣的可以看看[这篇简介](http://www.ibm.com/developerworks/cn/xml/x-cn-yamlintro/)）中，除了可以修改页面标题、描述之外，一些第三方服务也是支持的，诸如Twitter、Pinboard、Delicious……只需要填入相应的用户名或相关信息就可以在相应位置显示了（注意冒号后面应该留个空格），还可以在这里重新安排它们的位置，创建自定义的侧边栏。

在`source`目录下可以写一个`404.html`，这个就是404页面了。

编辑`/source/_includes/custom/`里的相应文件就可以修改header, footer, navigation了。

添加一个新页面：

```
rake new_page['About']
```
我这里添加了个**about**页面，这会在`source`目录下生成一个`about/index.markdown`，同样是markdown编写，跟文章一样。下面让它显示到导航条中。只要编辑`source/_includes/custom/navigation.html`就行了，编辑之后是这个样子的：
```html
<ul class="main-navigation">
  <li><a href="{{ root_url }}/">Blog</a></li>
  <li><a href="{{ root_url }}/blog/archives">Archives</a></li>
  <li><a href="{{ root_url }}/about">About</a></li>
</ul>
```
