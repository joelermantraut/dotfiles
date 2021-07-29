#!/usr/bin/python

"""
Shows a list of engines, select one
with dmenu and search input with it.
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
    "youtube": "https://www.youtube.com/results?search_query="
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

def launch_dmenu(options, label):
    """
    Runs dmenu with given options.
    """
    options = "\n".join(options)
    string = f'echo -e "{options}" | dmenu_styled -p "{label}:"'
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
    result = launch_dmenu(engines.keys(), "Motor")
    result = result[:-1]
    # To delete last \n from dmenu
    if result == "":
        exit()

    engine = engines[result]
    result = launch_dmenu([], result)
    result = result[:-1]
    if result == "":
        exit()

    open_browser(engine, result)

def main():
    run()

if __name__ == "__main__":
    main()
