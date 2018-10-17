marx_list = ['Groucho','Chico', 'Harpo']
marx_tuple = 'Groucho','Chico','Harpo'
marx_dict = {'Groucho': 'Banjo', 'Chico': 'piano','Harpo':'harp'}
print(marx_list[2]) # list의 2번째 요소에 접근
print(marx_tuple[2]) # tuple의 2번째 요소에 접근
print(marx_dict['Harpo']) # 딕셔너리의 'Harpo'에 키로 접근 값얻기

marxes = ['Groucho', 'Chico', 'Harpo'] # 리스트3개생성 3개생성
pythons = ['Chapman','Cleese', 'Gilliam', 'Jones', 'Palin']
stooges = ['Moe','Curly', 'Larry']

tuple_of_lists = marxes, pythons , stooges  # 튜플의 각요소는 list다.
print(tuple_of_lists)

list_of_lists = [marxes,pythons,stooges] # 3가지 list를 한 list에 포함시키기
print(list_of_lists)

dict_of_lists = {'Marxes': marxes,'Pythons': pythons, 'Stooges': stooges} # list의 딕셔너리를 만들어보기
print(dict_of_lists)



