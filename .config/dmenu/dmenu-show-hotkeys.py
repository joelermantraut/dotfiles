#!/usr/bin/python

"""
Dmenu script that show hotkeys from a file.

This receives only one parameter, which is
the file where to take hotkeys list.
If there is no parameter, it quits.
"""

import subprocess
import sys

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
    options = "\n".join(options)
    string = f'echo -e "{options}" | dmenu_styled -p "Atajos:" -l 20'
    return get_cmd_output(string)

def show_list(file_content):
    """
    Shows all lines in dmenu.
    """
    _ = launch_dmenu(file_content)

def run():
    if sys.argv == 1:
        exit(1)

    filepath = sys.argv[1]
    with open(filepath, "r") as file:
        lines = file.readlines()
        lines = [line.replace("\n", "") for line in lines]
        show_list(lines)

def main():
    run()

if __name__ == "__main__":
    main()
