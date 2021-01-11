#ClassTest.py

'''
#자동차라면 다 갖고있는 Brand,color,Price가 있고, 
#engineStart,engineStop이라는 기능이 있다.
#따라서 클래스에 담아두어 설정하면 된다.
myCarBrand = "Ferrarri"
myCarColor = "Red"
myCarPrice = 60000

def myCarEngineStart():
    print(myCarBrand+" 시동켜기")

def myCarEngineStop():
    print(myCarBrand+" 시동끄기")

momCarBrand = "Benz"
momCarColor = "Black"
momCarPrice = 35000

def momCarEngineStart():
    print(momCarBrand+" 시동켜기")

def momCarEngineStop():
    print(momCarBrand+" 시동끄기")

myCarEngineStart()
momCarEngineStart()
'''
class Car:
    brand=""
    color=""
    price=0
    
    #self는 객체를 뜻함 ex)mycar,momcar,...
    #메소드 매개변수 뒤에 = 값을 쓸 경우
    #매개값으로 적당한 값이 넘어오지 않았다면 그 값을
    #초기값으로 이용하여 내부 코드를 실행한다.
    def __init__(self,brand="",color="",price=0):
       self.brand=brand
       self.color=color
       self.price=price
       self.engine=False
       self.pw="abcd"
       self.cnt=0
    def engineStart(self,pw):
        if self.pw==pw:
            print("비밀번호 일치")
            if self.engine==False:
                print(self.brand+" 시동 켜기")
                self.engine=True
            else :
                print("이미 시동이 켜져있습니다.")
            self.cnt=0
        else:
            self.cnt+=1
            print("비밀번호가 틀리셨습니다. 틀린횟수:",self.cnt)
        if(self.cnt==3):
            print("====삐용삐용====")
            self.cnt=0
    def engineStop(self,pw):
        if self.pw==pw:
            print("비밀번호 일치")
            if  self.engine==True:
                print(self.brand+" 시동 끄기")
                self.engine=False
            else:
                print("이미 시동이 꺼져습니다.")
        else:
            self.cnt+=1
            print("비밀번호가 틀리셨습니다. 틀린횟수:",self.cnt)
        if(self.cnt==3):
            print("====삐용삐용====")
            self.cnt=0
    #Car클래스 안에 차의 정보를 출력해주는 show()메소드 만들기
    def show(self):
        print("브랜드 : "+self.brand)
        print("색깔 : "+self.color)
        print("가격 : ",self.price,sep="")
'''
#객체화 작업
mycar=Car("Ferrari","Red",60000)

    #기본생성자, 생성자는 사용한 부분이 만들어진 필드의 주소값이다.
#mycar = Car()
momcar = Car()
#객체 사용
#mycar.brand="Ferrari"
#mycar.color="Red"
#mycar.price=60000

momcar.brand="Benz"
momcar.color="Black"
momcar.price=35000

print(momcar.brand)
mycar.engineStart()
momcar.engineStart()

#아빠 차 정보를 입력받고 한대 만들기
brand=input("아빠 차 브랜드 : ")
color=input("아빠 차 색깔 : ")
price=int(input("아빠 차 가격 : "))
dadcar=Car(brand,color,price)

dadcar.show()
'''
#내 차 정보들 입력받고 한대 만들기
brand=input("내차 브랜드 : ")
color=input("내차 색깔 : ")
price=int(input("내차 가격 : "))
mycar=Car(brand,color,price)
#engineStart()
    #첫 시도 : brand+"시동켜기"
    #두번 이상 : 이미 시동이 켜져있습니다.
#engineStop()
    #첫 시도 : brand+"시동끄기"
    #두번 이상 : 이미 시동이 꺼져있습니다.

mycar.engineStart("1234")
mycar.engineStart("abcd")
mycar.engineStart("abcd")
mycar.engineStart("acbd")
mycar.engineStop("ㅁㅍㅍㅍ")
mycar.engineStop("ㅁㅍㅍㅍ")
mycar.engineStop("ㅁㅍㅍㅍ")
mycar.engineStop("1234")





