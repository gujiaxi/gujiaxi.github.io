---
layout: post
title: "Archlinux下搭建Android开发环境"
date: 2012-06-27 08:28
---
关于java环境的安装就不多说了，可以用aur里面的jdk，也可以用extra仓库里的openjdk，直接pacman就行了，然后eclipse的安装也是只要pacman就行了（arch就是这点方便）。下面主要说下android sdk相关的安装设置。

其实[arch wiki](https://wiki.archlinux.org/index.php/Android)写得很清楚，可以直接参考上面的来。

## 安装SDK
这里可以手动安装也可以直接用源里打包好了的。我比较懒，就直接用源里的了。

	yaourt -S android-sdk android-sdk-platform-tools

这样默认安装位置应该在`/opt/android-sdk`，当然，现在还没有安装android平台，运行：

	cd /opt/android-sdk/tools/
	sudo ./android

弹出Android SDK Manager，选择相应的平台进行安装，因为可能比较大，所以得稍等一会儿。

## 配置Eclipse
同样，aur里也有打包好了的：

	yaourt -S eclipse-android

当然你也可以通过eclipse的插件管理来进行安装，不过我还是比较推荐直接安装打包好了的，因为这样可以自动处理依赖关系。好了，安装完毕之后启动eclipse，不出意外应该会有android开发的提示出现，按着做就行了。
