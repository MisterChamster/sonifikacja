import pandas as pd



def get_open_close_for_chunks(datafile_path: str, chunk_size: int, min_ds_val: float, max_ds_val: float) -> list:
    ret_chunk_decider = []

    file_len = 0
    with open(datafile_path, 'r') as file:
        for line in file:
            file_len += 1
            last_line = line
    if last_line:
        if last_line == "":
            file_len -= 1

    if chunk_size > file_len:
        raise Exception("Chunk size is bigger than number of lines in the file!!")

    mid_file_value = (min_ds_val+max_ds_val)/2
    whole_chunks = int(file_len/chunk_size)
    for i in range(whole_chunks):
        read_start = i*chunk_size
        # print(read_start, "Hello")
        loaded_chunk = pd.read_csv(datafile_path, header=None, names=["values"], skipinitialspace=True, skiprows=range(read_start), nrows=chunk_size)

        summ = 0
        for i in range(chunk_size):
            summ += loaded_chunk["values"][i]
        avg = summ/chunk_size

        # print("Mid value: ", mid_file_value, " Avg val: ", avg)
        if avg > mid_file_value:
            # print("Greater! ", end="")
            ret_chunk_decider.append("1")
        else:
            # print("Lower!   ", end="")
            ret_chunk_decider.append("0")
        # print(avg)
        # print(loaded_chunk)
    # print(ret_chunk_decider)
    return ret_chunk_decider


def get_peaks_x_vals(general_chunk_vals: list, chunk_size: int) -> list:
    peak_chunks = []
    i = 0
    while i<len(general_chunk_vals):
        curr_height = general_chunk_vals[i]
        j = i
        while j<len(general_chunk_vals):
            if general_chunk_vals[j] == curr_height:
                j += 1
            else:
                break

        peak_x = (i+j)/2
        peak_chunks.append(peak_x)
        i = j

    peak_xes = [int(a*chunk_size) for a in peak_chunks]
    print(peak_xes)


