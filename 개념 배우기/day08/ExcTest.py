#ExcTest.py
try:
    int("S")
except ValueError as ve:
    print("이런거는 int로 바꿀 수 없어요!!")
    print(ve)
