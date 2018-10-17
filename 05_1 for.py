rabbits = ['Flopsy', 'Mopsy', 'Conttontail', 'Peter'] # 자료구조확인?순회?
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

print("*"*30)
for rabbit in rabbits: # 파이썬은 편리하게 가능
    print(rabbit)

word = 'cat' #문자열 순회해보기
for letter in word:
    print(letter)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col.Mustard'}
for card in accusation: # card를 키로
    print(card)

for value in accusation.values(): # 값을 순회하려면 values() 함수사용
    print(value)

for item in accusation.items(): # 키와 값을 모두 반환하기 위해서는 items() 함수사용
    print(item)

for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents) # accusation의 첫번째내용(키)는 card에 두번째내용(값)은 contents에 할당된다

days = ['Monday', 'Tuesday','Wednesday'] #
fruits = ['banana', 'orange', 'peach'] #
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie','pudding']
for day, fruit , drink,dessert in zip(days, fruits, drinks, desserts): # 시퀀스를 병렬로 순회하게하기
    print(day, ": drink", drink,"- eat", fruit, "- enjoy", dessert)

# 앞에 숫자부터 ~ 뒤에숫자까지 나오는데 뒤에숫자에서 -1 한 값이나옴
for x in range(0,3): # 0,1,2의, 숫자 시퀀스
    print(x)
print(list(range(0,3))) # 리스트로 보기

for x in range(2,-1): # 2에서 그이상을 찾아서 출력되지않음
    print(x)
for x in range(2,-1,-1): # 2에서부터 0까지의 숫자 시퀀스 뒤에 -1을 붙여서 역순이라는걸 적어줘야함.
    print(x)
print(list(range(2,-1,-1))) #리스트로 보기

print(list(range(0,11,2))) # 0에서 11까지 숫자중 2칸씩 나오게하기 3번째 매개변수는 스텝오버하는 옵션





