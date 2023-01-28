# 集合的運算
s1={3,4,5}
print(10 not in s1) #10沒有在s1中，顯示 True
s2={4,5,6,7}
s3=s1&s2 # 交集 : 取兩個集合中，相同的資料
print(s3)
s3=s1|s2 # 聯集 : 取兩個集合中的所有資料，但不重複放
print(s3)
s3=s1-s2 # 差集 : 從 s1 中，減去和 s2 重疊的部分
print(s3)
s3=s1^s2 # 反交集 : 取兩個集合中，不重疊的部分
print(s3)

s=set("Hello") # set(字串)  把字串自動拆解，重複的部分不重複進來
print(s)
print("e" in s)
# 字典的運算 : key-value 配對
dic={"apple":"蘋果","bug":"蟲蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) #判斷 key 是否存在，value不管
print("Apple" in dic)
del dic["apple"] #刪除的時候會把整個key-value刪掉
print(dic)
dic={x:x*2 for x in [3,4,5]} #從列表的資料產生字典
print(dic)

#如果只想要print x*2的值的話
print(dic[3])
print(dic[4])
print(dic[5])


a=[1,2,3,4,5]
b=[5,10,15,20,25]
dic=dict(zip(a, b))
print(dic)