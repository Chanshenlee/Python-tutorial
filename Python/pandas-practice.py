import pandas as pd
# 建立 Series

# 基本 Series 操作
# data=pd.Series([20,10,15])
# print("MAX",data.max())
# print("MEDIAN",data.median())
# data=data*2
# print(data)
# data=data==20
# print(data)
# 建立 DataFrame
data=pd.DataFrame({
    "name":["Amy","John","Bob"],
    "salary":[30000,50000,40000]
})
print(data)
# 取得特定的欄位
print(data["salary"])
# 取得特定的列
print(data)
print("==================")
print(data.iloc[0])#印出第一列
# 建立 DataFrame 操作

