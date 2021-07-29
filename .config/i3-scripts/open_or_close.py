#!/usr/bin/python

import i3
import sys

def cycle(window_exe, window_title, window_class):
    current = i3.filter(nodes=[], focused=True)
    current_title = current[0]["window_properties"]["title"]
    current_class = current[0]["window_properties"]["class"]

    print(current)

    # if current_title == window_title or current_class == window_class:
        # return
    # else:
        # other = i3.filter(nodes=[], focused=False)
        # for window in other:
            # try:
                # this_window_title = window['window_properties']['title']
                # this_window_class = window['window_properties']['class']
                # if this_window_class == window_class or this_window_title == window_class:
                    # i3.focus(con_id=window['id'])
                    # return
            # except:
                # pass

    # i3.command('exec', window_exe)

if __name__ == '__main__':
    # args = sys.argv

    # cycle(args[1], args[2], args[3])
    cycle("", "", "")
