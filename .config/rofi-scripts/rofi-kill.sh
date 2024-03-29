#!/usr/bin/env bash
#
# Based on Derek Taylor dmkill script

answer="No"

confirm() {
    if [[ -n $selected ]]; then

        answer="$(echo -e "No\nYes" | rofi -dmenu -i -p "Kill $selected?")"

        if [[ $answer == "Yes" ]]; then
            selpid="$(awk '{print $1}' <<< $selected)"; 
            kill -9 $selpid
            echo "Process $selected has been killed." && exit 1
        fi
    fi
}


while [ "$answer" == "No" ]
do
    selected="$(ps --user "$(id -u)" -F | \
                rofi -dmenu -l 15 -width 500 -p "Kill:" | \
                awk '{print $2" "$11}')";

    if [ "$selected" == "" ]; then
        exit
    fi

    confirm

done

exit 0
