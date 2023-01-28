# def myFactory(base):
#     def myDeco(cb):
#         def run():
#             print("裝飾器內的程式",base)
#             result=base*2
#             cb(result)
#         return run
#     return myDeco

# @myFactory(5)
# def test(result):
#     print("普通函式的程式",result)

# test()

# 計算1+2+3+...+max 的裝飾器工廠
def calculateFactory(max):
    def calculate(callback):
        def run():
            #裝飾器想要執行的程式碼
            result=0
            for n in range(max+1):
                result+=n
                #把計算結果透過參數傳到被裝式的普通函式中
            callback(result)
        return run
    return calculate
    # 使用裝飾器
@calculateFactory(100)
def show(n):
    print("計算結果",n)
@calculateFactory(10)
def showenglish(n):
    print("Result is",n)

show()
showenglish()