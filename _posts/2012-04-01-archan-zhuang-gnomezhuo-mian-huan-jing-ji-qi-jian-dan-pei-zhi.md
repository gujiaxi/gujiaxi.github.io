---
layout: post
title:  "Arch安装Gnome桌面环境及其简单配置"
date:   2012-04-01 19:58
---
> Arch Linux is what you make it.

前一篇文章写了安装Arch的基本系统，当然，相信很多人都不会接受总是黑乎乎的屏幕，正如我的舍友吼道：**尼玛这是一种退化！！！**好吧，还是把桌面环境装上吧，我选择了Gnome，当然你可以选择其他的DE比如说KDE，Xfce，E17，LXDE…… because you make it!

## 基础知识
* [AUR](https://wiki.archlinux.org/index.php/AUR)(ArchLinux User-community Repository)是Arch社区用户的软件仓库，它是Arch的灵魂所在。
* [pacman](https://wiki.archlinux.org/index.php/Pacman)是Arch的包管理工具，你可以`man pacman`或者看看[pacman常用命令](https://www.evernote.com/shard/s96/sh/3f4517a0-89b8-4626-baaf-5a77090609c5/c13d3184f3ea10b12f5dc62f8da0238c)。

## 添加普通用户
先不管其他的，加一个普通用户再说，并把它放入到相应的组中（如果希望交互，可以输入`adduser`来添加普通用户），各个组的介绍在wiki上都有，有兴趣的可以去看一下：
```sh
useradd -m -g users -G audio,lp,optical,storage,video,wheel,games,power,scanner -s /bin/bash isaac
```

最后一个是你的用户名，我写的是我的名字。接下来安装*sudo*：
```sh
pacman -S sudo
```

然后让刚才创建的那个普通用户使用sudu，输入`visudo`，其实就是打开并编辑`/etc/sudoers`这个文件（不过不建议直接用vi或者nano打开它）。把下面这一行开头的注释去掉就行了（刚才创建用户的时候已经把他放到了wheel组中），以后就可以在普通用户登录的情况下使用sudo来临时获取root权限了（后面的操作可能要获取权限，该加sudo的地方记得加上sudo，关于权限问题我就不赘述了）：
```
%wheel	ALL=(ALL) ALL
```

## 安装X
这个是绝对必要的，直接pacman就可以了：
```sh
pacman -S xorg-server xorg-xinit xorg-utils xorg-server-utils
```

如果需要3D支持的话可以另外再安装*mesa*、*mesa-demos*这两个包。

## 安装显卡驱动
这个部分比较麻烦，可能看着简单，实际拿自己机子做了会发现很多问题。首先`lspci|grep VGA`查看一下自己的显卡情况，然后根据自己的情况选择显卡驱动（开源的或者闭源的）。我的是ati的显卡（其实其他显卡可能还容易配置一点，ati显卡驱动的麻烦是出了名的），可以选择开源驱动（xf86-video-ati）或者闭源的[ATI Catalyst](https://wiki.archlinux.org/index.php/ATI_Catalyst)，我没有尝试开源驱动（虽然#archlinux跟#linux里很多人都劝我换开源驱动），还是固执地选择了[ATI Catalyst](https://wiki.archlinux.org/index.php/ATI_Catalyst)。

在我安装的时候Catalyst的版本是12.2，它不支持xorg-server 1.12版本，所以必须先得把xorg-server的版本降到1.11，在`/etc/pacman.conf`添加软件源：
```conf
[catalyst]
Server = http://catalyst.apocalypsus.net/repo/catalyst/$arch
[xorg111]
Server = http://catalyst.apocalypsus.net/repo/xorg111/$arch
```

注意，这个`xorg111`的源一定要放在`extra`源之前。然后更新数据库并“升”级xorg-server（应该会提示版本问题，要求确认，yes就行了）：
```sh
pacman -Syu
```

然后安装*catalyst-utils*跟*catalyst*软件包（如果提示包冲突，移除*libgl*，确认就行了）
```sh
pacman -S catalyst-utils catalyst
```

如果还是有烦人的依赖问题，就先把*libgl*忽略依赖关系地删除：
```sh
pacman -Rdd libgl
```

装上了*catalyst-utils*跟*catalyst*之后，再运行一下`aticonfig --initial`，这会生成`/etc/X11/xorg.conf`文件，应该会报一个*PowerXpress*的错误，这个跟显卡切换有关，目前貌似还相当不成熟，我是在BIOS里把显卡切换关了只用独立显卡的。最后打开`/boot/grub/menu.lst`，加上`nomodeset`：
```
kernel /boot/vmlinuz-linux root=/dev/sda6 ro nomodeset
```

## 安装输入设备驱动
我要一个[synaptics](https://wiki.archlinux.org/index.php/Synaptics)的触摸板驱动：
```sh
pacman -S xf86-input-synaptics
```

配置文件在`/etc/X11/xorg.conf.d/10-synaptics.conf`相应的可以查看[synaptics](https://wiki.archlinux.org/index.php/Synaptics)的wiki页面，不过默认就已经挺强大的了。最后别忘了在`/etc/rc.conf`里边儿的*DAEMONS*中加入*synaptics*。

## 安装dbus
这个基本也是必备的：
```sh
pacman -S dbus
```

可以运行`rc.d start dbus`来启动它。同样，在`/etc/rc.conf`里边儿的*DAEMONS*中加入*dbus*。

## 安装gnome
著名的gnome桌面环境，分*gnome*、*gnome-extra*两个包，当然只安装*gnome*这个包其实就可以了，不过没有关系，都装上好了，以后可以再删的：
```sh
pacman -S gnome gnome-extra
```

## 进入gnome
创建一个`～/.xinitrc`文件，内容如下：
```
exec ck-launch-session gnome-session
```

这样就可以输入`startx`来进入gnome了，如果想要开机的时候直接进入gnome,可以打开`/etc/inittab`文件，修改下面几个地方：
```
# Boot to console
#id:3:initdefault:
# Boot to X11
id:5:initdefault:

x:5:respawn:/usr/sbin/gdm -nodaemon
```

## 安装软件
首先，先安装一下*yaourt*，不然软件数量是远远达不到我们的需求的，最简单的方法就是把下面这个源加入到`/etc/pacman.conf`中（64位系统的话把`i686`改成`x86_64`）：
```conf
[archlinuxfr]
Server =http://repo.archlinux.fr/i686
```

然后pacman一个*yaourt*就行了，yaourt的用法跟pacman基本一样。注意，之前如果没有安装*base-devel*软件包的话用*yaourt*编译部分软件的时候可能会报错，建议把*base-devel*这个包装上。

* 安装字体，我选择的是*ttf-dejavu*跟*wqy-microhei*（文泉译微米黑），你也可以选择其他的。
* 安装输入法，*ibus*跟*ibus-pinyin*这两个包，一个是框架，一个是引擎，如果需要五笔输入也可以安装对应的。
* 安装flash插件*flashplugin*。
* 关于解压缩，安装*p7zip*这个包。
* 安装解码器*gstreamer0.10-plugins*，默认的totem（当然你也可以把它换成其他的）播放器需要解码器。
* 安装网络配置工具*network-manager-applet*，然后再改一下`/etc/rc.conf`里面的*DAEMONS*，在*network*前面加`!`，再在后面加一个*networkmanager*：
	  DAEMONS=(hwclock syslog-ng !network acpid netfs crond dbus synaptics networkmanager)
* 安装聊天软件empathy（当然你也可以把它换成pidgin)必要的后端*telepath*。
* 安装浏览器*firefox*（当然你也可以选择*chromium*），默认的那个太简单了。
* 安装办公软件，我安装的是*libreoffice*这个包，你也可以选择其他的，我还安装了一个*hunspell-en*包用来对输入（英文）进行拼写检查的。
* 安装修图软件*gimp*，算是linux下的ps吧。
* 安装gnome配置的工具*gnome-tweak-tool*。
* 安装图标主题，我用的是*faenza-icon-theme*，还是很漂亮的，安装之后记得用gnome-tweak-tool选择它就行了。
* 创建home目录下的一些基础文件夹，安装*xdg-user-dirs*这个包会自动在home目录下创建漂亮的常用文件夹。
* 安装*openssh*，用来连接ssh，当然对于大陆的同学来说，可以“爬墙”（提到这个，aur里面还有一个`gstm`包可以提供GUI）。
* 安装游戏，这里推荐两个比较轻量、有内涵的游戏：*braid*、*mari0*。
* 安装*git*、*vim*、*jdk*、*dropbox*、*skype*，这些看个人喜好吧。

## 其他设置
基本的已经差不多配置完毕了，下面的这些配置主可以自由发挥，每个人都不一样，我只是写一下作为参考。

* 如果之前有装*gnome-extra*这个包的话可能默认会安装上一些扫雷、贪吃蛇之类的游戏，把*gnome-games*跟*gnome-games-extra-data*删了就清净了，当然还有一些其他的如果不喜欢也可以删除对应的包。
* gnome3默认窗口是没有最大（小）化按钮的，如果需要可以使用gnome-tweak-tool工具设置显示。如果想把最大（小）、关闭按钮放到左边，只需要打开`gconf-editor`一次进入`desktop->gnome->shell->windows`，将其中的`:minimize,maximize,close`改成`close,maximize,minimize:`，看明白了吗？还可以改顺序。
* 设置开机启动的程序：
```sh
gnome-session-properties
```
* 如果安装*libreoffice*的时候你没注意的话，可能现在会发现语言有问题（默认是Afrikaans），换个语言包就行了（汉语是*libreoffice-zh-CN*这个包）：
```sh
pacman -S libreoffice-en-US
pacman -R libreoffice-af
```
