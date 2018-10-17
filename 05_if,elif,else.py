disaster = True # disaster = True 이다 라고 선언
if disaster: # 만약 disaster 가 True면
    print("Woe!") # 이 문구 출력
else:
    print("Whee!") # 아니면 or 그밖에 이 문구 출력


furry = True
small = True
if furry: # furry 확인
    if small:  # furry는 True이기 때문에 small출력
        print("It's a cat.")
    else :
        print("It's a bear!")
else :
    if small:
        print("It's a skink!")
    else :
        print("It's a human. Or a hairless bear.")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple":
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color",color)

x = 7

print(x ==5) # x는 5와 같나?
print(x ==7) # x는 7과 같나?
print(5<x)  # 5보다 x가 더큰가?
print(x<10) # x보다 10이 더큰가?

print("*"*30)

print( 5 < x and x < 10) # 5<x는 true고 x<10또한 true 결국 true and true 이기 때문에 true

print(5<x)and (x<10) # 괄호를 이용하여 우선순위 혼란피하기

print(5<x or x < 10)
print(5<x and x > 10)
print(5 <x and not x >10)

print(5<x<10) # 하나의 변수를 여러번 비교
print(5<x<10<999)

count = 1 # count 에 변수1할당
while count <= 5: # count(1)이 5와 같거나 5가 더커질때까지
    print(count)
    count += 1 # 1씩 증가하면서

while True:
    stuff = input("String to capitalize [type q to quit]:") # 콘솔창에 출력했을때 나오는부분
    if stuff == "q": # q를 누르면
        break # 종료된다
        print(stuff.capitalize()) # capitalize = 첫번째 문자를 대문자로 출력

while True:
    value = input("Integer, please [q to quit]:")
    if value == 'q': # q를 입력하면 종료된다
        break
    number = int(value)
    if number %2 ==0:
        continue
        print(number, "squared is " , number*number)




