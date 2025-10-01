import os
from tkinter import filedialog



def ask_path_filedialog(type, message):
    original_path = os.getcwd()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    os.chdir(desktop_path)

    sel_path = ""
    if type == "f":
        sel_path = filedialog.askopenfilename(title=message)
    elif type == "d":
        sel_path = filedialog.askdirectory(title=message)

    os.chdir(original_path)
    return sel_path


def ask_normalize():
    rets_dict = {"y": 1,
                 "n": 0}

    while True:
        print("Do You want to normalize the data? (y/n)\n" \
            ">> ", end="")
        asker = input()

        if asker in rets_dict:
            return rets_dict[asker]
        else:
            print("Incorrect input.\n\n")
