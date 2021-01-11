#Stroage.py
data=10
def init():
    global data
    print(data)
    data=20
    #data=20  사용은 되지만 수정은 불가 -- global 추가
init()
print(data)
