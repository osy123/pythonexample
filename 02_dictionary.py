empty_dict = {} # 중괄호로 딕셔너리 생성
print(empty_dict) # 딕셔너리는 키와 값으로 생성한다

bierce = {
    "day": "A period of twenty-four hours, mostly misspent", # day , positive , misfortune = 키 , 오른쪽의 내용들은 값
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses"}
print(bierce)

lol = [ ['a','b'],['c','d'],['e','f']] # 리스트를 딕셔너리로 변환
print(dict(lol))

lot = [('a','b'),('c','d'),('e','f')] # 튜플로 된 리스트
print(dict(lot))

tol = ( ['a','b'],['c','d'],['e','f']) # 리스트로 된 튜플
print(dict(tol))

los = [ 'ab', 'cd', 'ef'] # 두 문자열로 된 리스트
print(dict(los))

tos = ( 'ab' , 'cd' , 'ef') # 두 문자열로 된 튜플
print(dict(tos))

pythons = {
    'Chapman':'Graham',
    'Cleese' : 'John',
    'Idle': 'Eric',
    'Jones' : 'Terry',
    'Palin' : ' Michael'}
print(pythons) # 성을 키로 이름을 값으로 하는 딕셔너리 생성

pythons['Gilliam'] = 'Gerry' # 'Gilliam' : 'Gerry' 추가
print(pythons)

pythons['Gilliam'] = 'Terry' # 'Gilliam' : 'Gerry' 였던걸 같은키를 이용하여 'Gilliam' : 'Terry'로 수정
print(pythons)

others = { 'Marx': 'Groucho','Howard':'Moe'} # others 딕셔너리 생성
print(others)

pythons.update(others) # pythons딕셔너리에 others딕셔너리를 병합
print(pythons)

first = {'a':1, 'b':2} # first 딕셔너리 생성
second = {'b':'platypus'} # second 딕셔너리 생성
first.update(second) # first딕셔너리에 second 딕셔너리 병합
print(first) # 두 딕셔너리에 같은 키값이 있으면 두번째 딕셔너리에 있는 값이 남는다.

del pythons['Marx'] ## 딕셔너리 항목 삭제
print(pythons)
del pythons['Howard']
print(pythons)

pythons.clear() # 딕셔너리 키와 값 모두삭제
print(pythons)
pythons = {} # 딕셔너리 키와 값 모두삭제 2
print(pythons)

pythons = {
    'Chapman':'Graham',
    'Cleese' : 'John',
    'Idle': 'Eric',
    'Jones' : 'Terry',
    'Palin' : ' Michael'}
print(pythons)
print('Chapman' in pythons) # 안에 Chapman 키가 존재하는지 확인
print('Gilliam' in pythons)

print(pythons['Cleese']) # 딕셔너리에 키로 상응하는 값을 확인한다.

print(pythons.get('Cleese')) # 딕셔너리,키,옵션값을 사용한다 키가 존재하면 그 값을 얻는다
print(pythons.get('Marx', 'Not a Python')) # Mark 키가 없으면 뒤에 있는 문자 출력

signals = {'green': 'go','yellow':'go faster', 'red': 'smile for the camera'}
print(signals.keys())  # 키값만 가져오기

print(list(signals.values())) # 값만 가져오기

print(list(signals.items())) # 모든 쌍의 키-값 가져오기

save_signals = signals
signals['blue'] = 'confuse everyone' # 딕셔너리에 키,값 추가
print(save_signals) # 리스트와 마찬가지로 딕셔너리를 할당한 후 변경 할때 딕셔너리를 참조하는 모든 이름에 변경된 딕셔너리를 반영한다.
                    #signals에 추가했는데 save_signals로 출력했는데 'blue'가 추가된것을 확인할수있음.

signals = {'green': 'go','yellow':'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy() # copy명령어로 복사
signals['blue'] = 'confuse everyone' # signals에만 blue추가.
print(signals)  # signals에는 blue가 추가되었음.
print(original_signals) # copy해둔 original_signals에는 blue가 추가되지 않았음.









