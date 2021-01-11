#Controller.py
adminid="admin"
adminpw="admin"
#내가 주문한 메뉴의 이름들을 담을 리스트
basket=list()
#전체 메뉴들을 담을 딕셔너리
menu=dict() #그냥{}이렇게 만들면 딕셔너리로 만들어짐
#내가 현재 갖고있는 잔액
balance=0

def login(id,pw):
    #넘겨받은 id와 pw를 전역변수로 선언되어 있는
    #adminid, adminpw와 비교해본다.
    #둘 다 같은 경우에 성공
    if(id==adminid):
        if(pw==adminpw):
            #관리자 로그인 성공이기 때문에 사용하는 곳으로
            #True값을 리턴해준다.
            return True
        #그 외에는 전부 False를 리턴해준다.
    return False

def insert(name,price):
    #메뉴 추가가 가능한지 여부를 알아볼 flag 변수
    flag=True
    #딕셔너리에서 빠른 for문을 사용하게 되면 key값들을 가져온다.
    #따라서 menu라는 딕셔너리는 "메뉴이름" : 가격 으로 이루어질
    #메뉴 딕셔너리 이므로 메뉴 이름을 하나씩 가져오게 된다.
    for menuName in menu:
        #내가 추가하려고 입력한 메뉴이름과 기존에 존재하는 메뉴의 이름이
        #같은것이 있는지를 확인한다.
        if menuName==name:
            #같은게 있다는 뜻이므로 추가 불가능, flag를 False로 바꿔준다.
            flag=False
            #이미 같은게 있다고 찾았으므로 더이상의 검색이 무의미하다. break 해준다.
            break
    #if문에 한번도 걸리지 않아서 flag가 그대로 True값이라면 추가 가능하다는 뜻이다.
    if(flag):
        #메뉴 추가
        menu[name]=price
        print("성공적으로 메뉴%s가 추가되었습니다.\n가격 : %d원"%(name,price))
    #flag가 False라면 else문으로 들어오게 된다.(추가 불가능)
    else:
        print("중복된 메뉴이름이 있습니다.")

def update(name,price):
    #수정이 가능한지를 확인할 flag
    flag=False
    for menuName in menu:
        if menuName==name:
            #찾는 메뉴가 있으므로 수정 가능하다는 뜻이다.
            flag=True
            #이미 찾았으므로 더 검색할 필요가 없으니 break
            break
    if(flag):
        #메뉴 수정
        menu[name]=price
        print("성공적으로 메뉴%s가 수정되었습니다.\n가격 : %d원"%(name,price))
    else:
        print("찾는 메뉴가 없습니다.")

def delete(name):
    flag=False
    for menuName in menu:
        if menuName==name:
            flag=True
            break
        if(flag):
            #메뉴 삭제
            del menu[name]
            print("성공적으로 메뉴%s가 삭제되었습니다."%name)
        else:
            print("찾는 메뉴가 없습니다.")

def selectAll():
    for name in menu:
        print("%s\t:\t%d원"%(name,menu[name]))

def getTotal(basket):
    total=0
    #장바구니에 담겨져 있는 이름 하나씩 가져와서
    for name in basket:
        #딕셔너리의 키값으로 사용하면 그 메뉴의 가격이 나온다.
        #그 나온 가격들을 total이라는 변수에 누적
        total+=menu[name]
    #누적된 total 리턴
    return total

def order(name):
    #넘겨받은 이름이 메뉴판 안에 있는지 확인하기 위한 flag
    flag=False
    #메뉴 딕셔너리 안에서 키값(메뉴이름)들을 하나씩 가져온 후
    for menuName in menu:
        #같은게 한번이라도 있다면 주문을 할 수 있다는 뜻이다.
        if name==menuName:
            flag=True
            break
        #찾는게 있다면 주문 성공
    if flag:
        #장바구니 리스트에 그 주문할 메뉴 이름을 추가해준다.
        basket.append(name)
        #장바구니 리스트를 getTotal()에 넘겨주면 그리스트에 담긴
        #메뉴들의 총 가격 합을 구해준다.
        total=getTotal(basket)
        print("현재 결제하실 금액 : %d원"%total)
    else:
        #찾는게 없는 경우
        print("메뉴 이름을 확인해 주세요.")

def pay():
    global basket
    #결제시 balance에서 결제하는 금액만큼을 빼서 넣어줘야 하므로
    #수정 가능하게 만들어 준다.
    global balance
    #getTotal()을 이용하여 현재 총 결제해야할 금액을 받아온다.
    total=getTotal(basket)
    if balance>=total:
        balance-=total
        print(total,"원 결제완료")
        #리스트명.clear() : 리스트 비우기
        basket.clear()
    else:
        print(total-balance,"원 부족, 결제 실패")

def deposit(money):
    #잔액을 충전하기 위해서는 전역변수 balance의 수정이 필요하다.
    #따라서 global 키워드를 이용해 전역변수 수정을 가능하게 해준다.
    global balance
    if money<=0:
        print("금액을 확인해 주세요.")
    else:
        balance+=money
        print("%d원 충전 완료\n현재 잔액 : %d원"%(money,balance))

def getList():
    if len(basket)==0:
        print("담긴 상품이 없습니다.")
    else:
        for name in basket:
            print("%s\t-\t%d원"%(name,menu[name]))



    
