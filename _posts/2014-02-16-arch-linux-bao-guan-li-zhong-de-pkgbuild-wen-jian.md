---
layout: post
title: "Arch Linux包管理中的PKGBUILD文件"
date: 2014-02-16 19:55
---
主要说说 Archlinux 下的包管理，对于下载源码编译的包，最好的办法还是把它打包成`xxx.pkg.tar.xz`然后再用**pacman**来安装，其实核心内容还是**PKGBUILD**的问题。

首先了解一下[PKGBUILD](https://wiki.archlinux.org/index.php/PKGBUILD)的概念。

在系统目录中有一个示例文件`/usr/share/pacman/PKGBUILD.proto`：
```shell
# This is an example PKGBUILD file. Use this as a start to creating your own,
# and remove these comments. For more information, see 'man PKGBUILD'.
# NOTE: Please fill out the license field for your package! If it is unknown,
# then please put 'unknown'.

# Maintainer: Your Name <youremail@domain.com>
pkgname=NAME
pkgver=VERSION
pkgrel=1
epoch=
pkgdesc=""
arch=()
url=""
license=('GPL')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=($pkgname-$pkgver.tar.gz
        $pkgname-$pkgver.patch)
noextract=()
md5sums=() #generate with 'makepkg -g'

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
}

build() {
	cd "$srcdir/$pkgname-$pkgver"
	./configure --prefix=/usr
	make
}

check() {
	cd "$srcdir/$pkgname-$pkgver"
	make -k check
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make DESTDIR="$pkgdir/" install
}
```

相关的参数跟规则可以对照着看 Wiki，就不多说了，下面再完整地举个打包的例子：

```shell
mkdir package # 建立一个工作目录
cp PKGBUILD package/; cd package # 把写好的PKGBUILD拷到目录中然后进入目录
wget xxx.tar.gz # 下载文件
mkdir src; ln src/xxx.tar.gz xxx.tar.gz # 建软链
md5sum xxx.tar.gz # 计算md5并把它填如PKGBUILD文件中
makepkg -g
makepkg # 打包
pacman -U xxx.pkg.tar.xz # 安装
```
