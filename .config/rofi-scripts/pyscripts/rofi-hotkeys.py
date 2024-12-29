#!/usr/bin/python3

"""
Shows a list of hotkeys files, select one
with rofi and show it in PDF viewer.
"""

import subprocess
import glob
import os

PDF_VIEWER = "mupdf"
FILES_DIR = os.path.expanduser("~/Documentos/cheatsheets")


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
    string = (
        "list=("
        + options_joined
        + ');selected=$(printf "%s\n" "${list[@]}" | rofi -l '
        + str(len(options))
        + ' -dmenu -p "Select: ");echo $selected'
    )
    option = get_cmd_output(string)

    return options.index(option[:-1])


def run_process(cmd):
    """
    Runs command in another thread.
    """
    os.system(cmd)


def main():
    files = glob.glob(f"{FILES_DIR}/*.pdf")

    filenames = [os.path.basename(file) for file in files]

    index = launch_rofi(filenames)

    abspath = files[index]
    cmd = f"{PDF_VIEWER} {abspath}"

    run_process(cmd)


if __name__ == "__main__":
    main()
