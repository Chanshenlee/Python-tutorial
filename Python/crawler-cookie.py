# 抓取 PTT 八卦版的網頁原始碼 (HTML)
import urllib.request as req
def getData(url):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    # 必須要讓自己看起來像一個正常的使用者在發送要求
    request=req.Request(url,headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Mobile Safari/537.36"
    })# 用甚麼樣的系統甚麼樣的瀏覽器

    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    # 解析原始碼，取得每篇的文章標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") #讓 BeautifulSoup 協助我們解析 HTML 格式文件
    titles=root.find_all("div",class_="title") #尋找 class="title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除) 印出來
            print(title.a.string)
    # 抓取上一頁連結
    nextLink=root.find("a",string="‹ 上頁") # 找到內文是 ‹ 上頁的 a 標籤
    return nextLink["href"]
# 抓取一個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<10:
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1
