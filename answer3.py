# 3-1
names = ['liuda','wanger','zhangsan','lisi']
print(names[0])
print(names[1])
print(names[2])
print(names[3])
 
# 3-2
message = "hello,"
print(message+names[0])
print(message+names[1])
print(message+names[2])
print(message+names[3])
#below is my answer:
names=['wangchengyan','wangchenglin','wangping','yanfudan']
message="nice to meet you!"
print(f"{names[0].title()},{message}")
print(f"{names[1].title()},{message}")
print(f"{names[2].title()},{message}")
print(f"{names[3].title()},{message}")
 
# 3-3
ty = ['bicycle','car','motorcycle']
sth = "I would like to own a "
print(sth+ty[0])
print(sth+ty[1])
print(sth+ty[2])
#below is my answer:
trans=['mote','bicycle','bus','subway']
message="I would like to own a"
print(f"{message} {trans[0]}.")
print(f"{message} {trans[1]}.")
print(f"{message} {trans[2]}.")
print(f"{message} {trans[3]}.")
 
# 3-4
person = ['sunyanzi','wuenda','dafenqi','tuling']
print("welcome to my party "+person[0])
print("welcome to my party "+person[1])
print("welcome to my party "+person[2])
print("welcome to my party "+person[3])
#below is my answer
friends=['tom','mike','dan']
msg="welcome to my house for dinner!"
print(f"Hi {friends[0].title()},{msg}")
print(f"Hi {friends[1].title()},{msg}")
print(f"Hi {friends[2].title()},{msg}")
 
# 3-5
print(person[2]+" not go to my party");
person[2]="yaoqizhi"
print("welcome to my party "+person[0])
print("welcome to my party "+person[1])
print("welcome to my party "+person[2])
print("welcome to my party "+person[3])
#below is my answer
print(f"I am sorry to hear that {friends[2].title()} could not come.")
friends[2]='john'
print(f"Hi {friends[0].title()},{msg}")
print(f"Hi {friends[1].title()},{msg}")
print(f"Hi {friends[2].title()},{msg}")
 
# 3-6
print("I find a big dining-table")
person.insert(0,'wangfei')
person.insert(2,'jiaying')
person.append('dilireba')
print("welcome to my party "+person[0])
print("welcome to my party "+person[1])
print("welcome to my party "+person[2])
print("welcome to my party "+person[3])
print("welcome to my party "+person[4])
print("welcome to my party "+person[5])
print("welcome to my party "+person[6])
#below is my answer
print("I find a bigger desk")
friends.insert(0,'lucy')
friends.insert(2,'lily')
print(friends)
friends.append('jenny')
print(f"Hi {friends[0].title()},{msg}")
print(f"Hi {friends[1].title()},{msg}")
print(f"Hi {friends[2].title()},{msg}")
print(f"Hi {friends[3].title()},{msg}")
print(f"Hi {friends[4].title()},{msg}")
print(f"Hi {friends[5].title()},{msg}")
 
# 3-7
print("I am sorry,I just invite two people")
print("sorry I can't invite you,"+person.pop())
print("sorry I can't invite you,"+person.pop())
print("sorry I can't invite you,"+person.pop())
print("sorry I can't invite you,"+person.pop())
print("sorry I can't invite you,"+person.pop())
print("welcome to my party "+person[0])
print("welcome to my party "+person[1])
del person
#below is my answer
print("Finally I can only invite two friends to have dinner")
print(friends)
print(len(friends))
cancelone=friends.pop(0)
print(f"I am sorry {cancelone.title()}, I can't invite you.")
canceltwo=friends.pop()
print(f"I am sorry {canceltwo.title()}, I can't invite you.")
canceltwo=friends.pop()
print(f"I am sorry {canceltwo.title()}, I can't invite you.")
canceltwo=friends.pop()
print(f"I am sorry {canceltwo.title()}, I can't invite you.")
print(friends)
print(f"Hi {friends[0].title()}, you are still invited.")
print(f"Hi {friends[1].title()}, you are still invited.")
del friends[0]
del friends[0]
print(friends)
 
# 3-8
travel = ['xinjiang','maerdaifu','weinisi','xianggelila','sanya']
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel,reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)
#below is my answer:
places=['hangzhou','suzhou','yunnan','chongqing','qingdao']
print(places)
print(sorted(places))
print(places)
print(sorted(places,reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
 
# 3-9
person = ['sunyanzi','wuenda','dafenqi','tuling']
print(len(person))
 
# 3-10
like = ['sunyazi','xiaolongxia','xinjiang','yuedu']
print(like)
print(sorted(like))
like.sort(reverse=True)
print(like)
like.insert(2,'sanbu')
like.append('green')
del like[2]
print(like)
like.pop()
print(like)
#below is my answer
like=['huangshan','changjiang','China','shenzhen','hanyu','dota']
print(like)
print(sorted(like))
print(sorted(like,reverse=True))
print(like)
like.sort(reverse=True)
print(like)
like.insert(2,'sanbu')
print(like)
like.append('green')
print(like)
del like[2]
print(like)
like.remove('hanyu')
print(like)
like.pop()
print(like)
#print(like[8])
 
# 3-11
error = ['sd','s1']
print(error[2])