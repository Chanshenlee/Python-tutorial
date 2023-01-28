# def test(arg):
#     arg() # 呼叫回呼函式 handle()

# #定義一個回呼函式
# def handle():
#     print(100)

# test(handle)

# def test2(abc):
#     abc(50) # 回呼函式的參數

# #定義一個回呼函式
# def handle2(data):
#     print(data)

# test2(handle2)


# def add(n1,n2,cb):
#     cb(n1+n2)

# def handle(result):
#     print("result",result)
# def handle2(result):
#     print("Result of Add is",result)

# add(3,4,handle)
# add(5,6,handle2)



print("----------------------------------")
def add(n1,n2,cb):
    cb(n1+n2)

def handle(result):
    print("result",result)

add(3,6,handle)
