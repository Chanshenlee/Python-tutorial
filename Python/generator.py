# # 定義生成器函式
# def test():
#     print("階段一")
#     yield 3
#     print("階段二")
#     yield 10
    

# # 呼叫並回傳生成器
# gen=test()
# # print(gen) # 它是產生一個生成器，不是3喔
# # 搭配 for 迴圈中使用
# for d in gen: # 如果要產生資料，可以搭配for迴圈使用
#     print(d) #3

def generateEven(maxnumber):
    number=0
    while number<=maxnumber:
        yield number
        number+=2

evenGenerator=generateEven(10)
for data in evenGenerator:
    print(data)
