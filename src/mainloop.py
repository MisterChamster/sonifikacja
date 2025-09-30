from src.askers import ask_path_filedialog
from src.utils import get_open_close_for_chunks
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
# So, a border reasonable num of putting rows in hist with loaded_boi.hist()
# is around 25k which is 15 seconds. More than that will be a slog and we
# don't want that.



def mainloop() -> None:
    print("Choose data file in txt/csv format:")
    datafile_path = ask_path_filedialog("f", "Choose data txt file")
    if not datafile_path.endswith(".txt"):
        print("Wrong file format")
        return
    print(datafile_path)

    # Load file
    loaded_boi = pd.read_csv(datafile_path, header=None, names=["values"], skipinitialspace=True)
    # print(loaded_boi)

    # Data segmentation - averaging samples into n-sample bins
    # n = 10
    # loaded_boi = loaded_boi.groupby(loaded_boi.index // n).mean()

    # Get pandas.Series objects and convert them to floats. There was a 
    # FutureWarning regarding a blatant type casting to float :((
    min_ds_val = loaded_boi.min()
    min_ds_val = float(min_ds_val["values"])
    max_ds_val = loaded_boi.max()
    max_ds_val = float(max_ds_val["values"])
    diff = max_ds_val-min_ds_val

    # Normalization xnorm = (x-xmin)\(xmax-xmin)
    # Comment this line get non-normalized data
    loaded_boi = loaded_boi.map(lambda x: (x-min_ds_val)/(diff))
    print(loaded_boi)

    get_open_close_for_chunks(datafile_path, min_ds_val, max_ds_val, 2000)

    row_count = len(loaded_boi.index)
    print(row_count)

    # plt.plot(loaded_boi.index, loaded_boi["values"], linestyle="None", marker="o")
    plt.scatter(loaded_boi.index, loaded_boi["values"], s=1)  # s = point size

    plt.xlabel('Um whatever idk yet. Time? I guess time. I gotta check frequency of the measurement i think.')
    plt.ylabel('Value')
    plt.gca().xaxis.set_major_locator(MultipleLocator(20000))
    plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))
    plt.title('A VERY Cool Chart')
    # plt.show()
