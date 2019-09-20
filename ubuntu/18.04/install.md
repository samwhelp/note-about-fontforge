
# 如何安裝 FontForge


## 操作環境

* Ubuntu 18.04

## 查詢套件

執行

``` sh
$ apt-cache search fontforge
```

顯示

```
fontforge - font editor
fontforge-common - font editor (common files)
fontforge-dbg - debugging symbols for fontforge
fontforge-doc - documentation for fontforge
fontforge-extras - Additional data and utilities for FontForge
fontforge-nox - font editor - non-X version
fonts-hanazono - Japanese TrueType mincho font by KAGE system and FontForge
fonts-inconsolata - monospace font for pretty code listings and for the terminal
fonts-oflb-euterpe - unicode musical font
fonts-oldstandard - smart font with wide range of Latin, Greek and Cyrillic characters
fonts-opendin - Open DIN font
fonts-rufscript - handwriting-based font for Latin characters
libfontforge-dev - font editor - runtime library (development files)
libfontforge2 - font editor - runtime library
libgdraw5 - font editor - runtime graphics and widget library
python-fontforge - font editor - Python bindings
sortsmill-tools - tools for designers of digital fonts
unifont-bin - utilities for manipulating GNU Unifont
```

執行

``` sh
$ apt-cache pkgnames fontforge
```

顯示

```
fontforge-common
fontforge-nox
fontforge-extras
fontforge-dbg
fontforge-doc
fontforge
```

執行

``` sh
$ apt-cache show fontforge
```

顯示

```
Package: fontforge
Architecture: amd64
Version: 1:20170731~dfsg-1
Multi-Arch: foreign
Priority: optional
Section: universe/x11
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Debian Fonts Task Force <pkg-fonts-devel@lists.alioth.debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 91
Depends: fontforge-common (= 1:20170731~dfsg-1), libfontforge2 (= 1:20170731~dfsg-1), libgdraw5 (= 1:20170731~dfsg-1), libc6 (>= 2.2.5)
Suggests: autotrace, fontforge-doc, fontforge-extras, potrace, python-fontforge
Conflicts: fontforge-nox
Filename: pool/universe/f/fontforge/fontforge_20170731~dfsg-1_amd64.deb
Size: 15768
MD5sum: 1221a4a288f0f0a16e850eab8ecc8209
SHA1: 61818a044e7a070f5000c3dba3513fad81118448
SHA256: 0bab802a5690e458783aa7aded51e6f3083fb6c8a4ababa0e5cb98caf18bcd23
Homepage: https://fontforge.github.io/en-US/
Description-en: font editor
 FontForge is a font editor.
 Use it to create, edit and convert fonts
 in OpenType, TrueType, UFO, CID-keyed, Multiple Master,
 and many other formats.
 .
 This package also provides these programs and utilities:
  fontimage - produce a font thumbnail image;
  fontlint  - checks the font for certain common errors;
  sfddiff   - compare two font files.
Description-md5: 4ebffb1f6ab9a1d49bd81ce04ad8a0a7
Task: ubuntustudio-publishing
```


## 安裝步驟

### 安裝 fontforge

執行下面指令，安裝「[fontforge](https://packages.ubuntu.com/bionic/fontforge)」這個「Package」。

``` sh
$ sudo apt-get install fontforge
```

確認是否安裝成功，執行下面指令

``` sh
$ dpkg -l fontforge
```

顯示

```
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name                            Version              Architecture         Description
+++-===============================-====================-====================-====================================================================
ii  fontforge                       1:20170731~dfsg-1    amd64                font editor
```

執行下面指令，查詢「[fontforge](https://packages.ubuntu.com/bionic/fontforge)」這個「Package」安裝[那些檔案](https://packages.ubuntu.com/bionic/amd64/fontforge/filelist)在系統上。

``` sh
$ dpkg -L fontforge | sort
```

顯示

```
/.
/usr
/usr/bin
/usr/bin/fontforge
/usr/bin/fontimage
/usr/bin/fontlint
/usr/bin/sfddiff
/usr/share
/usr/share/applications
/usr/share/applications/fontforge.desktop
/usr/share/doc
/usr/share/doc/fontforge
/usr/share/doc/fontforge/AUTHORS.gz
/usr/share/doc/fontforge/changelog.Debian.gz
/usr/share/doc/fontforge/copyright
/usr/share/lintian
/usr/share/lintian/overrides
/usr/share/lintian/overrides/fontforge
```

## 額外安裝

討論中會提到一個指令「[showttf](http://manpages.ubuntu.com/manpages/bionic/en/man1/showttf.1.html)」，是來自於「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」這個「Package」。

### 安裝 fontforge-extras

安裝前，先執行下面指令，觀看「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」這個「Package」的相關資訊

``` sh
$ apt-cache show fontforge-extras
```

顯示

```
Package: fontforge-extras
Architecture: amd64
Version: 0.3-4ubuntu1
Priority: optional
Section: universe/x11
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Debian Fonts Task Force <pkg-fonts-devel@lists.alioth.debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 905
Depends: libc6 (>= 2.4)
Conflicts: fontforge (<= 0.0.20081224)
Replaces: fontforge (<= 0.0.20081224)
Filename: pool/universe/f/fontforge-extras/fontforge-extras_0.3-4ubuntu1_amd64.deb
Size: 398652
MD5sum: ef87e5fdf2e2272662f3e24881dc7cc5
SHA1: e1b699c94b145e6c17c860115a8386d6bf5df4f1
SHA256: f4ed5649b01bdc5008cfd6feeff0364d251a05ff9056ffa7d512120ea0d59ea5
Homepage: http://fontforge.sourceforge.net/
Description-en: Additional data and utilities for FontForge
 This package contains extra data and utilities for the FontForge
 font editor:
 .
  * cidmaps: character set descriptions for editing CID keyed fonts;
  * encodings.ps: an extra encoding tables;
  * showttf: a program which will decompose a truetype (or opentype)
    font file into its various tables and display the contents of
    those tables.
Description-md5: 9df2c744dcade7838696ce74d8ba0ec9
```

執行下面指令，安裝「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」這個「Package」。

``` sh
$ sudo apt-get install fontforge-extras
```

執行下面指令，查詢「[fontforge](https://packages.ubuntu.com/bionic/fontforge-extras)」這個「Package」安裝[那些檔案](https://packages.ubuntu.com/bionic/amd64/fontforge-extras/filelist)在系統上。

``` sh
$ dpkg -L fontforge-extras | sort
```

顯示

```
/.
/usr
/usr/bin
/usr/bin/showttf
/usr/share
/usr/share/doc
/usr/share/doc/fontforge-extras
/usr/share/doc/fontforge-extras/changelog.Debian.gz
/usr/share/doc/fontforge-extras/copyright
/usr/share/doc/fontforge-extras/Encodings.ps.gz
/usr/share/doc/fontforge-extras/README.Debian
/usr/share/fontforge
/usr/share/fontforge/Adobe-CNS1-5.cidmap
/usr/share/fontforge/Adobe-GB1-5.cidmap
/usr/share/fontforge/Adobe-Identity-0.cidmap
/usr/share/fontforge/Adobe-Japan1-6.cidmap
/usr/share/fontforge/Adobe-Japan2-0.cidmap
/usr/share/fontforge/Adobe-Korea1-2.cidmap
/usr/share/man
/usr/share/man/man1
/usr/share/man/man1/showttf.1.gz
```




## 下一步

* [回索引](all.md)
