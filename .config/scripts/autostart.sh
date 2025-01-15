#!/bin/bash

picom --animations -b &
betterlockscreen -u ~/.wallpapers && betterlockscreen -w &
~/.config/polybar/forest/launch.sh &
kmonad ~/.kmonad.kbd && setxkbmap -layout us -variant intl &
greenclip daemon &
dunst &
udiskie -a &
caffeine &
xfsettingsd --sm-client-disable & # To apply themes to gtk apps
anydesk --service &
xset -b s off -dpms r rate 180 60 &
