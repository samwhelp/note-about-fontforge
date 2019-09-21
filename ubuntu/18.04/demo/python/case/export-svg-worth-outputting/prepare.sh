#!/usr/bin/env bash

## Prepare unar or unzip
## https://www.ubuntu-tw.org/modules/newbb/viewtopic.php?post_id=360396#forumpost360396
#sudo apt-get install unar
#sudo apt-get install unzip

## To Work Dir
mkdir -p var
cd var

## Download
## https://data.gov.tw/dataset/5961
wget -c 'http://www.cns11643.gov.tw/AIDB/Open_Data.zip'


## Extract
unar Open_Data.zip
## or use
#unzip -O big5 Open_Data.zip


## Copy TW-Kai-98_1.ttf to Base Dir
cp Open_Data/Fonts/TW-Kai-98_1.ttf ../
