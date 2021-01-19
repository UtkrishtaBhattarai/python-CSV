import fire
import csv
import os.path
import collections
from os import path
list_of_column_names = [] 
users = collections.Counter()

class CSV:
    filepath=input("Please enter the file path: ")
    if path.exists(filepath) and filepath.endswith('.csv'):
        column_check=input("Enter Column: ")
        with open(filepath,'r',newline="") as file:
            reader=csv.reader(file)
            list_of_column_names=next(reader)
            if column_check in list_of_column_names:
                index=int(list_of_column_names.index(column_check))
                for data in reader:
                    users[data[index]] += 1
                print(dict(users))
            else:
                print("Column Not present")
    else:
        print("File doesnot exist or wrong file selected")
    exit()

if __name__ == '__main__':
  fire.Fire(CSV)