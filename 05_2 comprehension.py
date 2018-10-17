number_list = [] # 리스트생성
number_list.append(1) #정수 추가하기
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
print(number_list)

number_list= [] # 리스트생성
for number in range(1,6): # number에 range1~5까지를 넣는다.
    number_list.append(number) # 넘버리스트에 추가한다 윗줄에서 number에 추가햇던 1~5
print(number_list)

number_list = list(range(1,6)) # list에 직접 range를 넣어서 결과보기
print(number_list)

number_list = [number for number in range(1,6)] # 리스트 컴프리헨션으로 정수리스트 만들기
print(number_list)

number_list = [number-1 for number in range(1,6)] # 구하려던값에서 -1 즉 0~4까지 구한다는뜻 number-1(옵션)
print(number_list)

a_list = [number for number in range(1,6) if number %2 ==1] # number 에서 2를 나눠서 1로 남는걸 구한다는뜻 즉 홀수를 구한다는것.
print(a_list)

a_list=[]
for number in range(1,6): # 파이썬에서 할수있는 방식
    if number % 2 == 1:
        a_list.append(number)
print(a_list)

rows = range(1,4) # 1 2 3출력
cols = range(1,3) # 1 2 출력
for row in rows: # rows와 cols의 중첩되는것 확인
    for col in cols :
        print(row, col)

rows = range(1,4)
cols = range(1,3)
cells = [(row,col) for row in rows for col in cols] # 튜플리스트를 만들어서 cells변수에 할당하기
for cell in cells:
    print(cell)

for row, col in cells: # row와 col의 값만 출력하기위해 튜플 언패킹
    print(row,col)

word = 'letters' # word에 letters 저장
letter_counts = {letter: word.count(letter) for letter in word} # 문자열 letter의 일곱글자를 글자가 몇번나왔는지 그수를 샌다
print(letter_counts)

word = 'leeters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

a_set = {number for number in range(1,6) if number % 3 ==1} #1부터 5까지의 수 = 1,2,3,4,5 에서 3을 나누고 나머지가1인 숫자멤버출력 + 1은 몫이 0이라서 나옴.
print(a_set)

number_thing = (number for number in range(1,6)) # 오류 튜플은 컴프리헨션x , 제너레이터 컴프리헨션이라는것이며 제너레이터 객체를 반환
print(type(number_thing))

for number in number_thing: # 제너레이터 객체를 바로 순회하는방법 / 제너레이터는 이터레이터에 데이터를 제공하는 하나의방법
    print(number)

number_thing = (number for number in range(1,6)) # 제너레이터는 한번만 실행될수 잇다. 제너레이터는 즉석에서 그값을 생성한다 제너레이터는 이값을 기억하지 않으므로 다시시작,백업할수없다.
number_list = list(number_thing) # 그래서 위에 number_thing 이 있음에도 다시 생성해야 출력이 된다.
print(number_list)



