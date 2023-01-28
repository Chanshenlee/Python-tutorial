# 載入 pandas 模組
from multiprocessing import Condition
import pandas as pd
# 篩選練習 - Series
# data = pd.Series([30,15,20])
# Condition=data>18
# print(Condition)
# filterData=data[Condition]
# print(filterData)

# data=pd.Series(["您好","Python","Pandas"])
# Condition=data.str.contains("P")
# print(Condition)
# filteredData=data[Condition]
# print(filteredData)
# 篩選練習 - DataFrame
data=pd.DataFrame({
    "name":["Amy","Bob","Charles"],
    "salary":[30000,50000,40000]
})
# print(data)
Condition=data["name"]=="Amy"
print(Condition)
filteredData=data[Condition]
print(filteredData)