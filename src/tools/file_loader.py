import pandas as pd
from dataclasses import dataclass
from typing import List

@dataclass
class DFInfo:
    n_cols: int
    n_rows: int

@dataclass
class DFNullCounts:
    col_name: str
    type_name: str
    null_count: int
    unique_count: int
# @dataclass
# class DFStats:
#
# @dataclass
# class DFSchema:

def read_csv_file(path:str) -> pd.DataFrame:
    if path.endswith(".csv"):
        df =  pd.read_csv(path)
    elif path.endswith(".gz"):
        df= pd.read_csv(path, compression="gzip")
    df_info = df.describe()
    print(df_info)

if __name__ == "__main__":
    result = read_csv_file("/Users/abhisheknarayanchaudhury/Desktop/GenAIProjects/Learn Langchain/DQLib/data/listings.csv.gz")
