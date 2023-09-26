from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))
driver.get("https://leetcode.com/accounts/login/")
driver.maximize_window()
# 輸入帳號密碼，按下登入按鈕
usernameInput = driver.find_element(By.ID, "id_login")
userpasswardInput = driver.find_element(By.ID, "id_password")
usernameInput.send_keys("")
userpasswardInput.send_keys("")
signinbtn = driver.find_element(By.ID,"signin_btn")
signinbtn.send_keys(Keys.ENTER)

# 等待登入完成
time.sleep(10)
#連線到登入後才能取得的資料畫面，取得資料
driver.get("https://leetcode.com/problemset/all/")
time.sleep(2)
startElement = driver.find_element(By.CSS_SELECTOR,"[data-difficulty=TOTAL]")
columns=startElement.text.split("\n")
print("已完成刷題數量",columns[1])
