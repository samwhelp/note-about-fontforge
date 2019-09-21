
## 緣起

這個專案是用來回覆「討論：[LO既有圖形操作介面能否直接叫用未被設定unicode碼位的字形檔內的字圖？](https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=361612#forumpost361612)」


## Python Script 範例

* [svg-export.py](svg-export.py)
* [svg-import.py](svg-import.py)

## 對照 Native 版本

* [export-svg-no-unicode](https://github.com/samwhelp/note-about-fontforge/tree/gh-pages/ubuntu/18.04/demo/native/case/export-svg-no-unicode)
* export-svg-no-unicode/[svg-export.ff](https://github.com/samwhelp/note-about-fontforge/tree/gh-pages/ubuntu/18.04/demo/native/case/export-svg-no-unicode/svg-export.ff)
* export-svg-no-unicode/[svg-import.ff](https://github.com/samwhelp/note-about-fontforge/tree/gh-pages/ubuntu/18.04/demo/native/case/export-svg-no-unicode/svg-import.ff)

## 事前準備

### 安裝 python-fontforge

要在「python2」可以使用「fontforge」這個「module」，需要安裝「[python-fontforge](https://packages.ubuntu.com/bionic/python-fontforge)」這個「Package」

``` sh
$ sudo apt-get install python-fontforge
```

> 若是在「fontforge」使用「python script」則不需要額外安裝「python-fontforge」。


### 準備字型檔

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

關於在「FontForge」裡「Unicode=-1」的「Glyph」，在下面幾個連結可以找到相關論述，

* http://designwithfontforge.com/en-US/Importing_Glyphs_from_Other_Programs.html#custom-glyph-lists]
* http://designwithfontforge.com/en-US/Adding_Glyphs_to_an_Arabic_Font.html#add-the-glyphs-for-the-connected-forms-of-peh
* http://designwithfontforge.com/zh-CN/Importing_Glyphs_from_Other_Programs.html#%E8%87%AA%E5%AE%9A%E4%B9%89%E5%AD%97%E5%BD%A2%E5%88%97%E8%A1%A8
* http://designwithfontforge.com/zh-CN/Adding_Glyphs_to_an_Arabic_Font.html#%E4%B8%BApeh%E7%9A%84%E8%BF%9E%E6%8E%A5%E5%BD%A2%E5%BC%8F%E6%B7%BB%E5%8A%A0%E5%AD%97%E5%BD%A2

從「TW-Kai-98_1.ttf」 匯出在「FontForge」裡「Unicode=-1」的「Glyph」，

這些步驟，我寫成「Python Script」，內容請參考「[svg-export.py](svg-export.py)」。

可以執行

``` bash
$ ./svg-export.py ./TW-Kai-98_1.ttf
```

或是執行

``` sh
$ make svg-export
```

會顯示

```
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

$ ls -1 svg/{.[!.]*.svg,*.svg}
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

> 關於「匯出」這個動作，也可以在「FontForge」的「圖形界面操作」，目前只有了解到「一次匯出一個」，還沒有了解到「批次匯出」，所以才寫成「Python Script」。操作方式，點選某一個有「字圖」的「碼位」，然後會跳出一個新視窗，在這個「新視窗」的「功能選單」找到「File/Export」，點選它，接著就跳出一個新的「對話框」，然後最下方，有一個「Format」欄位，可以下拉選「SVG」，按下「Save」按鈕，就可以「匯出svg」。
注意：若看不到下方「Save」按鈕，可以用滑鼠拖拉更改「對話框」大小，就會顯示出來了。


## 匯入

將剛剛匯出「svg」，匯入到一個全新的「ttf」。

這些步驟，我寫成「Python Script」，內容請參考「[svg-import.py](svg-import.py)」。

可以執行

``` bash
$ ./svg-import.py svg/{.[!.]*.svg,*.svg}
```

或是執行

``` sh
$ make svg-import
```

會顯示

```

=== Import Start:

Import: [ellipsis.vert] To: [a]

Import: [nonmarkingreturn] To: [c]
I'm sorry this file is too complex for me to understand (or is erroneous)

Import: [uniFF5E.vert] To: [b]

=== Import End:


Generate Demo-NoUni.ttf.

Please check:

$ file Demo-NoUni.ttf
$ showttf Demo-NoUni.ttf | less
$ fontforge Demo-NoUni.ttf
```

從上面提示訊息，可以看到只有匯入[ellipsis.vert]和[uniFF5E.vert]。


> 關於「匯入」這個動作，也可以在「FontForge」的「圖形界面操作」，請參考「匯出」這個動作，做反向操作，在「Glyph視窗」的「功能選單」有「File/Export」可選。


> 關於「匯入失敗」，這部份尚在研究中，所以就暫時不處理了。


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


## Python Script for FontForge 參考文件

### 教學

* https://fontforge.github.io/en-US/tutorials/scripting/
* https://fontforge.github.io/scripting-tutorial.html
* https://fontforge.github.io/en-US/documentation/scripting/
* https://fontforge.github.io/scripting.html

### Api

* https://fontforge.github.io/python.html
* https://fontforge.github.io/en-US/documentation/scripting/python/
* http://dmtr.org/ff.php

### Example

* https://github.com/fontforge/designwithfontforge.com/issues/16
