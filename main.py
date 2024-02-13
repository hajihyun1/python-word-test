
f=open("list.txt",'r')
list=f.readlines()

score=0
line_count=0
word=[]
meaning=[]

for line in list:
  line_count+=1

for i in range(0,line_count):
  tenporary=[]
  temporary=list[i].split(' ')
  word.append(temporary[0])
  meaning.append(temporary[1])


f.close()

for i in range(line_count):
  if i!=line_count-1:
    print(meaning[i],end="")
  else:
    print(meaning[i])
  answer=input()
  if answer==word[i]:
    score+=1
    

print("%d개중 %d개 정답"%(line_count,score))
