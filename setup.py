""" Hot Swap themes for suckless terminal """
from __future__ import print_function
import os
import sys
import re
from config_manager import ConfigManger
REGEX = r"static const char \*colorname\[\] = {(.*)"

def main_func():
    """ Primary function where program begins """

    if not os.path.isdir('./themes'):
        print(
            "\nThis program modifies and extracts information from \n" +
            "several files in your st installation to allow for \n" +
            "easier theming. Use this application at your own risk\n")
        if yes_no_prompt("Y", "N", "No themes folder is in current directory. Make one", False):
            os.mkdir("themes")
            color_info = get_deliminator_content("config.h", re.compile(REGEX, re.DOTALL))
            write_to_file("./themes/original.txt", color_info)
            print("original theme added to theme folder")
        else:
            sys.exit(1)
    else:
        print("exists!")


def yes_no_prompt(yes_str, no_str, msg_str, is_recurse):
    """ Read input that gives a binary yes, no option and executes function,
    exits, or recurses on input"""
    ret = False

    if not is_recurse:
        print(msg_str + f" {yes_str}/{no_str}" + "?: ", end=" ")
    answer = input("")
    if answer.upper() == yes_str:
        ret = True
    elif answer.upper() == no_str:
        ret = False
    else:
        print(f"Please input {yes_str} or {no_str}")
        ret = yes_no_prompt(yes_str, no_str, msg_str, True)
    return ret

def get_deliminator_content(filename, regex):
    """ Returns a string with the regex match between that and deliminator """
    arr_content = ""
    between_delimiter = False
    on_delimiter = False
    for _i, line in enumerate(open(filename, 'r')):
        #print(on_delimiter)
        for _match in re.finditer(regex, line):
            between_delimiter = True
            on_delimiter = True
        if between_delimiter and not on_delimiter:
            if line.find('}') != -1:
                between_delimiter = False
            else:
                arr_content = arr_content + line
        on_delimiter = False
    return arr_content


def write_to_file(filename, text):
    """ Write text to a file and close """
    _f = open(filename, "w+")
    _f.write(text)
    _f.close()








if __name__ == "__main__":
    main_func()
