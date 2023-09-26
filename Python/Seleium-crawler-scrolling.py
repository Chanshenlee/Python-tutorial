from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search?trk=guest_homepage-basic_guest_nav_menu_jobs&position=1&pageNum=0")
driver.maximize_window()

n=0
while n<3:
    #捲動視窗並等待瀏覽器載入更多內容
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 捲動視窗到底部
    time.sleep(3)
    n+=1
#取得網頁中的工作標題
tags = driver.find_elements(By.CLASS_NAME,"base-search-card__title")
for tag in tags:
    print(tag.text)
