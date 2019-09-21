#!/usr/bin/env bash

THE_FONTS_DIR_PATH="$HOME/.local/share/fonts"

mkdir -p "$THE_FONTS_DIR_PATH"

echo
echo "rm -f $THE_FONTS_DIR_PATH/Demo-NoUni.ttf"
rm -f "$THE_FONTS_DIR_PATH/Demo-NoUni.ttf"

echo
fc-cache -fv "$THE_FONTS_DIR_PATH"

echo
fc-list | grep 'DemoNoUni'
ls "$HOME/.local/share/fonts/Demo-NoUni.ttf"
#file "$HOME/.local/share/fonts/Demo-NoUni.ttf"
#stat "$HOME/.local/share/fonts/Demo-NoUni.ttf"


## [exit 0] for [$ make font-remove]
exit 0
