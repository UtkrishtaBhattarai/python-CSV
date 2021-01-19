import pandas as pd
mydata={
    "SN":[1,2],
    "name":["apple","ball"],
    "price":[100,200]
}

var=pd.DataFrame(mydata)
print(var)