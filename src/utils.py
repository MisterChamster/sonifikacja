import pandas as pd



def get_open_close_for_chunks(datafile_path: str, chunk_size: int) -> list:
    ret_chunk_decider = []

    file_len = 0
    last_line = None
    with open(datafile_path, 'r') as file:
        for line in file:
            file_len += 1
            last_line = line
    if last_line:
        if last_line == "":
            file_len -= 1

    if chunk_size > file_len:
        raise Exception("Chunk size is bigger than number of lines in the file!!")

    whole_chunks = int(file_len/chunk_size)
    for i in range(whole_chunks):
        read_start = i*chunk_size
        loaded_chunk = pd.read_csv(datafile_path, header=None, skipinitialspace=True, skiprows=range(read_start), nrows=chunk_size)
        print(read_start, "Hello")
        print(loaded_chunk)
