import fire
import os.path
import os
import csv
list_of_column_names=[]
class Calculator(object):
    
    def double(self, number):
        return 2 * number

    def getheaders(self):
        with open("users.csv",'r',newline="") as file:
            reader=csv.reader(file)
            writer = csv.writer(file)
            for rows in reader:
                list_of_column_names.append(rows)
            return list_of_column_names[0]

    def checkvalidpath(self,path):
        self.path=path
        if os.path.exists(path):
            print ("File exists")
        else:
            print ("File or folder exist")

    def getuserdata(self,filepath):
        with open(filepath, 'r') as file:
            reader = csv.reader(file)
            column_check=input("Enter column: ").lower()

        if column_check==list_of_column_names[0][0]:
            for rows in reader:
                list1.append(rows[0].split(list_of_column_names[0][0]))
                d = {x:list1.count(x) for x in list1}
            print(d)

        elif column_check==list_of_column_names[0][1]:
            for rows in reader:
                list1.append(rows[1])
                d = {x:list1.count(x) for x in list1}
            print (d)
                    

        elif column_check==list_of_column_names[0][2]:
            for rows in reader:
                list1.append(rows[2])
                d = {x:list1.count(x) for x in list1}
            print (d)
        else:
            print("Please enter valid column name")
        


    def getusername(self,name):
        self.name=name
        return name +" "+"is your name"



    def enterpath(self,path):
        self.path=path
        if os.path.exists(path):
            os.chdir(os.path.expanduser(path))
        else:
            print ("File or folder doesnt exist")

if __name__ == '__main__':
  fire.Fire(Calculator)