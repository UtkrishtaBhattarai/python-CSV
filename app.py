from os import path
import csv
counts={}
class MyClass():
    def __init__(self,filepath):
        self.filepath=filepath 
    def validatefilepath(self):
        return True if path.exists(self.filepath) and self.filepath.endswith(".csv") else False
    def getthecolumn(self):
        if self.validatefilepath() is True:
            searchval=input("Please enter search value:")
            with open(self.filepath,'r',newline="") as file:
                reader=csv.reader(file)
                list_of_column_names=next(reader) 
                print({"Number of headers in csv":len(list_of_column_names),"data":list_of_column_names}) 
                if searchval in list_of_column_names:
                    index=int(list_of_column_names.index(searchval))
                    for data in reader:
                        counts[data[index]] = counts.get(data[index], 0) + 1
                    print(counts)
                else:
                    print("Column Not present")
        else:
            print("Path Not Valid")
            
filepath=input("Please enter file path: ")
myclass=MyClass(filepath)
myclass.getthecolumn()