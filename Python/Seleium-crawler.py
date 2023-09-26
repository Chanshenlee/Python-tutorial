from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
driver.maximize_window()

tags = driver.find_elements(By.CLASS_NAME,"title")
for tag in tags:
    print(tag.text)

# 模擬使用者點擊4次(我要五頁股票版的文章標題)
n=0
while n<5:
    # 取得上一頁的文章標題
    link=driver.find_element(By.LINK_TEXT,"‹ 上頁")
    link.click()
    tags = driver.find_elements(By.CLASS_NAME,"title")
    for tag in tags:
        print(tag.text)
    n+=1
driver.close()











