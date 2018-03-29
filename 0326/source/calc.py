def add_func(*args):
    try:
        a = list(map(int,input("相加,以逗號分開").split(',')))
        b=0
        for i in a:
            b += i
        print(b)
    except:
        print('錯誤，請輸入數字')
    
def sub_func(*args):
    try:
        a = list(map(int,input("加減,以逗號分開").split(',')))
        b=a[0]
        for i in a[1:]:
            b -= i
        print(b)
    except:
        print('錯誤，請輸入數字')
        
def mult_func(*args):
    try:
        a = list(map(int,input("加乘,以逗號分開").split(',')))
        b=1
        for i in a:
            b *= i
        print(b)
    except:
        print('錯誤，智障')
        
def div_func(*args):
    try:
        a = list(map(int,input("加除,以逗號分開").split(',')))
        b=a[0]
        for i in a[1:]:
            b /= i
        print(b)
    except:
        print('錯誤，請輸入數字')
    