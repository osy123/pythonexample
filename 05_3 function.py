def do_nothing(): # 매개변수가 없는 함수를 정의하고 호출
    pass
print(do_nothing())

do_nothing()

def make_a_sound(): #매개변수없는 함수 정의하고 호출
    print('quack')
make_a_sound()

def agree(): # 매개변수없는 True값을 반환하는 함수 정의
    return True
if agree(): # return 값이 True면 'Splendid!' 출력하고 아니면 'That was unexpected.' 를 출력하는 if문
    print('Splendid!')
else:
    print('That was unexpected.')

def reverse():
    return False # 소문자안됨.
if reverse():
    print('Sqlendid!')
else :
    print('That was unexpected.')

def echo(anything):
    return anything + ' ' + anything
print(echo('haha'))
print(echo('Rumplestiltskin')) # 리턴값을 참고하여 하나더 생성된모습

def commnetary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else :
        return "I've never heard of the color " + color + "."

commnet = commnetary('blue') # 함수호출
#blue 값을 함수내의 color 매개변수에 할당
# if,elif , else문 실행
# 문자열을 반환
print(commnet) # 맞는부분이 없기때문에 else문 실행

print(do_nothing())

def menu(wine , entree , dessert): # 함수정의
    return {'wine': wine, 'entree': entree , 'dessert':dessert} #return값 딕셔너리로
print(menu('charbonnay', 'chicken', 'cake')) #값을 순서대로 상응하는 매개변수에 복사함. 이것이 위치인자
print(menu('beef', 'bage', 'bordeaux')) # 각위치의 인자를 잘알아야함

print(menu(entree='beef',dessert='bagel', wine='bordeaux')) # 매개변수에 상응하는 이름을 인자에 지정하기 , 함수의 정의와 다른순서로도 가능

print(menu('frontenac',dessert='flan', entree='fish')) # 위치인자와 키워드인자를 섞어서 쓸수있음. ! 대신에 위치인자가 먼저와야함

def menu(wine,entree,dessert='pudding'): # dessert만 키워드인자 정의
    return {'wine': wine, 'entree': entree, 'dessert':dessert}
print(menu('chardonnay','chicken')) # 'chardonnay', 'chicken'가 wine,entree에 매개변수값지정이됨
print(menu('dunkelfelder', 'duck', 'doughnut')) # 원래있던 dessert='pudding'이 사라지고 doughnut가 재정의됨

def buggy(arg, result=[]):
    result.append(arg)
    print(result) # result에 arg를 추가했으나 비어있다.

print(buggy('a'))
print(buggy('b')) # None값이 계속나온다.

def works(arg):
    result = []
    result.append(arg)
    return result
print(works('a'))
print(works('b'))

def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
print(nonbuggy('a')) #매개변수에 다른값을 넣어서 수정하기
print(nonbuggy('b'))

# 133p , 기본매개변수값지정하기까지