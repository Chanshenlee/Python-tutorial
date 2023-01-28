#有序可變動列表 List
grades=[12,60,15,70,90]
grades[0]=55 #把 55 放到列表中的第一個位置
print(grades)
print(grades[1:4]) # 包含第一個位置，不包含第四個位置
grades[1:4]=[] #連續刪除編列表中從編號1到編號4(不包括)的資料
print(grades)
grades=grades+[12,33,50] #原來的列表+新的列表
print(grades)
length=len(grades) #取得列表的長度
print(length)


#有序可變動列表 List 的巢狀列表
data = [[3,4,5],[6,7,8]]
data[0][0]=5
print(data[0])
print(data[0][0:2])

data[0][0:2]=[5,5,5] 
print(data[0]) #這邊主要是把[5,4]換成[5,5,5]，加上原本剩下來的5。
print(data)


#有序不可變動列表 Tuple
data=(3,4,5)
#data[0]=5 #錯誤 : Tuple的資料不可更動
print(data[2])
print(data[0:2])
