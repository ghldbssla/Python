#ClassTest.py
'''
myCarBrand = "Ferrari"
myCarColor = "Red"
myCarPrice = 60000
def myCarEngineStart():
    print("Ferrari 시동켜기")
def myCarEngineStop():
    print("Ferrari 시동끄기")

myCarEngineStart()

myCarBrand = "K7"
myCarColor = "white"
'''

class Car:
    brand=""
    color=""
    price=0

    #생성자
    def __init__(self,brand,color,price):
        self.brand=brand
        self.color=color
        self.price=price
    
    def EngineStart(self):
        print(self.brand+"시동켜기")
    def EngineStop(self):
        print(self.brand+"시동끄기")

#.(하위연산자) : A.b : A안의b, A의b
'''
#mycar.EngineStart() - self가없어 실행이 안됨
mycar=Car()#생성자

#print(mycar)
mycar.brand="Ferrari"
mycar.color="red"
mycar.price=60000
mycar.EngineStart()
'''

mycar=Car("Ferrari","red",60000)
mycar.EngineStart()
momcar=Car("K7","white",20000)
momcar.EngineStart()



    
