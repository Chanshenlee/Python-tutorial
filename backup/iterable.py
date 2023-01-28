# Iterable 資料型態
# 字串、列表、集會、字典


# for 迴圈
# for 變數名稱 in 可疊代的資料
from unittest import result


for x in [3,5,2]: #列表list
    print(x)
for x in "abc":   #字串
    print(x)
for x in {"a","test", 3, 10}: #集合
    print(x)
for x in {"a":3,"x":5}: #字典
    print(x)
dic={"a":3,"x":5} #如果要印出key-value可以這麼寫
for key in dic:
    print(key)
    print(dic[key])

# 內建函式
# 放列表、集合、字典都可以

# max(可疊代資料) 找最大

result=max([10,2,30,1]) #列表 
print(result)
result=max("abc")
print(result)
# sorted(可疊代資料) 由小到大排序，並用列表的方式回傳
result=sorted("cba")
print(result)
result=sorted({10,2,100,-5})
print(result)
