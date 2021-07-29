#!/usr/bin/python
# -*- coding:utf-8 -*-

"""
This script launches dmenu passmenu utility,
enable to select a password and writes it.

It allows to select multiple fields, like
username and password. Also, when it detects
you are running on a terminal, it writes username
and password, which are common cases like Github.
"""

import os
import subprocess
from pathlib import Path
import Xlib
import Xlib.display

# Modules

respective_fields = [
    "password",
    "username",
    "website"
]
terminal_list = ["Alacritty", "konsole"]
# This means, that fields must be enter in this
# order. If there are some fields but other not,
# it can be replaced with null string.

# Global Variables

def get_cmd_output(cmd):
    """
    Runs a cmd and returns its output.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    result = output.decode()
    return result

def launch_dmenu(options):
    """
    Runs dmenu with given options.
    """
    options = " ".join(["'{}'".format(item) for item in options])
    string = 'list=(' + options + ');password=$(printf "%s\n" "${list[@]}" | dmenu_styled -p "Select: ");echo $password;'
    return get_cmd_output(string)

def get_passwords():
    """
    Gets list of paths.
    """
    pathlist = list()
    for path in Path(os.path.expanduser("~/.password-store")).rglob("*.gpg"):
        name = path.name.split(".")
        name.pop()
        name = ".".join(name)
        # Gets name without .gpg
        last_parent = path.parent.__str__().split("/")[-1]
        # Gets last parent's name
        if last_parent in ["branches", "hooks", "info", "objects", "refs"]:
            continue
            # Special folders
        elif last_parent != ".password-store":
            pathlist.append("{}({})".format(name, last_parent))
        else:
            pathlist.append(name)

    pathlist.sort()
    # Alphabetic sort
    return pathlist

def get_pass(name):
    """
    Get the pass with pass utility.
    """
    if "(" in name:
        name = name.split("(")
        basename = name[0]
        parent = name[1][:-2]
        name = "{}/{}".format(parent, basename)

    password = get_cmd_output("pass show {}".format(name))
    return password

def write_on_field(content, enter=True):
    """
    Writes the file content on the field.

    If enter is true, press Enter at the end.
    """
    get_cmd_output('xdotool type "{0}";'.format(content))
    if enter:
        get_cmd_output('xdotool key KP_Enter;')

def get_window_class():
    """
    Gets actual window class.
    """
    disp = Xlib.display.Display()
    window = disp.get_input_focus().focus

    wm_class = window.get_wm_class()

    return wm_class[0]

def run():
    """
    Runs program.
    """
    passwords = get_passwords()

    result = launch_dmenu(passwords)

    if result in ["\n", '', " "]:
        exit(0)
    # Escaped selection

    value = get_pass(result)
    value = value[:-1]
    # Deletes the last end of line character

    fields = value.split("\n")
    if len(fields) > 1:
        if get_window_class() in terminal_list:
            write_on_field(fields[0]) # Password
            write_on_field(fields[1]) # Username
            exit(0)
        else:
            value = launch_dmenu(respective_fields[:len(fields)])
            value = value[:-1]
            # Deletes the last end of line character

            if value not in respective_fields:
                exit(0)
            # Escaped selection

            value = fields[respective_fields.index(value)]

    write_on_field(value)

def main():
    run()

if __name__ == "__main__":
    main()
