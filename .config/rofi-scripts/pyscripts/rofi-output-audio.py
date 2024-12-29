#!/usr/bin/python3

"""
Rofi script with which select output audio source.
"""

import subprocess


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
    options = " ".join(["'{}'".format(item) for item in options])
    string = (
        "list=("
        + options
        + ');password=$(printf "%s\n" "${list[@]}" | rofi -dmenu -i -l 2 -p "Select: ");echo $password;'
    )
    return get_cmd_output(string)


# def get_outputs(cmd_output):
# """
# Gets command output as string and parses it.
# """
# outputs = []
# for line in cmd_output.split("\n"):
# if "name" in line:
# outputs.append(line.split(".")[-1][:-1])

# return outputs


def run():
    # cmd_output = get_cmd_output("pacmd list-sinks | grep -e 'name:' -e 'index:'")
    # outputs = get_outputs(cmd_output)
    outputs = ["lineout", "headphones"]

    result = launch_rofi(outputs)

    get_cmd_output("pacmd set-sink-port 1 analog-output-{}".format(result))


def main():
    run()


if __name__ == "__main__":
    main()
