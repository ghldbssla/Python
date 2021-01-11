#밥먹기 : feedCnt-=1, hp+=1
#잠자기 : 3초마다 hp 1 증가
#산책하기 : hp -= 1, 문제풀기 성공시 먹이갯수 2개 증가
#                           실패시 hp-=1
import time
class Animal:
    #메소드의 매개변수에 초기값을 주는 경우에는
    #가장 마지막 매개변수부터 주어야 한다.
    #따라서 내가 초기값을 주고싶은 매개변수를 가장 뒤쪽으로 배치해준다.
    def __init__(self,age,gender,hp,feed,name=''):
        self.name=name
        self.age=age
        self.gender=gender
        self.hp=hp
        self.feed=feed
        self.feedCnt = 0

    def eat(self):
        print(self.name + "이(가) "+self.feed+"을(를) 먹는 중...")
        if self.feedCnt!=0:
            self.feedCnt-=1
            self.hp+=1
            print("아유 맛있어!")
        else:
            print("먹이가 부족해요! 산책을 가보세요!")

    def sleep(self):
        count = 0
        while True:
            print("자는 중.",end='')
            for i in range(2):
                #1초 잠시 멈추기
                time.sleep(1)
                print(".",end='')
            time.sleep(1)
            count+=1
            self.hp+=1
            choice = input("계속 잘까요?(Y/N)")
            if choice.lower()=='n':
                break
        print("\nHP %d 회복 완료. 현재 체력 : %d"%(count,self.hp))
    def walk(self):
        if self.hp>1:
            self.hp-=1
            print("다음 중 파이썬을 가르치는 강사의 이름은?")
            print("1. 김다솔\n2. 이다솔\n3. 정다솔\n4. 최다솔\n5. 박다솔")
            choice = int(input())
            if choice==3:
                print("정답입니다")
                self.feedCnt+=2
            else:
                print("오답 ㅠㅠ")
                self.hp-=1
                if self.hp == 0:
                    print(self.name+" 안녕~")
        else:
            print("체력이 부족해요! 체력을 채우고 오세요!")

    def show(self):
        print("이름 : "+self.name)
        print("나이 :",self.age)
        print("성별 : "+self.gender)
        print("체력 :",self.hp)
        print(self.feed+"갯수 :",self.feedCnt)



##########################################MAIN#########################################
pig=Animal(4,'수컷',5,'감자')
dog=Animal(5,'암컷',7,'뼈다귀')
cat=Animal(3,'수컷',10,'생선')
arAnimal=[pig,dog,cat]

while True:
    choice = int(input("1. 돼지\n2. 강아지\n3. 고양이\n4. 나가기\n"))
    if choice==4:
        break
    #초이스가 1~3중에 하나인지 검사하는것이 필요하다
    choiceAnimal=arAnimal[choice-1]

    name = input("캐릭터 이름 : ")
    choiceAnimal.name=name
    while True:
        if choiceAnimal.hp==0:
            print("다시 생성할 캐릭터 정보를 입력하세요")
            age=input("나이 : ")
            gender = input("성별 : ")
            hp = int(input("체력 : "))
            feed = input("먹이 : ")
            arAnimal[choice-1]=Animal(age,gender,hp,feed)
            break
        menu = int(input("1. 밥먹기\n2. 잠자기\n3. 산책하기\n4. 내정보\n5. 메인메뉴로 이동\n"))
        
        if menu==1:
            #밥먹기
            choiceAnimal.eat()
        elif menu==2:
            #잠자기
            choiceAnimal.sleep()
        elif menu==3:
            choiceAnimal.walk()
        elif menu==4:
            choiceAnimal.show()
        elif menu==5:
            break
        











