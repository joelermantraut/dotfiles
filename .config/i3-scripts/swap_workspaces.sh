#!/usr/bin/env bash
# requires jq

IFS=:
i3-msg -t get_outputs | jq -r '.[]|"\(.name):\(.current_workspace)"' | grep -v '^null:null$' | \
while read -r name current_workspace; do
    if [ "${current_workspace}" != "null" ] ; then
        i3-msg workspace number "${current_workspace}"
    fi
done
