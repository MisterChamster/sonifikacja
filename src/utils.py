import pandas as pd
from math import floor



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


def get_peak_coordinates (datafile_path: str, chunk_size: int, min_ds_val: float, max_ds_val: float) -> list:
    ret_peaks_coords = []

    line_count = get_line_count(datafile_path)
    print("Line count: ", line_count)
    if chunk_size > line_count:
        raise Exception("Chunk size is bigger than number of lines in the file!!")

    # Equated, not fixed in case non-normalized data comes in
    mid_file_value = (min_ds_val+max_ds_val)/2
    whole_chunks_count = int(line_count/chunk_size)
    chunk_avgs_on_level = []
    last_chunk_level = None

    # Analyzing chunks
    i = 0
    while i<whole_chunks_count:
        # Load
        read_start = i*chunk_size
        loaded_chunk = pd.read_csv(datafile_path, header=None, names=["values"], skipinitialspace=True, skiprows=range(read_start), nrows=chunk_size)

        # Get average height in chunk
        summ = 0
        for j in range(chunk_size):
            summ += loaded_chunk["values"][j]
        avg = summ/chunk_size

        # Check level of average chunk height
        if avg > mid_file_value:
            current_chunk_level = 1
        else:
            current_chunk_level = 0

        # Handle first chunk
        if last_chunk_level is None:
            chunk_avgs_on_level.append(avg)
            last_chunk_level = current_chunk_level

        # If on the same level as last one
        elif current_chunk_level == last_chunk_level:
            chunk_avgs_on_level.append(avg)
            last_chunk_level = current_chunk_level

        # If different levels
        elif current_chunk_level != last_chunk_level:
            # Get middle chunk index
            level_len = len(chunk_avgs_on_level)
            first_chunk_on_curr_level = i-level_len
            last_chunk_on_curr_level = i-1
            mid_chunk = (first_chunk_on_curr_level+last_chunk_on_curr_level)/2
            # print(mid_chunk)

            # Get middle chunk avg height
            if mid_chunk == int(mid_chunk):
                mid_chunk_avg_height = chunk_avgs_on_level[floor(level_len/2)]
            else:
                tmp1 = chunk_avgs_on_level[int(level_len/2)]
                tmp2 = chunk_avgs_on_level[int(level_len/2)-1]
                mid_chunk_avg_height = (tmp1+tmp2)/2
            # print("MIDASSSSSS: ", mid_chunk_avg_height)

            mid_chunk_midpoint_x = mid_chunk*chunk_size
            ret_peaks_coords.append([mid_chunk_midpoint_x, mid_chunk_avg_height])


            last_chunk_level = current_chunk_level
            chunk_avgs_on_level = [avg]

        i += 1

    return ret_peaks_coords
