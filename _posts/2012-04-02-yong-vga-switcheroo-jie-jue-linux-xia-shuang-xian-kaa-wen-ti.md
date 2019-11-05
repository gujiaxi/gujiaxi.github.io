---
layout: post
title:  "用vga_switcheroo解决Linux下双显卡问题"
date:   2012-04-02 00:08
---
兴奋啊！Linux双显卡的问题困扰我太久了，今天总算是解决了，以前一直寄希望于闭源的ATI Catalyst，但是它一次又一次地让我失望，各种问题，就算去#linux求助也基本无解，都建议换开源驱动。但是温度的问题也得考虑啊，而且夏天快来了，我这本子散热本来就不怎么好，要是开源的ati驱动的话那不得烫死。终于，感谢[右京样一](http://ukyoi.wordpress.com/)童鞋的[这篇文章](http://ukyoi.wordpress.com/2012/03/14/%E7%94%A8vga_switcheroo%E5%9C%A8linux%E4%B8%8B%EF%BC%88%E5%BC%80%E5%90%AFkms%EF%BC%89%E5%BD%BB%E5%BA%95%E5%85%B3%E9%97%AD%E6%9F%90%E4%B8%80%E5%8F%AF%E5%88%87%E6%8D%A2%E6%98%BE%E5%8D%A1%E7%9A%84/)，让我的本本可以清凉一夏了～

*vgaswitcheroo*是内核提供的组件，但只有在KMS开启状态下才用，这点需要注意。

因为之前安装的是闭源的Catalyst，先得把它们（*catalyst*跟*catalyst-utils*这两个包）卸载了，卸载的时候会提示依赖问题，加上`-d`参数忽略即可，删除之后把*libgl*（之前安装闭源驱动的时候删除了这个包）这个包装上：

```shell
pacman -Rdd catalyst
pacman -S libgl
```

因为当初闭源驱动依赖xorg-server 1.11的原因，所以一直用的是xorg-server 1.11，现在把`/etc/pacman.conf`里面的[xorg111]跟[catalyst]两个源都删除好了。然后运行`pacman -Syu`让xorg-server更新到最新。然后把开源的intel、ati驱动都装上：

```shell
pacman -S xf86-video-intel xf86-video-ati
```

把当初用`aticonfig`生成的xorg.conf删除：

```shell
sudo rm /etc/X11/xorg.conf
```

如果到下一步发现对应文件不存在，请在`/etc/fstab`最后加上一行后重启：

```shell
debugfs /sys/kernel/debug debugfs defaults 0 0
```

输入：

```shell
cat /sys/kernel/debug/vgaswitcheroo/switch
```

可以看到结果类似于：

```
0:IGD:+:Pwr:0000:00:02.0
1:DIS: :Off:0000:01:00.0
```

“IGD”表示集成显卡，“DIS”表示独立显卡；加号（“+”）表示当前用作输出（或称“连接上”（connected））的显卡；“Pwr”代表正在供电，“Off”代表已关闭。如果看到两个显卡都显示“Pwr”，则说明都在消耗着电能。

接下来输入`su`切换到root（不能用sudo替代）。通过向`/sys/kernel/debug/vgaswitcheroo/switch`这个文件发送对应的指令就能对显卡进行控制了：

```shell
echo ON > /sys/kernel/debug/vgaswitcheroo/switch    # 给所有显卡加电
echo IGD > /sys/kernel/debug/vgaswitcheroo/switch   # 切换到集成显卡
echo OFF > /sys/kernel/debug/vgaswitcheroo/switch   # 关闭未使用的显卡
```

然后可以再`cat`一下看看显卡的状态。

最后，因为重启后会失效，这个问题的解决办法因发行版不同而不同，我的是Arch Linux，所以只要在`/etc/rc.local`文件中加入以下内容就可以了（Ubuntu用户可以参考最后的链接）：

```shell
echo IGD > /sys/kernel/debug/vgaswitcheroo/switch
echo OFF > /sys/kernel/debug/vgaswitcheroo/switch
```

-----

- [HybridGraphics](https://help.ubuntu.com/community/HybridGraphics)
