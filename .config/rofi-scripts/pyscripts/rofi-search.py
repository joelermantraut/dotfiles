#!/usr/bin/python3

"""
Shows a list of engines, select one
with rofi and search input with it.
"""

import subprocess
import threading
import os

engines = {
    "archwiki": "https://wiki.archlinux.org/index.php?search=",
    "duckduckgo": "https://duckduckgo.com/?q=",
    "facebook": "https://www.facebook.com/search/top?q=",
    "github": "https://github.com/search?q=",
    "google": "https://www.google.com/search?q=",
    "googleimages": "https://www.google.com/search?hl=en&tbm=isch&q=",
    "mercadolibre": "https://listado.mercadolibre.com.ar/",
    "stackoverflow": "https://stackoverflow.com/search?q=",
    "translate": "https://translate.google.com/?sl=auto&tl=en&text=",
    "wayback": "https://web.archive.org/web/*/",
    "wikipedia": "https://en.wikipedia.org/wiki/",
    "wolfram": "https://www.wolframalpha.com/input/?i=",
    "youtube": "https://www.youtube.com/results?search_query=",
}
BROWSER = "brave"


def get_cmd_output(cmd):
    """
    Runs a cmd and returns its output.
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    (output, _) = p.communicate()
    result = output.decode()
    return result


def launch_rofi(options, label):
    """
    Runs rofi with given options.
    """
    len_engines = len(engines)

    options = "\n".join(options)
    string = f'echo -e "{options}" | rofi -dmenu -i -l {len_engines if len_engines <= 15 else 15} -p "{label}:"'
    return get_cmd_output(string)


def run_process(cmd):
    """
    Runs command in another thread.
    """
    os.system(cmd)


def open_browser(engine, link):
    """
    Opens the browser with the given link.
    """
    global BROWSER

    cmd = "{} '{}'".format(BROWSER, engine + link)
    thread = threading.Thread(target=lambda: run_process(cmd))
    thread.start()


def run():
    result = launch_rofi(engines.keys(), "Motor")
    result = result[:-1]
    # To delete last \n from rofi
    if result == "":
        exit()

    engine = engines[result]
    result = launch_rofi([], result)
    result = result[:-1]
    if result == "":
        exit()

    open_browser(engine, result)


def main():
    run()


if __name__ == "__main__":
    main()
