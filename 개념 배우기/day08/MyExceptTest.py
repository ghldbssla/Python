class MyError(Exception):
    pass

print("안녕! 예외발생 전!")
choice=input("예외 발생 (y,n)")
if(choice=='y'):
    raise MyError
else:
    print("무사히 지나감!")
