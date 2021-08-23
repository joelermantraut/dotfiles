#!/bin/bash

$HOME/.config/polybar/launch.sh --forest &
betterlockscreen -u ~/Imagenes/slideshow && betterlockscreen -w &
udiskie -t -a &
dunst &
