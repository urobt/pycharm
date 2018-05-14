#End_0514

class stack:
  def __init__(self):
    self.st=[]
    self.a=""
  def push(self,x):
    self.st.append(x)
  def pop(self):
    # 스택이 비어있을때는 에러메세지 출력
    if len(self.st) >= 1 :
       self.a = (self.st.pop(-1))
       print(" ".join(self.a))
    else :
       print("-1")
  def size(self):
    #스택에 들어있는 정수 개수
    print(len(self.st))

  def empty(self):
    # 스택이 비어있으면 1, 아니면 0
    if len(self.st) < 1:
      print("1")
    else:
      print("0")

n=0
stk1=stack()
limit=int(input("몇줄?"))
#명령을 몇줄 넣을거에요?

while limit != n :
  x1=str(input("명령어"))
  x1=x1.replace(" ", "")

  if x1 == "pop":
     stk1.pop()
  elif x1 == "size":
     print(str(len(stk1.st)))
  elif x1 =="empty":
     print(stk1.empty)
  elif x1 == "top":
     print(str(stk1.st[-1]))
  else:
     stk1.push(list(x1[-1]))

  # 명령 하나당 n을 하나씩 올립니다.
  n += 1

#limit과 입력한 명령어 수가 같아지면 종료합니다 종료합니다



'''
1.stack을 구현합니다.
2.class기반으로 구현
2-1.class를 모듈화합니다
3.push n ,pop , size , empty , top만이 입력값으로 들어옵니다
4.명령줄 입력값은 1-10000사이입니다.무조건.
'''




