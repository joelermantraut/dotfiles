#!/usr/bin/python

"""
Script called by Dunst to save all notifications info in a file.
"""

import sys
import os

def run():
    args = sys.argv[0:-2]

    with open(os.path.expanduser("~/.config/dunst/notifications.txt"), "w") as file:
        file.write(f"{args[0]}%{args[1]}%{args[2]}%{args[3]}%{args[4]}")

def main():
    run()

if __name__ == "__main__":
    main()
