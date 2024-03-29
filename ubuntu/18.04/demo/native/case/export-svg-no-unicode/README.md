
# export-svg-no-unicode

## 緣起

這個專案是用來回覆「討論：[LO既有圖形操作介面能否直接叫用未被設定unicode碼位的字形檔內的字圖？](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=361612#forumpost361612)」


## FontForge Script 範例

* [svg-export.ff](svg-export.ff)
* [svg-import.ff](svg-import.ff)


## 事前準備

先在這個資料夾準備「TW-Kai-98_1.ttf」這個檔案，
可以在「[這個頁面](https://data.gov.tw/dataset/5961)」，找到「[下載連結](http://www.cns11643.gov.tw/AIDB/Open_Data.zip)」。

> 寫這篇文，在測試的時候，是「108年8月13日更新」的版本。

下載後，解開，然後可以在「Open_Data/Fonts」這個資料夾找到「TW-Kai-98_1.ttf」，

我把整個步驟簡單寫成「Shell Script」，內容請參考「[prepare.sh](prepare.sh)」。

可以執行

``` sh
$ ./prepare.sh
```

或是執行

``` sh
$ make prepare
```

## 匯出

從「TW-Kai-98_1.ttf」 匯出在「FontForge」裡「Unicode=-1」的「Glyph」，

這些步驟，我寫成「FontForge Script」，內容請參考「[svg-export.ff](svg-export.ff)」。

可以執行

``` bash
$ ./svg-export.ff ./TW-Kai-98_1.ttf
```

或是執行

``` sh
$ make svg-export
```

會顯示

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

=== Export Start:

Glyph.Unicode=-1 : Glyph.Name=.notdef
Glyph.Unicode=-1 : Glyph.Name=.null
Glyph.Unicode=-1 : Glyph.Name=nonmarkingreturn
Glyph.Unicode=-1 : Glyph.Name=ellipsis.vert
Glyph.Unicode=-1 : Glyph.Name=uniFF5E.vert

=== Export End:


Please check dir [svg]:

$ ls -a -1 svg
```

會匯出在「svg」這個資料夾，

主要會匯出5個檔案，分別是

```
svg/.notdef.svg
svg/.null.svg
svg/nonmarkingreturn.svg
svg/ellipsis.vert.svg
svg/uniFF5E.vert.svg
```

> 關於「匯出」這個動作，也可以在「FontForge」的「圖形界面操作」，目前只有了解到「一次匯出一個」，還沒有了解到「批次匯出」，所以才寫成「FontForge Script」。操作方式，點選某一個有「字圖」的「碼位」，然後會跳出一個新視窗，在這個「新視窗」的「功能選單」找到「File/Export」，點選它，接著就跳出一個新的「對話框」，然後最下方，有一個「Format」欄位，可以下拉選「SVG」，按下「Save」按鈕，就可以「匯出svg」。
注意：若看不到下方「Save」按鈕，可以用滑鼠拖拉更改「對話框」大小，就會顯示出來了。


## 匯入

將剛剛匯出「svg」，匯入到一個全新的「ttf」。

這些步驟，我寫成「FontForge Script」，內容請參考「[svg-import.ff](svg-import.ff)」。

可以執行

``` bash
$ ./svg-import.ff svg/*
```

或是執行

``` sh
$ make svg-import
```

會顯示

```
Copyright (c) 2000-2014 by George Williams. See AUTHORS for Contributors.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 with many parts BSD <http://fontforge.org/license.html>. Please read LICENSE.
 Based on sources from 11:21 UTC 24-Sep-2017-ML-D.
 Based on source from git with hash:

=== Import Start:

Import: [ellipsis.vert] To: [U+0061]

Import: [nonmarkingreturn] To: [U+0063]
I'm sorry this file is too complex for me to understand (or is erroneous)

Import: [uniFF5E.vert] To: [U+0062]

=== Import End:


Generate Demo-NoUni.ttf.

Please check:

$ file Demo-NoUni.ttf
$ showttf Demo-NoUni.ttf | less
$ fontforge Demo-NoUni.ttf
```

從上面提示訊息，可以看到只有匯入[ellipsis.vert]和[uniFF5E.vert]。


> 關於「匯入」這個動作，也可以在「FontForge」的「圖形界面操作」，請參考「匯出」這個動作，做反向操作，在「Glyph視窗」的「功能選單」有「File/Export」可選。


> 關於「匯入失敗」因為「[Import](https://fontforge.github.io/scripting-alpha.html#Import)」沒有回傳值，並且目前我也還找不到其他偵測例外狀況的方式，所以就暫時不處理了。


## 安裝新產生的字型

安裝新產生的字型，除了可以使用圖形界面安裝，

在我的環境，在檔案總管「pcmanfm-qt」裡，

點選剛剛「Demo-NoUni.ttf」，

會使用「[gnome-font-viewer](https://packages.ubuntu.com/bionic/gnome-font-viewer) (Fonts)」開啟。

右上方有個按鈕「Install」按鈕，按下後就會安裝，

會安裝到「~/.local/share/fonts/」這個資料夾，

路徑是「~/.local/share/fonts/Demo-NoUni.ttf」。

這些步驟，我寫成「Shell Script」，內容請參考「[font-install.sh](font-install.sh)」。


## 測試新產生的字型

使用「LibreOffice Writer」來測試，

先用其他字型，輸入「ab」，

接著再改用「DemoNoUni」這個字型，

就可以看到「a」會變成「svg/ellipsis.vert.svg」的「字樣」。

就可以看到「b」會變成「svg/uniFF5E.vert.svg」的「字樣」。


## 移除新產生的字型

將剛剛安裝的字型，從系統移除。

這些步驟，我寫成「Shell Script」，內容請參考「[font-remove.sh](font-remove.sh)」。


## FontForge Script 參考文件

### 教學

* https://fontforge.github.io/en-US/tutorials/scripting/
* https://fontforge.github.io/scripting-tutorial.html
* https://fontforge.github.io/en-US/documentation/scripting/
* https://fontforge.github.io/scripting.html

### Api

* https://fontforge.github.io/scripting-alpha.html
* https://fontforge.github.io/scripting-alpha.html#Print
* https://fontforge.github.io/scripting-alpha.html#New
* https://fontforge.github.io/scripting-alpha.html#Open
* https://fontforge.github.io/scripting-alpha.html#Generate
* https://fontforge.github.io/scripting-alpha.html#Export
* https://fontforge.github.io/scripting-alpha.html#Import
* https://fontforge.github.io/scripting-alpha.html#SelectIf
* https://fontforge.github.io/scripting-alpha.html#SelectWorthOutputting
* https://fontforge.github.io/scripting-alpha.html#GlyphInfo
* https://fontforge.github.io/scripting-alpha.html#SetFontNames
* https://fontforge.github.io/scripting-alpha.html#Reencode
* https://fontforge.github.io/scripting-alpha.html#StrSplit
* https://fontforge.github.io/en-US/documentation/scripting/native/
