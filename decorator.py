def myDec(cb):
    def infunc():
        result = 0
        for i in range(51):
            result += i
        cb(result)
    return infunc()

@myDec
def test(n):
    print('1加到50：', n) 

@myDec
def showEnglish(n):
    print('The result is :', n)

test
showEnglish