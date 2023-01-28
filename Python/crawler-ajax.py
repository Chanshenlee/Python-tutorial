# AJAX 是一個網頁前端的javacript程式技術
# 抓取 kkdays.com 的文章資料
import urllib.request as req
url="https://m.kkday.com/zh-tw/product/ajax_get_productlist?countryCd=A01-001&sort=prec&page=1&city=A01-001-00009&cat=TAG_4_4&glang=&fprice=*&eprice=*&availStartDate=&availEndDate="
# 建立一個 Request 物件，附加 Request Headers 的資訊
# 必須要讓自己看起來像一個正常的使用者在發送要求
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36"
})

with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #根據觀察，取得的資料是 JSON 格式

# 解析 JSON 格式的資料，取得每篇文章的標題
import json
data=json.loads(data) # 把原始的資料解析成字典/列表的表示形式
# 取得 JSON 資料中的文章標題
posts=data["data"]["product_list"]
for key in posts:
    print(key["name"])
