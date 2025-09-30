import pandas as pd



def get_open_close_for_chunks(datafile_path: str, chunk_size: str) -> list:
    file_len = 0
    with open(datafile_path, 'r') as file:
        for _ in file:
            file_len += 1
