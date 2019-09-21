#!/usr/bin/env bash

THE_FONTS_DIR_PATH="$HOME/.local/share/fonts"

mkdir -p "$THE_FONTS_DIR_PATH"

echo
echo "cp Demo-NoUni.ttf $THE_FONTS_DIR_PATH/Demo-NoUni.ttf"
cp "Demo-NoUni.ttf" "$THE_FONTS_DIR_PATH/Demo-NoUni.ttf"

echo
fc-cache -fv "$THE_FONTS_DIR_PATH"

echo
fc-list | grep 'DemoNoUni'
#ls -l "$HOME/.local/share/fonts/Demo-NoUni.ttf"
file "$HOME/.local/share/fonts/Demo-NoUni.ttf"
#stat "$HOME/.local/share/fonts/Demo-NoUni.ttf"
