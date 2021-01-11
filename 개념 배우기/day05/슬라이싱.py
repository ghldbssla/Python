#슬라이싱.py

arList=[1,2,3,4,5]
#[1,2]
print(arList[0:2])
print(arList[:2])

#[3,4,5]
print(arList[2:])

#음수인덱싱
print(arList[-1])

#################
print(arList[1:-1])

msg="Hello World"
print(msg[0:5])



#Life is too short, you need Python
#"too python"

msg="Life is too short, you need Python"
print(msg[8:12]+msg[-6:])
print(msg[msg.find("too"):12]+msg[msg.find('P'):])

word=input("슬라이싱 해 올 단어 : ")
idx = msg.find(word)
print(msg[idx:idx+len(word)])
