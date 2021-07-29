#!/bin/bash

declare options=("alacritty
neovim
qtile
qutebrowser
zsh
dmenu
rofi
ranger
dunst")

choice=$(echo -e "${options[@]}" | dmenu_styled -p 'Config: ') || exit 1

case "$choice" in
	alacritty)
		choice="$HOME/.config/alacritty/alacritty.yml"
	;;
    neovim)
        choice="$HOME/.config/nvim/init.vim"
    ;;
    qtile)
        choice="$HOME/.config/qtile/config.py"
    ;;
    qutebrowser)
        choice="$HOME/.config/qutebrowser/config.py"
    ;;
    zsh)
        choice="$HOME/.zshrc"
    ;;
    dmenu)
        choice="$HOME/.config/dmenu-extended/config/dmenuExtended_preferences.txt"
    ;;
    rofi)
        choice="$HOME/.config/rofi/config.rasi"
    ;;
    ranger)
        choice="$HOME/.config/ranger/rifle.conf"
    ;;
    dunst)
        choice="$HOME/.config/dunst/dunstrc"
    ;;
esac
alacritty -e nvim "$choice"

