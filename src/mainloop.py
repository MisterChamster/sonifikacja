from src.askers import ask_path_filedialog
import pandas as pd
import matplotlib.pyplot as plt
# So, a border reasonable num of putting rows in hist with loaded_boi.hist()
# is around 25k which is 15 seconds. More than that will be a slog and we
# don't want that.

# xnorm = (x-xmin)\(xmax-xmin)



def mainloop():
    print("Choose data file in txt format:")
    datafile_path = ask_path_filedialog("f", "Choose data txt file")
    if not datafile_path.endswith(".txt"):
        print("Wrong file format")
        return
    print(datafile_path)

    loaded_boi = pd.read_csv(datafile_path, header=None, names=["values"], skipinitialspace=True)
    print(loaded_boi)
    min_ds_val = loaded_boi.min()
    max_ds_val = loaded_boi.max()
    diff = max_ds_val-min_ds_val
    loaded_boi = loaded_boi.map(lambda x: float((x-min_ds_val)/(diff)))
    print(loaded_boi)

    row_count = len(loaded_boi.index)
    print(row_count)
    loaded_boi.hist(bins=int(row_count/10))

    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram of Value')
    plt.show()
