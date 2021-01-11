#BookManager.py
class Book:
    def __init__(self,name,author,isbn):
        self.name=name
        self.author=author
        self.isbn=isbn
        
#1. 도서등록
    #도서명 : 
    #저자 :
    #ISBN(도서번호) : 0001~9999
    
#2. 도서수정

#3. 도서삭제
    #목록 보여주고
    #삭제할 도서번호 입력받기
    #일치하는거 목록에서 삭제

#4. 도서목록
    #도서명    -    저자(ISBN)

#5. 나가기
library = []
while True:
    print("1. 도서등록\n2. 도서수정\n3. 도서삭제\n4. 도서목록\n5. 나가기")
    choice=int(input())
    if(choice==1):
        #도서등록
        name = input("도서명 : ")
        author = input("저자 : ")
        isbn = input("ISBN : ")
        book = Book(name,author,isbn)
        library.append(book)
        print(name,"도서가 등록되었습니다.")
        
    elif choice==2:
        #도서수정
        #None : 모든 타입의 초기값(보통 주소값의 초기값으로 사용)
        updateBook=None
        for book in library:
            print(book.name+"\t-\t"+book.author+"("+book.isbn+")")
        isbn = input("삭제하실 도서의 ISBN을 입력하세요 : ")
        
        for i in range(len(library)):
            if(library[i].isbn==isbn):
                #수정할 책 찾은상태
                updateBook=library[i]
                
        print("수정하실 정보를 선택하세요")
        print("1. 도서명\n2. 저자")
        choice = int(input())
        newData=input("새로운 정보 : ")
        if choice==1:
            #도서명 수정
            updateBook.name=newData
        elif choice==2:
            #저자 수정
            updateBook.author=newData
        else:
            print("잘못 입력하셨습니다.")
    elif choice==3:
        #도서삭제
        for book in library:
            print(book.name+"\t-\t"+book.author+"("+book.isbn+")")
        isbn = input("삭제하실 도서의 ISBN을 입력하세요 : ")
        for i in range(len(library)):
            if(library[i].isbn==isbn):
                del library[i]
                break
        
    elif choice==4:
        #도서목록
        for book in library:
            print(book.name+"\t-\t"+book.author+"("+book.isbn+")")
    elif choice==5:
        print("안녕히가세요")
        break
    else:
        print("잘못 입력하셨습니다.")












    
