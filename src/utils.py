import pandas as pd



def get_line_count(datafile_path: str):
    line_count = 0
    with open(datafile_path, 'r') as file:
        for line in file:
            line_count += 1
            last_line = line
    if last_line:
        if last_line == "":
            line_count -= 1
    return line_count


def get_open_close_for_chunks(datafile_path: str, chunk_size: int, min_ds_val: float, max_ds_val: float) -> list:
    ret_chunk_decider = []

    line_count = get_line_count(datafile_path)
    if chunk_size > line_count:
        raise Exception("Chunk size is bigger than number of lines in the file!!")

    # Equated, not fixed in case non-normalized data comes in
    mid_file_value = (min_ds_val+max_ds_val)/2
    whole_chunks_count = int(line_count/chunk_size)

    # Analyzing chunks
    for i in range(whole_chunks_count):
        read_start = i*chunk_size
        loaded_chunk = pd.read_csv(datafile_path, header=None, names=["values"], skipinitialspace=True, skiprows=range(read_start), nrows=chunk_size)

        summ = 0
        for i in range(chunk_size):
            summ += loaded_chunk["values"][i]
        avg = summ/chunk_size

        if avg > mid_file_value:
            ret_chunk_decider.append("1")
        else:
            ret_chunk_decider.append("0")
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
    return peak_xes


def get_peaks_ys(peak_xes: list, first_peak: bool) -> list:
    peak_ys = []
    for i in range(len(peak_xes)):
        if i%2:
            peak_ys.append(0.2)
        else:
            peak_ys.append(0.8)
    return peak_ys
