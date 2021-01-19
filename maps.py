import fire
import csv
import os.path
from os import path
from collections import Counter
from operator import itemgetter
list_of_column_names = [] 
counts={}
d=dict()
class CSV:
    filepath=input("Please enter the file path: ")
    if path.exists(filepath) and filepath.endswith('.csv'):
        column_check=input("Enter Column: ")
        with open(filepath,'r',newline="") as file:
            reader=csv.reader(file)
            list_of_column_names=next(reader) ##accessing headers name with next function
            print({"Number of headers in csv":len(list_of_column_names),"data":list_of_column_names}) #printing headers count and name
            if column_check in list_of_column_names:#checking if user input value is in listofcolumn
                index=int(list_of_column_names.index(column_check))#getting the index of list where columncheck is present
                for data in reader: #looping only if user input is in list of column
                    counts[data[index]] = counts.get(data[index], 0) + 1 #loops and stores index into key and its count to value
                print(counts)# if item is only one then value will be 1 and 1 will be added on each same item found
            else:
                print("Column Not present")
    else:
        print("File doesnot exist or wrong file selected")
    exit()
if __name__ == '__main__':
  fire.Fire(CSV)
