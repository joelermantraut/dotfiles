#!/bin/bash

declare options=("Apagar
Reiniciar
Suspender
Bloquear
Salir")

choice=$(echo -e "${options[@]}" | dmenu_styled -p "»") || exit 1

case "$choice" in
    Apagar)
        choice="shutdown -h now"
    ;;
    Reiniciar)
        choice="reboot"
    ;;
    Suspender)
        choice="systemctl suspend"
    ;;
    Bloquear)
        choice="betterlockscreen -l dim blur"
    ;;
    Salir)
        choice="kill -9 -1"
    ;;
esac
alacritty -e $choice
