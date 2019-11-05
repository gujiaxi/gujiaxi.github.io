---
layout: post
title: "Arch Linux下通过chroot修复GRUB"
date: 2013-06-04 23:26
---
之前一直用的[旧的GRUB](https://wiki.archlinux.org/index.php/GRUB_Legacy)，一直好好的也没管它，今天因为升级个filesystem提示冲突，就心想着换到[新的GRUB](https://wiki.archlinux.org/index.php/GRUB)吧正好，可当时不知道怎么就二了，直接把原来的GRUB给删除了，然后忘了安装`grub-bios`。。。重启。。。世界一片漆黑 = =.

首先，找张Live CD盘，引导进去，然后挂载原来Linux的分区，再chroot进去：

```shell
mount /dev/sda6 /mnt # 这里的sda6是我Arch的根分区
for i in /sys proc /run /dev; do mount --bind "$i" "/mnt$i"; done
arch-chroot /mnt
```

再把GRUB相关的包装上：

```shell
pacman -S os-prober grub-common grub-bios # 这里的os-prober的作用是检测硬盘上的其他OS
```

最后就是grub相关命令来产生配置文件，并安装GRUB到相应位置：

```shell
grub-mkconfig -o /boot/grub/grub.cfg # 这一步会自动检测硬盘上的所有OS并生成配置文件
grub-install /dev/sda
```

好了，大致就这样子了，如果有遇到相同麻烦的朋友，还有问题可以在下面留言，一起交流学习哈。:)
