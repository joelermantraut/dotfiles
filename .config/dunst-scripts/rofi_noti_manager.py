#!/usr/bin/python3

"""
Shows a rofi notifications history.
"""

import os.path
import subprocess

FILE_PATH = os.path.expanduser("~/.config/dunst/notifications.txt")
ROFI_THEME = os.path.expanduser("~/.config/rofi/style_8.rasi")
SEPARATOR = ","


def get_cmd_output(cmd):
    """
    Runs a cmd and returns its output.
    """
    p = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, shell=True, executable="/bin/bash"
    )
    (output, _) = p.communicate()
    result = output.decode()
    return result


def launch_rofi(options):
    """
    Runs rofi with given options.
    """
    options = "~".join(["'{}'".format(item) for item in options])
    string = (
        "list=("
        + options
        + ');password=$(printf "%s\n" "${list[@]}" | \
             rofi -sep "~" -markup-rows -dmenu -p "Select: " -theme '
        + ROFI_THEME
        + ");echo $password;"
    )
    return get_cmd_output(string)


def open_noti_file(file_path):
    """
    Opens the file and returns the content.
    """
    with open(file_path, "r") as file:
        content = file.readlines()

    return content


def format_notis(options):
    """
    Receives a list of notifications saved in a file,
    and formats it to be shown in rofi.
    """
    notis = []

    for option in options:
        parts = option.split(SEPARATOR)
        if parts[3]:
            string = (
                f"<b>{parts[3]}{parts[0]}:{parts[1]} - <i>{parts[4]}</i></b>{parts[2]}"
            )
        else:
            string = f"<b>{parts[0]}:{parts[1]} - <i>{parts[4]}</i></b>{parts[2]}"
        notis.append(string)

    return notis


def run():
    options = open_noti_file(FILE_PATH)
    notis = format_notis(options)
    result = launch_rofi(notis)

    content = result.split("</b>")[-1]
    return subprocess.check_call(
        f"echo '{content}' | xclip -selection clipboard", shell=True
    )


def main():
    run()


if __name__ == "__main__":
    main()
