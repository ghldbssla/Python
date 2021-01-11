#inhTest2

#동물(Animal)클래스
#변수 : 이름, 나이, 성별, 먹이
#기능 : 먹기, 자기, 움직이기

#동물 클래스의 자식클래스 3개 만들기
class Animal:
    def __init__(self,name="",age=0,gender="",food=""):
        self.name=name
        self.age=age
        self.gender=gender
        self.food=food
        
    def eat(self):
        print(self.name+"(이)가 "+self.food+"(을)를 먹는다.")
        
    def sleep(self):
        print(self.name+"(이)가 잔다.")
           
    def move(self):
        print(self.name+"(이)가 움직인다.")

class Fish(Animal):
    
    def move(self):
        print(self.name+"(이)가 물속에서만 움직인다.")

class Turtle(Animal):
    
    def move(self):
        print(self.name+"(이)가 육지랑 물속 둘다 움직일수 있다.")

class Bear(Animal):
    
    def move(self):
        print(self.name+"(이)가 육지에서만 움직인다.")

    def sleep(self):
        print(self.name+"(이)가 겨울잠을 잔다.")

fish=Fish("물고기",1,"수컷","박테리아")
turtle=Turtle("거북이",80,"암컷","젤리")
bear=Bear("곰",15,"수컷","꿀단지")
fish.eat()
fish.sleep()
fish.move()
turtle.eat()
turtle.sleep()
turtle.move()
bear.eat()
bear.sleep()
bear.move()
