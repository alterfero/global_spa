__author__ = 'thor'

import glob
import pickle
import pandas as pd


def df_aggregated_from_loaded_files_matching_pattern(
        data_file_pattern,
        data_loader=pickle.load,
        pre_aggregate_processor=lambda x: x):
    file_generator = glob.iglob(data_file_pattern)
    if data_loader is None:
        return file_generator  # for debugging purposes: You just want to have a peep before processing
    else:
        reduce(lambda x, y: pd.concat([x, pre_aggregate_processor(data_loader(y))]),
            file_generator, pd.DataFrame()) \
            .reset_index(drop=True)


