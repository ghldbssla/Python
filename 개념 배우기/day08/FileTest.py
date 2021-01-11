#FileTest.py

#file=open('파일경로','읽어올 모드')
#file.write("쓸 문자열")
#file.write()는 기존에 적혀있던 내용을 모두 지우면서 쓴다.
#따라서 수정시에는 기존 내용을 읽어오고 수정한 후 다시 덫어씌우는 식으로
#수정을 해야 한다.
#file.write() 후에는 file.close()로 파일에 적용시켜야 실제로 파일에 써진다.


#수정시
#먼저 모든 내용을 읽어와서 fileTxt에 넣어준다.
#fileTxt는 리스트 이므로 그안에 있는 문자열들을 다 꺼내오면서
#result에 연결해준다.
file=open('test.txt','r')
fileTxt=file.readlines()
result=""
for txt in fileTxt:
    result+=txt+"\n"

#추가할 내용을 연결하는 식으로 fileTxt에 연결해준다.
result+='Test\n'

#쓰기 모드로 연 후
file=open('test.txt','w')
#모든 내용에 추가할 내용까지 연결 된 fileTxt를 써주는 식으로
#기존 파일에 텍스트 추가를 해준다.
file.write(result)
file.close()
