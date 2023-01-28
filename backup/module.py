# 載入內建的 sys 模組並取得資訊
# import sys as system
# print(system.platform)
# print(system.maxsize)

# 建立 geometry 模組，載入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# result=geometry.slope(1,2,5,6)
# print(result)
# 調整搜尋模組的路徑
import sys
sys.path.append("modules")
# print(sys.path) # 印出模組的搜尋路徑
import geometry # 擴充套建檢查的問題
print(geometry.distance(1,1,5,5))

# 主程式 = 我們在執行時所跑的程式