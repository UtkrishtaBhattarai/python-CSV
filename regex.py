import csv
from os import path
list_of_column_names=[] 
counts={}

class CSV:
    def __init__(self):
        filepath=input("Please enter the file path: ")
        if path.exists(filepath) and filepath.endswith('.csv'):
            column_check=input("Enter Column: ")
            with open(filepath,'r',newline="") as file:
                reader=csv.reader(file)
                list_of_column_names=next(reader) 
                print({"Number of headers in csv":len(list_of_column_names),"data":list_of_column_names}) 
                if column_check in list_of_column_names:
                    index=int(list_of_column_names.index(column_check))
                    for data in reader:
                        counts[data[index]] = counts.get(data[index], 0) + 1
                    print(counts)
                else:
                    print("Column Not present")
        else:
            print("File doesnot exist or wrong file selected")  


                                                                                                        