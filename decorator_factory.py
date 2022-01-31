# 做一個裝飾器工廠可以處理1+2+3+4+....+(user set num)

def factor(end_num): # 裝飾器工廠
    def decor(cb): # 裝飾器
        def sum(): # 裝飾器內部函式
            result = 0
            for i in range(1, end_num + 1):
                result += i
                if i == end_num:
                    print(i, end='')
                else:
                    print(i, ' + ',sep='',end='')
            cb(result)
        return sum
    return decor

n = input('輸入最終數字：')
@factor(int(n))
def show(ans):
    print(' =', ans)

show()