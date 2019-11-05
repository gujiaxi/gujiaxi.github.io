---
layout: post
title:  "利用Ubuntu的Live CD修复MBR"
date:   2011-12-12 00:24:58
---

事情是这样的：昨天帮同学装了Ubuntu，后来他告诉我开机直接进Windows、进不了Ubuntu了，搞清楚状况之后，如你所想的那样，原因很简单，Windows下某个奇怪的软件重写了MBR。

1. 使用Ubuntu live CD引导系统。
2. 打开终端，输入以下命令：

   ``` shell
   sudo mount /dev/xxx /mnt    # 这儿的"/dev/xxx"是存放根分区的设备的名称（比如/dev/sda6）
   sudo grub-install --root-directory=/mnt /dev/yyy    # 这儿的"/dev/yyy"是你想要安装MBR的驱动器的名称（比如/dev/sda1）
   sudo umount /mnt    # 别忘了卸载/mnt
   sudo reboot    # 重启
   ```

3. 最后重新从硬盘引导系统。如果提示移出CD安装盘，照做就行了。
