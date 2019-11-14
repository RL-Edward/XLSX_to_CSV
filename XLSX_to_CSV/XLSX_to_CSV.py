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
                #cls.__convert_csv(xlsx_file_name, path)
                
        else:
            print("Path does not exist.")

    @classmethod
    def __convert_csv(cls, *args, **kwargs):
        file_path = kwargs["File Path"]

        try:
            frame = pd.read_excel(file_path, index_col=None)
            file_path = file_path.replace(".xlsx", ".csv")
            frame.to_csv(file_path, encoding='utf-8', index=False)
        except:
            print("%s could not be found in %s" % (file_name, path))

if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        path = None

    if path != None:
        XLSX_to_CSV.convert_csvs(path)
    else:
        print("No path provided.") 
    