#!/usr/bin/python

"""
Script that uses scrot to take snapshots.
"""

import screeninfo
import subprocess
import sys
import i3

def get_cmd_output(cmd):
    """
    Runs a cmd and returns its output.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    result = output.decode()
    return result

def launch_rofi(options):
    """
    Runs rofi with given options.
    """
    options_joined = " ".join(options)
    string = 'list=(' + options_joined + ');selected=$(printf "%s\n" "${list[@]}" | rofi -l ' + str(len(options))  + ' -dmenu -p "Select: ");echo $selected'
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

    return result

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
    if option == "ALL\n":
        _, _, width, height = get_screen_size(-1) # -1 to get all
        cmd = f"scrot -a 0,0,{width},{height} "
    elif option == "WINDOW\n":
        window = select_window()
        if window == "CURRENT":
            cmd = "scrot -u "
        else:
            cmd = "scrot -s "
    elif option == "AREA\n":
        cmd = "scrot -s -f"
    elif option == "SCREEN\n":
        n_screen = len(screeninfo.get_monitors())
        options = [str(item) for item in range(n_screen)]
        selected_screen = launch_rofi(options)
        x, y, width, height = get_screen_size(int(selected_screen))
        cmd = f"scrot -a {x} {y} {width} {height}"
    elif option == "COUNTDOWN\n":
        cmd = f"scrot -d 5 "
    else:
        return -1

    return cmd

def format_cmd(cmd, args):
    """
    Saves screenshot depending on parameters received.
    """
    if "-c" in args:
        pass # HOW?
    if "-p" in args:
        path = args[args.index("-p") + 1]
        cmd += path
        if "-s" in args:
            cmd += f" -e {path}" # Pass to PINTA

    return cmd

def run_cmd(cmd):
    """
    Runs generated command.
    """
    print(cmd)
    # print(subprocess.check_call(f"{cmd}", shell = True))

def run():
    args = sys.argv[0:-2]

    options = [
        "ALL",
        "WINDOW",
        "SECTION",
        "SCREEN",
        "COUNTDOWN"
    ]

    result = launch_rofi(options)

    cmd = select_cmd(result)
    if cmd == -1:
        return 0

    cmd = format_cmd(cmd, args)

    run_cmd(cmd)

def main():
    run()

if __name__ == "__main__":
    main()
