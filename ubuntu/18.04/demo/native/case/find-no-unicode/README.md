
# find-no-unicode


## 緣起

這個專案是用來回覆「討論：[LO既有圖形操作介面能否直接叫用未被設定unicode碼位的字形檔內的字圖？](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=361612#forumpost361612)」


## FontForge Script 範例

* [find-no-unicode.ff](find-no-unicode.ff)


## 事前準備

### 安裝工具

執行下面指令，安裝「[fontforge](https://packages.ubuntu.com/bionic/fontforge)」和「[fontforge-extras](https://packages.ubuntu.com/bionic/fontforge-extras)」。

``` sh
$ sudo apt-get install fontforge fontforge-extras
```

相關說明可以參考「[如何安裝 FontForge](https://samwhelp.github.io/note-about-fontforge/ubuntu/18.04/#/install)」。

### 準備字型檔

先在這個資料夾準備「TW-Kai-98_1.ttf」這個檔案，
可以在「[這個頁面](https://data.gov.tw/dataset/5961)」，找到「[下載連結](http://www.cns11643.gov.tw/AIDB/Open_Data.zip)」。

> 寫這篇文，在測試的時候，是「108年8月13日更新」的版本。

下載後，解開，然後可以在「Open_Data/Fonts」這個資料夾找到「TW-Kai-98_1.ttf」。


## 操作步驟

### 找尋

關於在「FontForge」裡「Unicode=-1」的「Glyph」，在下面幾個連結可以找到相關論述，

* http://designwithfontforge.com/en-US/Importing_Glyphs_from_Other_Programs.html#custom-glyph-lists]
* http://designwithfontforge.com/en-US/Adding_Glyphs_to_an_Arabic_Font.html#add-the-glyphs-for-the-connected-forms-of-peh
* http://designwithfontforge.com/zh-CN/Importing_Glyphs_from_Other_Programs.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AD%97%E5%BD%A2%E5%88%97%E8%A1%A8
* http://designwithfontforge.com/zh-CN/Adding_Glyphs_to_an_Arabic_Font.html#%E4%B8%BApeh%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%BD%A2%E5%BC%8F%E6%B7%BB%E5%8A%A0%E5%AD%97%E5%BD%A2

執行下面指令，找尋「Unicode=-1」的「Glyph」。

``` sh
./find-no-unicode.ff
```

顯示

```
Copyright (c) 2000-2014 by George Williams. See AUTHORS for Contributors.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 with many parts BSD <http://fontforge.org/license.html>. Please read LICENSE.
 Based on sources from 11:21 UTC 24-Sep-2017-ML-D.
 Based on source from git with hash:
The glyph named Delta is mapped to U+0394.
  But its name indicates it should be mapped to U+2206.
The glyph named Omega is mapped to U+03A9.
  But its name indicates it should be mapped to U+2126.
The glyph named mu is mapped to U+03BC.
  But its name indicates it should be mapped to U+00B5.

=== Find Start:

Glyph.Unicode=-1 : Glyph.Name=.notdef
Glyph.Unicode=-1 : Glyph.Name=.null
Glyph.Unicode=-1 : Glyph.Name=nonmarkingreturn
Glyph.Unicode=-1 : Glyph.Name=ellipsis.vert
Glyph.Unicode=-1 : Glyph.Name=uniFF5E.vert

=== Find End:
```

### 探索 .notdef

執行

``` sh
$ showttf TW-Kai-98_1.ttf | grep '.notdef' | less
```

最後顯示

```
Glyph 0 (name index=0) -> ".notdef"       U+FFFF
```

### 探索 .null

執行

``` sh
$ showttf TW-Kai-98_1.ttf | grep '.null' | less
```

最後顯示

```
Glyph 1 (name index=1) -> ".null"         U+0000
          Glyph 1 (.null) is a Base
```

### 探索 nonmarkingreturn

執行

``` sh
$ showttf TW-Kai-98_1.ttf | grep 'nonmarkingreturn' | less
```

最後顯示

```
Glyph 2 (name index=2) -> "nonmarkingreturn"      U+0000
          Glyph 2 (nonmarkingreturn) is a Base
```

### 探索 ellipsis.vert

執行

``` sh
$ showttf TW-Kai-98_1.ttf | grep 'ellipsis.vert' | less
```

最後顯示

```
Glyph 39189 (name index=39196) -> "ellipsis.vert"         U+0000
                Glyph 5539 (ellipsis) -> 39189 (ellipsis.vert)
          Glyph 39189 (ellipsis.vert) is a Base
```

### 探索 uniFF5E.vert

執行

``` sh
$ showttf TW-Kai-98_1.ttf | grep 'uniFF5E.vert' | less
```

最後顯示

```
Glyph 39190 (name index=39197) -> "uniFF5E.vert"          U+0000
                Glyph 39052 (uniFF5E) -> 39190 (uniFF5E.vert)
          Glyph 39190 (uniFF5E.vert) is a Base
```
