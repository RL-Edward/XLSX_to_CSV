# XLSX_to_CSV

XLSX_to_CSV is a simple program to convert ALL .xlsx files to .csv within a specified directory.
Output .csv will be placed in the same directory as source .xlsx files.

## Getting Started

Clone or download the repository to a location on your machine.

### Prerequisites

```
Python 3.7
pandas
xlrd
```

### Installing

Ensure you have a Python 3 enviroment with the pandas and xlrd modules.

If you have Python 3 in your PATH, you can do the following to run the program where TGT_Directory 
is the source directory of your .xlsx files.

```
Open a console in the folder where the .py files are located.
python3 XLSX_to_CSV.py TGT_Directory
```

If you are using an IDE, you will need to either run the console on the IDE or hard code the source directory into the path variable.

XLSX_to_CSV.py:
```
if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        path = None

    if path != None:
        XLSX_to_CSV.convert_csvs(path)
    else:
        print("No path provided.") 
```

## Authors

* **Ruben Lopez** - *Initial work* - [RL-Edward](https://gist.github.com/RL-Edward)
