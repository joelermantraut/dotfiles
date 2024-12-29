#!/usr/bin/python3

"""
Script called by Dunst to save all notifications info in a file.
"""

import sys
import os


def main():
    args = sys.argv[1:]

    if os.path.exists(os.path.expanduser("~/.config/dunst/notifications.txt")):
        with open(os.path.expanduser("~/.config/dunst/notifications.txt"), "w") as file:
            # file.write(f"{args[0]}%{args[1]}%{args[2]}%{args[3]}%{args[4]}")
            file.write(str(args))


if __name__ == "__main__":
    main()
