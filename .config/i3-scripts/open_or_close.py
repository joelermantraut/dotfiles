#!/usr/bin/python

import i3
import sys

def cycle(window_title, window_class):
    windows = i3.filter(nodes=[])
    print(windows)

    for window in windows:
        try:
            actual_window_title = window['window_properties']['title']
            actual_window_class = window['window_properties']['class']

            if window_title != None and window_title == actual_window_title:
                print("OK")
            elif window_class != None and window_class == actual_window_class:
                print("OK")
        except:
            pass

if __name__ == '__main__':
    # args = sys.argv

    # cycle(args[1], args[2], args[3])
    cycle("", "Brave-browser")
