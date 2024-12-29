#!/usr/bin/python3

"""
Script that uses scrot to take snapshots.
"""

import screeninfo
import subprocess
from datetime import datetime
import time
import sys
import os

CAPTURES_FOLDER = os.path.expanduser("~/Imagenes/captures")
WAIT_TIME = 0.4


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
    options_joined = " ".join(options)
    string = (
        "list=("
        + options_joined
        + ');selected=$(printf "%s\n" "${list[@]}" | rofi -l '
        + str(len(options))
        + ' -dmenu -p "Select: ");echo $selected'
    )
    return get_cmd_output(string)


def get_screen_size(n_screen):
    """
    Get size of any selected screen, or all
    if receives -1.
    """
    x = 0
    y = 0
    if n_screen < 0:
        width = 0
        height = 0
        for m in screeninfo.get_monitors():
            width += m.width
            if height < m.height:
                height = m.height
    else:
        monitors = screeninfo.get_monitors()
        if len(monitors) > n_screen:
            x = monitors[n_screen].x
            y = monitors[n_screen].y
            width = monitors[n_screen].width
            height = monitors[n_screen].height
        else:
            width = height = -1

    return x, y, width, height


def select_window():
    """
    Shows two options, current window o to select
    one on click.
    """
    options = ["CURRENT", "SELECT"]
    result = launch_rofi(options)

    return result[0:-1]


def get_time():
    """
    Opens Rofi to enter a number.
    """
    n = launch_rofi([])
    if int(n) in range(0, 100):
        return int(n)
    else:
        return -1


# def select_window():
# """
# Gets a list of windows and shows rofi
# to select one of them. Finally it returns
# selected option.
# """
# options = ["Current"]
# other = i3.filter(nodes = [], focused = False)
# for window in other:
# try:
# this_window_title = window['window_properties']['title']
# options.append(this_window_title)
# except:
# pass

# result = launch_rofi(options)
# if result == "Current\n":
# result = result.lower()[0:-1]
# else:
# for window in other:
# try:
# this_window_title = window['window_properties']['title']
# if this_window_title == result:
# result = this_window_title
# break
# except:
# pass

# return result


def select_cmd(option):
    """
    Receives the option selected and return the
    needed command to do it.
    """
    cmd = ""
    if option == "ALL":
        _, _, width, height = get_screen_size(-1)  # -1 to get all
        cmd = f"scrot -a 0,0,{width},{height} "
    elif option == "WINDOW":
        window = select_window()
        if window == "CURRENT":
            cmd = "scrot -u "
        else:
            cmd = "scrot -s "
    elif option == "AREA":
        cmd = "scrot -s -f "
    elif option == "SCREEN":
        n_screen = len(screeninfo.get_monitors())
        options = [str(item) for item in range(n_screen)]
        selected_screen = launch_rofi(options)
        x, y, width, height = get_screen_size(int(selected_screen))
        cmd = f"scrot -a {x},{y},{width},{height} "
    elif option == "COUNTDOWN":
        n = get_time()
        if n <= 0:
            exit(0)
        else:
            cmd = f"scrot -d {n} "
    else:
        return -1

    return cmd


def format_cmd(cmd, args):
    """
    Saves screenshot depending on parameters received.
    """

    if "-p" in args:
        path = args[args.index("-p") + 1]
        if not path.split(".")[-1] in ["png", "jpg"]:
            path += ".png"
    else:
        now = datetime.now()  # current date and time
        current_time = now.strftime("%m-%d-%Y-%H-%M-%S")
        path = f"{current_time}.png"

    cmd += path
    if "-o" in args:
        cmd += f" -e pinta {path}"  # Pass to PINTA
    # Change name

    cmd += f" -e 'mv $f {CAPTURES_FOLDER}' "
    # Move to captures folder

    return cmd, path


def run_cmd(cmd):
    """
    Runs generated command.
    """
    return subprocess.check_call(f"{cmd}", shell=True)


def run():
    args = sys.argv[1:]

    options = ["ALL", "WINDOW", "AREA", "SCREEN", "COUNTDOWN"]

    result = None
    for option in options:
        if f"--{option.lower()}" in args:
            result = option
            break
    if result == None:
        result = launch_rofi(options)[0:-1]

    cmd = select_cmd(result)
    if cmd == -1:
        return 0

    cmd, path = format_cmd(cmd, args)

    time.sleep(WAIT_TIME)
    result = run_cmd(cmd)

    if not result:
        if "-c" in args:
            copy_cmd = (
                f"xclip -selection clipboard -t image/png -i {CAPTURES_FOLDER}/{path}"
            )
            run_cmd(copy_cmd)
            notify_cmd = "notify-send 'Capture saved' 'Succesfully saved on clipboard'"
        elif "-oc" in args:
            copy_cmd = (
                f"xclip -selection clipboard -t image/png -i {CAPTURES_FOLDER}/{path}"
            )
            run_cmd(copy_cmd)
            os.remove(f"{CAPTURES_FOLDER}/{path}")
            notify_cmd = "notify-send 'Capture saved' 'Succesfully saved on clipboard'"
        else:
            notify_cmd = f"notify-send 'Capture saved' 'Succesfully saved on {path}'"

        run_cmd(notify_cmd)


def main():
    run()


if __name__ == "__main__":
    main()
