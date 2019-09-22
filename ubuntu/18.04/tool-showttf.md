
# showttf

## Help

### -h

執行

``` sh
$ showttf -h
```

顯示

```
showttf [-verbose] [-headers] ttf-file
```

### --help

執行

``` sh
$ showttf --help
```

顯示

```
showttf [-verbose] ttf-file
```

## ManPage

執行下面指令，觀看「showttf」的「[Manpage](http://manpages.ubuntu.com/manpages/bionic/en/man1/showttf.1.html)」。

``` sh
$ man showttf
```

## Package

### 已安裝時查詢

執行

``` sh
$ dpkg -S showttf
```

顯示

```
fontforge-extras: /usr/share/man/man1/showttf.1.gz
fontforge-extras: /usr/bin/showttf
```

### 未安裝時查詢

執行

``` sh
$ apt-file search showttf
```

顯示

```
fontforge-extras: /usr/bin/showttf
fontforge-extras: /usr/share/man/man1/showttf.1.gz
```

就可以查到「[showttf]((http://manpages.ubuntu.com/manpages/bionic/en/man1/showttf.1.html))」是來自於「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」這個「Package」。

## 使用範例

執行

``` sh
$ fc-list 'Ubuntu Mono'
```

顯示

```
/usr/share/fonts/truetype/ubuntu/UbuntuMono-RI.ttf: Ubuntu Mono:style=Italic
/usr/share/fonts/truetype/ubuntu/UbuntuMono-B.ttf: Ubuntu Mono:style=Bold
/usr/share/fonts/truetype/ubuntu/UbuntuMono-BI.ttf: Ubuntu Mono:style=Bold Italic
/usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf: Ubuntu Mono:style=Regular
```

上面找到四個檔案

以「UbuntuMono-R.ttf」為例，執行下面指令

``` sh
$ showttf /usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf | less
```

加入「--headers」參數，也就是執行下面指令

``` sh
$ showttf --headers /usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf | less
```


## 使用案例

* [find-no-unicode](https://github.com/samwhelp/note-about-fontforge/tree/gh-pages/ubuntu/18.04/demo/native/case/find-no-unicode)
