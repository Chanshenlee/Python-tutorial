# 網路連線
"""import urllib.request as request
src = "https://www.shu.edu.tw/"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") #取得世新大學網站的原始碼
print(data)"""
# 串接、擷取公開資料
import urllib.request as request
import json
src = "https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
# 將公司名稱列表出來
clist = data["result"]["results"]
with open("data.txt","w",encoding="utf-8") as file:
    for company in clist:
        file.write(company["公司名稱"]+"\n")