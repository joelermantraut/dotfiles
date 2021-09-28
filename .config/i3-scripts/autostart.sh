#!/bin/bash

$HOME/.config/polybar/forest/launch.sh &
udiskie -t -a &
dunst &
clipster -d &
redshift &
~/.screenlayout/i3-screen-layout.sh &
betterlockscreen -u ~/Imagenes/slideshow && betterlockscreen -w &
#betterlockscreen -u ~/Imagenes/slideshow &&
    #feh --bg-fill ~/.cache/betterlockscreen/1-HDMI-0/resize.png ~/.cache/betterlockscreen/1-HDMI-0/resize.png &
