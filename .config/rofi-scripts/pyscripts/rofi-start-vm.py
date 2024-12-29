#!/usr/bin/python3

"""
Script which show available VirtualBox Machines and allows
to start one of them.
"""

import subprocess

# Imports

CMD_GET_VMS = "VBoxManage list vms"
CMD_RUN_VM = "VBoxManage startvm '{0}'"
# Commands


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
    rofi_options = " ".join(["'{}'".format(item) for item in options])
    string = (
        "list=("
        + rofi_options
        + ');password=$(printf "%s\n" "${list[@]}" | rofi -dmenu -i \
            -l '
        + str(len(options))
        + ' -p "Select: ");echo $password;'
    )
    return get_cmd_output(string)


def get_vms():
    """
    Run a cmd and get a list of VMs.
    """
    result = get_cmd_output(CMD_GET_VMS)
    vms = result.split("\n")[0:-1]
    for vm_index in range(len(vms)):
        vms[vm_index] = vms[vm_index].split(" {")[0].replace('"', "")

    return vms


def run():
    vms = get_vms()

    result = launch_rofi(vms)[0:-1]
    # To delete \n
    if result not in vms:
        exit(1)

    get_cmd_output(CMD_RUN_VM.format(result))


def main():
    run()


if __name__ == "__main__":
    main()
