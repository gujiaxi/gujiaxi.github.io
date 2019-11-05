---
layout: post
title: "EZWinPorts on Windows"
date: 2015-12-10
---
> The EZWinPorts project provides many useful ports of recent versions of GNU and Unix software. This includes all the optional libraries used by Emacs (image libraries, libxml2, GnuTLS), RCS, Texinfo, a clone of man command, Grep, xz, bzip2, bsdtar, ID Utils, Findutils, Hunspell, Gawk, GNU Make, Groff, GDB.

Below is a how-to if you want to configure all-in-one [EZWinPorts](http://sourceforge.net/projects/ezwinports/) on your Windows machine. Now here we go.

1. Download the [text file](https://dl.dropboxusercontent.com/u/23227383/ezwinports.txt) which contains all the download link of the EZWinPorts sub-modules.

2. Download all the sub-modules using `wget` according to the text file we just fetched.
   ```shell
   wget -c --content-disposition --trust-server-names -i ezwinports.txt
   ```

3. Unzip all the zip files accordingly. Here I use `7z` on Windows. If you use it within `cygwin`, you'd better pay attention to the permission issues.
   ```shell
   for %i in (*.zip) do 7z x %i -od://gnu -aoa
   ```

4. Add the **bin** folder to you System PATH.
