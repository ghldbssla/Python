#InhTest.py
class Car:
    def __init__(self,brand="",color="",price=0):
        self.brand=brand
        self.color=color
        self.price=price

    def engineStart(self):
        print(self.brand+" 열쇠로 시동켜기")
        
    def engineStop(self):
        print(self.brand+" 열쇠로 시동끄기")

#Car 클래스를 상속 받는 SuperCar클스
class SuperCar(Car):
    #def __init__():
        #자동으로 부모 생성자가 먼저 나옴
    def __init__(self,brand="",color="",price=0,mode=""):
        #self.brand=brand
        #self.color=color
        #self.price=price
        #부모 클래스의 생성자를 재정의 하면서 부모클래스의 필드를
        #Car.__init__(매개변수)로 가져온다.

        #다중 상속시에는 부모가 뭔지몰라서 명시적으로 적어놔야함
        #Car.__init__(self,brand,color,price)
        #상속받은 부모 클래스가 하나일 경우 super로 대체함 -->self안씀
        super().__init__(brand,color,price)
        self.mode=mode
    
    def engineStart(self):
        print(self.brand+" 음성으로 시동켜기")

    def engineStop(self):
        print(self.brand+" 음성으로 시동끄기")
        
    def roofOpen(self):
        print(self.brand+" 뚜껑열기")

    def roofClose(self):
        print(self.brand+" 뚜껑닫기")        
ferrari = SuperCar("ferrari","Red",60000,"스포티모드")
ferrari.engineStart()    
ferrari.roofOpen()

K5=Car("K5","white",70000)
K5.engineStart()
#roofOpen()은 자식 클래스에 생성되어 있는 필드 이므로 사용 불가
#K5.roofOpen()
