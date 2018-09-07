# context manager
# A context manager, in Python, is a resource acquisition and release mechanism 
# that prevents resource leak and ensures startup and cleanup (exit) actions are always done.

import gc
import time
import pandas as pd
from contextlib import contextmanager

@contextmanager
def timer(title):
    t0 = time.time()
    yield
    print("{} in {:.0f}s".format(title, time.time() - t0))

# Preprocess credit_card_balance.csv
def process_file(num_rows = None, nan_as_category = True):
    df = pd.read_csv('file_name.csv', nrows = num_rows)
    # perform operations
    # df.transform, df.agg, df.groupby, df.drop
    gc.collect()
    return df

def main(debug = False):
    with timer("Process file"):
        df = process_file(num_rows)
        print("Pandas DataFrame shape:", df.shape)
        # sample operations
        df = df.join(df, how='left', on='ID')
        del df
        gc.collect()

if __name__ == "__main__":
    with timer("timer"):
        main()
