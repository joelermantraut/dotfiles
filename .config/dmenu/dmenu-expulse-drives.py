#!/usr/bin/python

"""
Gets a list of drives connected, uses dmenu to show
them, and select which one must be expulse. If unmount
fails, list programs using it, and closes them.
"""

import subprocess
import glob
import getpass
import os.path
import psutil

USER = getpass.getuser()
MAIN_DIR = f"/run/media/{USER}"

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
    string = f'echo -e "{options}" | dmenu_styled -p "Desmontar:"'
    return get_cmd_output(string)

def list_pendrives(main_dir):
    """
    List all mount points.
    """
    pendrives_dic = {}

    dirs = glob.glob(main_dir + "/*")
    for dirpath in dirs:
        dirname = dirpath.split("/")[-1]
        pendrives_dic[dirname] = dirpath

    return pendrives_dic

def remove_items(test_list, item):
    res = [i for i in test_list if i != item]

    return res

def get_connected_programs(path):
    """
    Get all programs PID connected to a pendrive.
    """
    result = get_cmd_output(f"fuser -c {path}")
    result = result.split(":")[-1].split(" ")
    result = remove_items(result, "")
    return result

def get_process_name(programs):
    """
    Receives list of pids and returns process names.
    """
    process_name = []

    for program in programs:
        process = psutil.Process(int(program))
        process_name.append(process.name())

    return process_name

def manage_exceptions(programs, process_name):
    """
    Gets all processes names that are using
    this pendrive, and modifies or closes them.
    """
    if "krusader" in process_name:
        HOME = os.path.expanduser('~')
        get_cmd_output(f"krusader --left {HOME}")
        get_cmd_output(f"krusader --right {HOME}")
        process_name.pop(process_name.index("krusader"))
    elif "zsh" in process_name:
        process_name.pop(process_name.index("zsh"))
    else:
        for process in range(len(process_name)):
            get_cmd_output(f"kill -9 {programs[process]}")

def run():
    dir_dic = list_pendrives(MAIN_DIR)
    result = launch_dmenu(dir_dic)
    result = result[:-1]
    # Deletes last \n from dmenu response
    result_path = dir_dic[result]
    programs = get_connected_programs(result_path)
    process_name = get_process_name(programs)

    manage_exceptions(programs, process_name)

    get_cmd_output(f"umount {result_path}")
    # Unmount drive

def main():
    run()

if __name__ == "__main__":
    main()
