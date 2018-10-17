empty_set = set() # 생성할때 set() 함수 혹은 중괄호 ({})안에 콤마로 구분된 하나 이상의 값을 넣으면 된다.
print(empty_set)

even_numbers = {0,2,4,6,8}
print(even_numbers)

odd_numbers = {1,3,5,7,9}
print(odd_numbers)

print(set('letters')) # e와 t가 2개씩 있어도 하나씩만 포함되어있다.

print(set(['Dasher','Dancer','Prancer', 'Mason-Dixon'])) #리스트를 set으로 만들기

print(set(('Ummagumma', 'Echoes', 'Atom Heart Mother'))) #튜플을 set으로 만들기

print(set( {'apple': 'red', 'orange':'orange','cherry' : 'red'})) #딕셔너리에 set() 을 이용하면 키만 사용한다.

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian' : {'vodka', 'kahlua'},
    'white russian' : {'cream', 'kahlua' , 'vodka'},
    'manhattan' : {'rye', 'vermouth' , 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
} # 딕셔너리 생성 / 키는 혼합음료의 이름 ,값은 음료에 필요한 제료들의 셋

for name, contents in drinks.items():
    if 'vodka' in contents: # 보드카가 포함된 음료는 무엇인가?
        print(name)
print('*************')

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
    'cream' in contents): # 베르무트나 크림이 없는거 찾기
        print(name)


print('*************')
for name, contents in drinks.items(): #오렌지 주스 or 버몬트가 들어있는 음료찾기
    if contents & {'vermouth', 'orange juice'}:
        print(name)

print('*************')

for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}: # 보드카는 포함하지만 크림이나 버몬트는 들어있지않은 음료찾기
        print(name)

print('*************')


bruss = drinks['black russian'] # 두 음료의 재료 set을 변수에 저장
wruss = drinks['white russian']

print(bruss & wruss) # 양쪽 set에 들어있는 같은 멤버(교집합)구하기


a = {1,2}
b = {2,3}
print(a & b) # 양쪽 set에 들어있는 같은 멤버(교집합)구하기 2
print(a.intersection(b))

print(a| b) # 각 set의 멤버 모두
print(a.union(b)) # 각 set의 멤버 모두2

print(bruss | wruss) # 각 set의 멤버 모두구하기


print(a-b)
print(a.difference(b)) # 차집합 첫번째 set에는 있찌만 두번째 set에는 없는 멤버
print(bruss - wruss)
print(wruss - bruss) # 반대로 하면 wruss에는 cream이라는 멤버가 하나 더 있기때문에


print(a^b)
print(a.symmetric_difference(b)) # 한쪽 set에는 들어있지만 양쪽 모두에 들어 있지 않은 멤버(차집합)구하기
print(bruss ^ wruss)


print(a<=b) # 부분집합인지 확인 (부분집합=첫번째 set이 두번째 set에 모두 속할때)
print(a.issubset(b))

print("*****************")
print(bruss<=wruss) # bruss(balck russian)에 cream을 추가하면 white russian이 된다. 그래서 wruss는 bruss의 슈퍼셋(상위집합)

print("*****************")
print(a<=a) # 모든 set은 자신의 서브set인가? 확인
a.issubset(a)

print("*****************")
print(a<b) # 첫번째 set이 두번째 set의 프로퍼 서브셋(진부분집합) 이 되려면 두번째 set에는 첫번째set의 모든멤버를 포함한 그이상의 멤버가 있어야한다.
print(a<a)
print(bruss<wruss) # bruss의 멤버 'vodka' , 'vermouth' 두가지 모두를 wruss는 포함하고있으며 그 이상 cream이라는 멤버를 하나더 가지고있다.

print("*****************")
print(a>=b) # 슈퍼set은 서브set의 반대다
print(a.issuperset(b))
print(wruss>=bruss)

print("*****************")
print(a>=a) # 모든 set은 자신의 슈퍼set이다
print(a.issuperset(a))

print("*****************")
print(a>b) # > 연산자로 첫번째 set이 두번째 set의 프로퍼 슈퍼set인지 확인
print(wruss > bruss)  # 첫번째 set이 두번째 set의 프로퍼 슈퍼set이 되려면 , 첫번째 set에는 두번쨰 set의 모든 멤버를 포함한 그 이상의 멤버가 잇어야한다.

print("*****************")
print(a>a) #모든 set은 자신의 프로퍼 슈퍼set이 될수 없다.








