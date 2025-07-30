from src.askers import ask_path_filedialog



def mainloop():
    print("Choose data file in txt format:")
    datafile_path = ask_path_filedialog("f", "Choose data txt file")
    print(datafile_path)
