#School.py

class Student:
    def __init__(self,stuname,stuclass,stunum):
        self.stuname=stuname
        self.stuclass=stuclass
        self.stunum=stunum
        self.stuscore=list()
#학생 객체들이 담길 리스트
stuList=list()
while True:
        print("1. 점수 기입하기\n2. 점수 조회하기 \n3. 나가기")
        choice = int(input())
        if choice==1:
            #점수 기입하기
            stuname = input("이름 : ")
            stuclass = input("반 : ")
            stunum = input("번호 : ")
            #입력받은 값들로 Student 객체 하나 생성하기
            newstudent= Student(stuname,stuclass,stunum)
            #전체 학생 목록에 그 객체 추가
            stuList.append(newstudent)
            kor = int(input("국어 점수 : "))
            eng = int(input("영어 점수 : "))
            mat = int(input("수학 점수 : "))

            #위에서 입력받은 세개의 점수들은 방금 만들어낸 학생객체의
            #정보들이므로 학생객체 내부의 stuscore리스트에 append해준다.
            newstudent.stuscore.append(kor)
            newstudent.stuscore.append(eng)
            newstudent.stuscore.append(mat)
            print(newstudent.stuname+" 학생 점수 기입 완료!")

        elif choice==2:
            #점수 조회하기
            stuclass = input("반 : ")
            stunum = input("번호 : ")
            for i in (stuList):
                if(i.stuclass==stuclass and i.stunum==stunum):
                    print(i.stuname+"학생 점수표 \n-국어점수 : "+str(i.stuscore[0])+"\n-영어점수 : "+str(i.stuscore[1])+"\n-수학점수 : "+str(i.stuscore[2]))
                else:
                     print("일치하는 학생이 없습니다.")
        elif choice==3:
            #나가기
            print("안녕히 가세요")
            break
        else:
            print("잘못 입력하셧습니다.")
