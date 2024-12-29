#!/usr/bin/python3

"""
Script that offers options to power off system.
"""

import subprocess


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
        + ');selected=$(printf "%s\n" "${list[@]}" | rofi -theme "~/.config/rofi/style_8.rasi" -l '
        + str(len(options))
        + ' -dmenu -p "Select: ");echo $selected'
    )
    return get_cmd_output(string)


def run_cmd(cmd):
    """
    Runs generated command.
    """
    subprocess.check_call(f"{cmd}", shell=True)


def select_cmd(option):
    if option == "💻 Shutdown":
        cmd = "systemctl poweroff"
    elif option == "🖥️ Reboot":
        cmd = "systemctl reboot"
    elif option == "💾 Lock":
        cmd = "betterlockscreen -l dim --text 'Dont touch my machine!'"
    elif option == "🖱️ Sleep":
        cmd = "systemctl suspend && betterlockscreen -l dimblur --text 'Dont touch my machine!'"
    elif option == "⌨️ Logout":
        cmd = "kill -9 -1"
    else:
        cmd = -1
        print("Wrong command")

    return cmd


def main():
    options = ["'💻 Shutdown'", "'🖥️ Reboot'", "'💾 Lock'", "'🖱️ Sleep'", "'⌨️ Logout'"]

    option = launch_rofi(options)[0:-1]

    cmd = select_cmd(option)
    if cmd == -1:
        return 0

    run_cmd(cmd)


if __name__ == "__main__":
    main()
