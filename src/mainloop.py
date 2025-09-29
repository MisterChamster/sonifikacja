from src.askers import ask_path_filedialog
import pandas as pd



def mainloop():
    print("Choose data file in txt format:")
    datafile_path = ask_path_filedialog("f", "Choose data txt file")
    if not datafile_path.endswith(".txt"):
        print("Wrong file format")
        return
    print(datafile_path)

    loaded_boi = pd.read_csv(datafile_path, sep=" \n", engine='python', header=None)
    # print(type(loaded_boi))
    print(loaded_boi)
