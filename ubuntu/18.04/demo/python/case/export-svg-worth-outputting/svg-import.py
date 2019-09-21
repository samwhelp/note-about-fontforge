#!/usr/bin/env python


## Usage:
# $ ./svg-import.py svg/*.svg
# $ ./svg-import.py svg/*
# $ ./svg-import.py svg/{.[!.]*.svg,*.svg}


# $ ls svg/*.svg
# $ ls svg/*
# $ ls svg/{.[!.]*,*}
# $ ls svg/{.[!.]*.svg,*.svg}


## Reference:
# https://github.com/fontforge/designwithfontforge.com/issues/16
# https://fontforge.github.io/python.html
# https://fontforge.github.io/en-US/documentation/scripting/python/
# http://dmtr.org/ff.php

import fontforge
import sys

#print(len(sys.argv))
#print(sys.argv[1:])
#print(sys.argv)

if len(sys.argv) < 2:
	print('Usage:')
	print('')
	print('$ ./svg-export.py svg_path_list')
	print('')

	print('')
	print('Example:')
	print('')
	print('$ ./svg-import.py svg/{.[!.]*.svg,*.svg}')
	print('')
	exit(0)

## Create New Font
target_font = fontforge.font()

target_font.fontname = 'DemoCopy'
target_font.familyname = 'DemoCopy'
target_font.fullname = 'DemoCopy'
#target_font.weight = 'Book'
target_font.weight = 'Regular'
target_font.copyright = 'Copyright (c) 2019, People,,,'
target_font.version = '1.0'

#target_font.encoding = 'UnicodeFull'
#target_font.encoding = 'UnicodeBmp'
target_font.encoding = 'iso10646-1'
#target_font.reencode('iso10646-1')
#print(target_font.encoding)



source_svg_list = sys.argv[1:]


## Import

print('')
print("=== Import Start:")

for source_svg_path in source_svg_list:
	#print(source_svg_path)
	col = source_svg_path.split('/', 1);
	source_glyph_unicode = col[1][:-4]
	target_glyph_unicode = int('0x' + source_glyph_unicode, 16)
	target_glyph_name = fontforge.nameFromUnicode(target_glyph_unicode)


	target_font.selection.select(target_glyph_unicode)
	target_font.paste() ## this line is essential for call target_font[target_glyph_unicode]


	#glyph = target_font[target_glyph_name]
	glyph = target_font[target_glyph_unicode]
	#print(dir(glyph))

	#print('')
	#print("Import: [{}] To: [{}]".format(source_glyph_unicode, target_glyph_name))
	glyph.importOutlines(source_svg_path)


print('')
print("=== Import End:")
print('')


## Generate Demo-Copy.ttf
target_font.generate('Demo-Copy.ttf')


print('')
print("Generate Demo-Copy.ttf.")

print('')
print("Please check:")
print('')
print("$ file Demo-Copy.ttf")
print("$ showttf Demo-Copy.ttf | less")
print("$ fontforge Demo-Copy.ttf")
print('')
