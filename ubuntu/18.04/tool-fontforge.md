
# fontforge


## Help

### --help

執行

``` sh
$ fontforge --help
```

顯示

```
Copyright (c) 2000-2014 by George Williams. See AUTHORS for Contributors.
 License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
 with many parts BSD <http://fontforge.org/license.html>. Please read LICENSE.
 Based on sources from 11:21 UTC 24-Sep-2017-ML-D.
 Based on source from git with hash:
no xdefs_filename!
TESTING: getPixmapDir:/usr/share/fontforge/pixmaps
TESTING: getShareDir:/usr/share/fontforge
TESTING: GResourceProgramDir:/usr/bin
trying default theme:/usr/share/fontforge/pixmaps/resources
fontforge [options] [fontfiles]
	-new			 (creates a new font)
	-last			 (loads the last sfd file closed)
	-recover none|auto|inquire|clean (control error recovery)
	-allglyphs		 (load all glyphs in the 'glyf' table
			 of a truetype collection)
	-nosplash		 (no splash screen)
	-quiet			 (don't print non-essential information to stderr)
	-unique			 (if a fontforge is already running open
			 all arguments in it and have this process exit)
	-display display-name	 (sets the X display)
	-depth val		 (sets the display depth if possible)
	-vc val			 (sets the visual class if possible)
	-cmap current|copy|private	 (sets the type of colormap)
	-dontopenxdevices	 (in case that fails)
	-sync			 (syncs the display, debugging)
	-keyboard ibm|mac|sun|ppc  (generates appropriate hotkeys in menus)
	-usecairo=yes|no  Use (or not) the cairo library for drawing
	-help			 (displays this message, and exits)
	-docs			 (displays this message, invokes a browser)
				 (Using the BROWSER environment variable)
	-version		 (prints the version of fontforge and exits)
	-library-status	 (prints information about optional libraries
				 and exits)
	-lang=py		 use python for scripts (may precede -script)
	-lang=ff		 use fontforge's legacy scripting language
	-script scriptfile	 (executes scriptfile)
		must be the first option (or follow -lang).
		All others passed to scriptfile.
	-dry scriptfile		 (syntax checks scriptfile)
		must be the first option. All others passed to scriptfile.
		Only for fontforge's own scripting language, not python.
	-c script-string	 (executes argument as scripting cmds)
		must be the first option. All others passed to the script.

FontForge will read postscript (pfa, pfb, ps, cid), opentype (otf),
	truetype (ttf,ttc), macintosh resource fonts (dfont,bin,hqx),
	and bdf and pcf fonts. It will also read its own format --
	sfd files.
If no fontfiles are specified (and -new is not either and there's nothing
	to recover) then fontforge will produce an open font dlg.
If a scriptfile is specified then FontForge will not open the X display
	nor will it process any additional arguments. It will execute the
	scriptfile and give it any remaining arguments
If the first argument is an executable filename, and that file's first
	line contains "fontforge" then it will be treated as a scriptfile.

For more information see:
	http://fontforge.sourceforge.net/
Send bug reports to:	fontforge-devel@lists.sourceforge.net
```

## 使用範例

### 開啟新檔

執行下面指令

``` sh
$ fontforge --new
```

一開始載入時，就不會出現對話框，直接開啟圖形界面程式，用來編輯新的字型。

### 開啟舊檔

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
$ fontforge /usr/share/fonts/truetype/ubuntu/UbuntuMono-R.ttf
```

### 開啟sfdir

關於「[Spline Font Database](sfd)」，可以存成資料夾的格式，
所以可以使用「fontforge」開啟該資料夾，副檔名是「sfdir」。
下面範例，資料夾的名稱是「Demo.sfdir」。

``` sh
$ fontforge Demo.sfdir
```

可以參考「[#2 回覆: 有無現成的把TTF包含字元輸出成純文字檔的圖形介面工具] (https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=361790#forumpost361790)」

### 執行腳本

關於這部份請參考「[scripting.md](scripting.md)」。

關於這方面的參數，擷取上面「--help」的內容如下

```
-lang=py		 use python for scripts (may precede -script)
-lang=ff		 use fontforge's legacy scripting language
-script scriptfile	 (executes scriptfile)
	must be the first option (or follow -lang).
	All others passed to scriptfile.
-dry scriptfile		 (syntax checks scriptfile)
	must be the first option. All others passed to scriptfile.
	Only for fontforge's own scripting language, not python.
-c script-string	 (executes argument as scripting cmds)
	must be the first option. All others passed to the script.
```
