# 寫入 csv 格式檔案
import csv
with open("data.csv",mode="w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow([1,2,3])
    writer.writerow([4,5,6])
    writer.writerow([7,8,9])

# 讀取 csv 格式檔案
import csv
with open("data.csv",mode="r",newline="") as file:
    reader=csv.reader(file)
    # 逐列讀取資料
    total=0
    for row in reader:
        for number in row:
            total=total+int(number)
    print(total)