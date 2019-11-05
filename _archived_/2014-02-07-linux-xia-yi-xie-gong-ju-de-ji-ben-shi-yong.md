---
layout: post
title: "Linux下一些工具的基本使用"
date: 2014-02-07 11:22
---
好久没有更新博客了，Evernote 上的笔记都很杂乱，一直没有空整理，过完年了，这几天准备慢慢整理出来几篇。

这篇其实就是笔记而已，都是一些常用的工具，主要是我记性不是很好，每次用都要查这个那个文档的，写下来加深记忆咯（尽量保持更新）。

## git

```sh
git init # 初始化本地代码库
git add . # 加载文件，后面可以是以逗号分隔的多个文件
git commit -m "commit info" # 提交代码到本地仓库
git status # 查询 git 状态

git checkout -b branch_name # 建立分支
git branch # 查看分支
git checkout branch_name # 切换分支
git branch -d branch_name # 删除分支
git merge branch_name master # 合并分支

git clone git_url # 将远程代码库克隆到本地
git remote add origin git_url # 定义远程服务
git fetch origin # 抓取远程代码库的更新
git push origin master # 推送到远程代码库
```

上面只是一些简单的用法，详细的说明可以看[这里](http://git-scm.com)。

## pacman
```sh
# -S, --sync 同步
pacman -Sy # 仅同步源
pacman -Su # 更新系统
pacman -Ss pkg_name # 搜索关于pkg_name的包
pacman -Si pkg_name # 从数据库中搜索包pkg_name的信息
pacman -S pkg_name # 安装包
pacman -Sc # 清理旧包

# -Q, --query 查询
pacman -Q pkg_name # 在本地包数据库搜索指定软件包
pacman -Qdt # 找出孤立的包

# -R, --remove 移除
pacman -R pkg_name # 删除pkg_name包
pacman -Rc pkg_name # 删除pkg_name包和依赖pkg_name的包
pacman -Rsn pkg_name # 删除pkg_name包所有不需要的依赖包并删除其配置文件
```

更加详细的说明参见[这里](https://www.archlinux.org/pacman/pacman.8.html)。

## tar
```sh
tar -cvf tar_file.tar files # 将files文件打包（并不压缩）
tar -xvf tar_file.tar # 解包
```

详情请见[这里](http://www.gnu.org/software/tar/manual/tar.html)。

## sed
```sh
sed 's/Tom/Peter/g' file_name # 将文件file_name中的Tom全部（g）替换成Peter。
sed '/Tom/'d file_name # 删除文件file_name中所有包含Tom的行
sed '3,6d' file_name # 删除文件的第3至第6行。
```
关于 sed 的用法远远不止这些，详细的见[这里](http://www.gnu.org/software/sed/manual/sed.html)。

## awk
```sh
awk -F: # 指定分隔符为":"
awk '/key_word/{print $1"\t"$2}' file_name # 匹配key_word并以一定格式输出相关内容
awk '$2=="Tom"{print $0}' workers # 精确匹配并输出整行
awk 'BEGIN{A=0}{A=A+$1}END{print "A is: "A}' file_name # 因为print是在END之后执行的，所以输出仅有一次
```

关于 awk 同样也有整整一本书的内容，详情请见[这里](http://www.gnu.org/software/gawk/manual/gawk.html)。

## gdb
```sh
gcc -g sourcefile.c # 在编译时加入调试信息

list n, m # 列出从n行到m行的源代码，简写为 l
start # 从程序开始处开始执行程序
run # 从开头开始连续运行程序直到发生中断 ，简写为 r
step # 单步执行（进入函数），简写为 s
next # 单步执行（不进入函数），简写为 n
continue # 运行到下一个断点，简写为 c
finish # 运行到函数返回，并显示返回值
quit # 退出 gdb，简写为 q

backtrace # 查看函数调用的栈帧，简写为 bt
info # 查看相关信息，简写为 i
info locals # 查看所有局部变量的信息
print # 打印变量的值（也可以改变变量的值），简写为 p
display # 指定每次调试时都显示某个变量的值
undisplay # 取消对先前通过display设置的变量的跟踪

info breakpoints # 查看所有断点的信息
delete breakpoints # 删除指定编号的断点
disable breakpoints # 暂时禁用指定编号的断点
watch # 设置观察点，简写为 w
info watchpoints # 查看观察点的信息
```

详情请见[这里](http://www.gnu.org/software/gdb/documentation/)。
