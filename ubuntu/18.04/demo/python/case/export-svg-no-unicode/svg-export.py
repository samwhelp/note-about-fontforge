#!/usr/bin/env python

## Usage:
# $ ./svg-export.py ./TW-Kai-98_1.ttf

## Reference:
# https://github.com/fontforge/designwithfontforge.com/issues/16
# https://fontforge.github.io/python.html
# https://fontforge.github.io/en-US/documentation/scripting/python/
# http://dmtr.org/ff.php

import fontforge
import sys

if len(sys.argv) < 2:
	print('Usage:')
	print('')
	print('$ ./svg-export.py {font_name}')
	print('')

	print('')
	print('Example:')
	print('')
	print('$ ./svg-export.py ./TW-Kai-98_1.ttf')
	print('')
	exit(0)

font=fontforge.open(sys.argv[1])
#font=fontforge.open("TW-Kai-98_1.ttf")

font.selection.all()

print('')
print('=== Export Start:')
print('')

for glyph_name in font:
	glyph = font[glyph_name]
	if glyph.unicode == -1:
		##print(dir(glyph))
		print("Glyph.Unicode=-1 : Glyph.Name={}".format(glyph_name))
		glyph.export("svg/{}.svg".format(glyph_name))

print('')
print('=== Export End:')
print('')

print('')
print('Please check dir [svg]:')
print('')

#print('$ ls -a -1 svg')
print('$ ls -1 svg/{.[!.]*.svg,*.svg}')
print('')
