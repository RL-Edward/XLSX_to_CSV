import pandas as pd
import os
import sys
from Threader import Threader
from collections import OrderedDict


# TGT dir
# "C:\Users\Edward\Documents\Work\SI Data"

class XLSX_to_CSV:
    @classmethod
    def convert_csvs(cls, path):
        if os.path.exists(path):
            path_files = os.listdir(path)
            xlsx_files = [file_name for file_name in path_files if ".xlsx" in file_name] 
            jobs = OrderedDict()
            jobs[cls.__convert_csv] = []
            for xlsx_file_name in xlsx_files:
                jobs[cls.__convert_csv].append({"File Path": os.path.join(path, xlsx_file_name)})   
            Threader.threads(jobs)                
        else:
            print("Path does not exist.")

    @classmethod
    def __convert_csv(cls, *args, **kwargs):
        file_path = kwargs["File Path"]
        file_name = os.path.basename(file_path)
        try:
            frame = pd.read_excel(file_path, index_col=None)
            frame = cls.__remove_invalid_characters(frame)
            frame = cls.__rename_duplicate_columns(frame)
            file_path = file_path.replace(".xlsx", ".csv")
            frame.to_csv(file_path, encoding='utf-8', index=False)
            print("Converted %s Successfully." % file_name)
        except:
            print("Could not convert %s." % file_name)

    @classmethod
    def __remove_invalid_characters(cls, frame):
        for header in frame.columns.values:
            frame.rename(columns={header:header.replace(u"\u2122", '')}, inplace=True)
        return frame

    @classmethod
    def __rename_duplicate_columns(cls, frame):
        prev_col_name = None
        for col_name in list(frame.columns.values):
            if "(abs)" in col_name:
                frame.rename(columns={col_name:prev_col_name + " (abs)"}, inplace=True)
            prev_col_name = col_name 
        
        return frame


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        path = None

    if path != None:
        XLSX_to_CSV.convert_csvs(path)
    else:
        print("No path provided.") 
    