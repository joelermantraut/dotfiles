#!/bin/bash

picom --animations -b &
betterlockscreen -u ~/.wallpapers && betterlockscreen -w &
~/.config/polybar/forest/launch.sh &
kmonad ~/.kmonad.kbd &
greenclip daemon &
dunst &
udiskie -a &
caffeine &
xfsettingsd --sm-client-disable & # To apply themes to gtk apps
anydesk --service &
xset s off -dpms &
