#연결리스트.py
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None#모든 타입의 초기값

class LinkedList:
    def __init__(self):
        self.head=Node('head')
        self.count=0

    #추가
    def append(self,data):
        newNode = Node(data)
        curr=self.head
        for i in range(self.count):
            curr=curr.next
        curr.next=newNode
        self.count+=1
    #삽입
    def insert(self,idx,data):
        newNode = Node(data)
        curr=self.head
        for i in range(idx):
            curr=curr.next
        if curr.next is not None:
            #curr.next가 None이 아닌 상태(중간에 삽입)
            newNode.next=curr.next
            curr.next=newNode
        else:
            #curr.next가 None인 상태(가장 마지막에 삽입)
            curr.next=newNode
        self.count+=1
        
    #수정
    def update(self,idx,data):
        curr=self.head
        for i in range(idx+1):
            curr=curr.next
        curr.data=data
    #삭제
    def delete(self,idx):
        curr=self.head
        for i in range(idx):
            curr=curr.next
        curr.next=curr.next.next
        self.count-=1
    #조회
    def get(self,idx):
        curr=self.head
        for i in range(idx+1):
            curr=curr.next
        return curr.data
        
    #목록
    def show(self):
        curr=self.head
        for i in range(self.count):
            print(curr.data,end='->')
            curr=curr.next
        print(curr.data)


li = LinkedList()
li.append('A')
li.append('B')
li.append('C')
li.insert(1,'D')
li.show()
li.update(1,'E')
li.show()
li.delete(1)
li.show()
print(li.get(1))

li2 = LinkedList()
li2.append(10)
li2.show()










