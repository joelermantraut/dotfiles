#!/usr/bin/python3

"""
This scripts shows all bookmarks store in Brave
Browser bookmarks file and allows to select one
to open it. Also, if you type "links" and press
enter, then dmenu will be launched again showing
links of bookmarks instead of their names.
"""

import subprocess
import threading
import os.path
import json
import sys  # Imports

# Needs to export bookmarks to html file because firefox stores
# them in a sqlite file
# https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data
BOOKMARKS_FILEPATH = os.path.expanduser("~/.mozilla/bookmarks.html")
BROWSER = "firefox"

# Variables


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
    options = "\n".join(options)
    string = f'echo -e "{options}" | rofi -dmenu -i -p "Marcadores:" -l 15'
    return get_cmd_output(string)


def get_bookmarks(obj):
    """
    Gets a JSON object and returns all
    bookmarks on it. Its recursively.
    """
    dic = {}

    for item in obj:
        try:
            new_obj = item["children"]
            dic.update(get_bookmarks(new_obj))
        except KeyError:
            name = item["name"]
            dic[name] = item["url"]

    return dic


def read_bookmarks(path):
    """
    Reads bookmars from file and
    returns it as a list.
    """
    with open(path, "r") as file:
        content = file.read()

    obj = json.loads(content)
    roots = obj["roots"]

    obj = roots["bookmark_bar"]["children"]
    return get_bookmarks(obj)


def get_link(bookmarks, names, result):
    """
    Receives a name or a link and return
    the link associated.
    """
    if names:
        link = bookmarks[result]
    else:
        link = result

    return link


def run_process(cmd):
    """
    Runs command in another thread.
    """
    os.system(cmd)


def open_browser(link):
    """
    Opens the browser with the given link.
    """
    global BROWSER

    cmd = "{} '{}'".format(BROWSER, link)
    thread = threading.Thread(target=lambda: run_process(cmd))
    thread.start()


def main():
    global BOOKMARKS_FILEPATH

    names = True
    bookmarks = read_bookmarks(BOOKMARKS_FILEPATH)
    result = launch_rofi(bookmarks.keys())

    while result in ["#links\n", "#names\n"]:
        if result == "#links\n":
            names = False
            result = launch_rofi(bookmarks.values())
        elif result == "#names\n":
            names = True
            result = launch_rofi(bookmarks.keys())

    if result in ["\n", "", " "]:
        exit(0)
    else:
        result = result[:-1]
    # Added by Dmenu
    if len(result.split("\n")) >= 2:
        result = result.split("\n")

    link = list()
    if type(result) is list:
        for item in result:
            link.append(get_link(bookmarks, names, item))
    else:
        link = get_link(bookmarks, names, result)

    if type(link) is list:
        for item in link:
            open_browser(item)
    else:
        open_browser(link)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if "--browser" in sys.argv:
            index = sys.argv.index("--browser")
            BROWSER = sys.argv[index + 1]
        if "--bookmarks" in sys.argv:
            index = sys.argv.index("--bookmarks")
            BOOKMARKS_FILEPATH = sys.argv[index + 1]

    main()
