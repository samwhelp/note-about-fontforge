#!/usr/bin/env bash

THE_FONTS_DIR_PATH="$HOME/.local/share/fonts"

mkdir -p "$THE_FONTS_DIR_PATH"

echo
echo "cp Demo-Copy.ttf $THE_FONTS_DIR_PATH/Demo-Copy.ttf"
cp "Demo-Copy.ttf" "$THE_FONTS_DIR_PATH/Demo-Copy.ttf"

echo
fc-cache -fv "$THE_FONTS_DIR_PATH"

echo
fc-list | grep 'DemoCopy'
#ls -l "$HOME/.local/share/fonts/Demo-Copy.ttf"
file "$HOME/.local/share/fonts/Demo-Copy.ttf"
#stat "$HOME/.local/share/fonts/Demo-Copy.ttf"
