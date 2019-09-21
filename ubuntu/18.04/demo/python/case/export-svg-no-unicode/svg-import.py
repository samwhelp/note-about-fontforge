#!/usr/bin/env python


## Usage:
# $ ./svg-import.py svg/*
# $ ./svg-import.py svg/{.[!.]*.svg,*.svg}

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


target_font.reencode('iso10646-1')

source_svg_list = sys.argv[1:]


## Import

print('')
print("=== Import Start:")

for source_svg_path in source_svg_list:
	#print(source_svg_path)
	col = source_svg_path.split('/', 1);
	source_glyph_name = col[1][:-4]
	#print(source_svg_path)

	if source_glyph_name == 'ellipsis.vert':
		target_glyph_name = 'a'
	elif source_glyph_name == 'uniFF5E.vert':
		target_glyph_name = 'b'
	elif source_glyph_name == 'nonmarkingreturn':
		target_glyph_name = 'c'
	else:
		continue

	target_font.selection.select(target_glyph_name)
	#print(target_glyph_name)
	target_font.paste() ## this line is essential for call target_font[target_glyph_name]

	glyph = target_font[target_glyph_name]
	#print(dir(glyph))

	print('')
	print("Import: [{}] To: [{}]".format(source_glyph_name, target_glyph_name))
	glyph.importOutlines(source_svg_path)


print('')
print("=== Import End:")
print('')


## Generate Demo-NoUni.ttf
target_font.generate('Demo-NoUni.ttf')


print('')
print("Generate Demo-NoUni.ttf.")

print('')
print("Please check:")
print('')
print("$ file Demo-NoUni.ttf")
print("$ showttf Demo-NoUni.ttf | less")
print("$ fontforge Demo-NoUni.ttf")
print('')
