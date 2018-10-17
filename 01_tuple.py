empty_tuple = ()
print(empty_tuple) # 튜플만들기

one_marx = 'Groucho', # 튜플에 요소저장하기 마지막에 ,필수
print(one_marx)

marx_tuple = 'Groucho', 'Chico', 'Harpo' # 2가지이상 요소가 있을경우 마지막에는 ,를 붙이지않는다.
print(marx_tuple)

marx_tuple = ('Groucho','Chico','Harpo') # 튜플을 출력할때 괄호()가 나오지만 튜플을 정의할때는 괄호가 필요없다. 뒤에콤마는 튜플을 정의한다는뜻.
print(marx_tuple)                        # 값들을 괄호로 묶어서 튜플을 정의하면 구분하기가 쉽다.

marx_tuple = ('Groucho','Chico','Harpo') # 튜플 생성
a,b,c=marx_tuple                         # 한번에 abc에 할당 = 튜플 언패킹
print(a)
print(b)
print(c)

password = 'swordfish' # 패스워드를 솔드피시로 정의
icecream = 'tuttifrutti' # 아이스크림을 투티프루티로 정의
password, icecream = icecream , password  # 값교환 , 임시변수를 사용하지않고 가능
print(password)
print(icecream)

marx_list = ['Groucho','Chico','Harpo'] # 리스트로 생성
print(tuple(marx_list)) # 튜플로 변경
