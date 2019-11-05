---
layout: post
title: "Setup printer service on Archlinux"
date: 2015-07-23
---
Just follow the [Wiki](https://wiki.archlinux.org/index.php/CUPS).

First, install [CUPS](http://www.cups.org/). Then **start** and **enable** the service.

```shell
pacman -S cups, libcups
systemctl start org.cups.cupsd.service
systemctl enable org.cups.cupsd.service
```

Finally, install **system-config-printer**. It's a GUI config tool for CUPS.

```shell
pacman -S system-config-printer
```
