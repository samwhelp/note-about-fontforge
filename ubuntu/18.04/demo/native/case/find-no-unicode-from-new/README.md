
# find-no-unicode-from-new


## 緣起

這個專案是用來回覆「討論：[LO既有圖形操作介面能否直接叫用未被設定unicode碼位的字形檔內的字圖？](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=361612#forumpost361612)」


## FontForge Script 範例

* [create-new-font.ff](create-new-font.ff)
* [find-no-unicode.ff](find-no-unicode.ff)


## 事前準備

### 安裝工具

執行下面指令，安裝「[fontforge](https://packages.ubuntu.com/bionic/fontforge)」和「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」。

``` sh
$ sudo apt-get install fontforge fontforge-extras
```

相關說明可以參考「[如何安裝 FontForge](https://samwhelp.github.io/note-about-fontforge/ubuntu/18.04/#/install)」。

### 準備字型檔

執行下面指令，產生一個新的字型檔

``` sh
$ ./create-new-font.ff
```

顯示

```
Copyright (c) 2000-2014 by George Williams. See AUTHORS for Contributors.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 with many parts BSD <http://fontforge.org/license.html>. Please read LICENSE.
 Based on sources from 11:21 UTC 24-Sep-2017-ML-D.
 Based on source from git with hash:
Warning: Font contained no glyphs
```

會產生一個檔案「Demo.ttf」。


## 探索操作步驟

### showttf

執行

``` sh
$ showttf ./Demo.ttf
```

擷取其中顯示的部份如下

```
Encoding (cmap) table (at 452)
platform=0 specific=3 offset=28 Unicode 2.0+
platform=1 specific=0 offset=52 Mac Roman
platform=3 specific=1 offset=28 MS Unicode
 Format=4 len=24 Language=0
Format 4 (Windows unicode), 1 segments
  Segment=0 unicode-start=ffff end=ffff range-offset=0 delta=1 glyph-start=65536 gend=65536
 Glyph 0 -> U+FFFF
 Glyph 1 -> U+0000
 Glyph 2 -> U+0000
```


### 找尋「Unicode=-1」的「Glyph」

關於在「FontForge」裡「Unicode=-1」的「Glyph」，在下面幾個連結可以找到相關論述，

* http://designwithfontforge.com/en-US/Importing_Glyphs_from_Other_Programs.html#custom-glyph-lists]
* http://designwithfontforge.com/en-US/Adding_Glyphs_to_an_Arabic_Font.html#add-the-glyphs-for-the-connected-forms-of-peh
* http://designwithfontforge.com/zh-CN/Importing_Glyphs_from_Other_Programs.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AD%97%E5%BD%A2%E5%88%97%E8%A1%A8
* http://designwithfontforge.com/zh-CN/Adding_Glyphs_to_an_Arabic_Font.html#%E4%B8%BApeh%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%BD%A2%E5%BC%8F%E6%B7%BB%E5%8A%A0%E5%AD%97%E5%BD%A2

執行下面指令，找尋「Unicode=-1」的「Glyph」。

``` sh
$ ./find-no-unicode.ff
```

顯示

```
Copyright (c) 2000-2014 by George Williams. See AUTHORS for Contributors.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 with many parts BSD <http://fontforge.org/license.html>. Please read LICENSE.
 Based on sources from 11:21 UTC 24-Sep-2017-ML-D.
 Based on source from git with hash:
Invalid ttf hmtx table (or hhea), numOfLongMetrics is 0

=== Find Start:

Glyph.Unicode=-1 : Glyph.Name=.notdef
Glyph.Unicode=-1 : Glyph.Name=glyph1
Glyph.Unicode=-1 : Glyph.Name=glyph2

=== Find End:
```

## 接下來

對照下面兩個範例

* [find-no-unicode](../find-no-unicode)
* [find-no-unicode-from-new-import](../find-no-unicode-from-new-import)
