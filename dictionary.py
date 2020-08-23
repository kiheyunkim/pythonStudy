# dictionary 선언
dictionary1 = {
    'name': 'kim',
    'phone': '000-0000-0000',
    'birth': '000000'
}
print(dictionary1)

dictionary2 = {1: 'name'}
print(dictionary2)
dictionary3 = {'a': [1, 2, 3]}
print(dictionary3)

# 값 추가
dictionary4 = {1: 'a'}
print(dictionary4)
dictionary4[2] = 'b'
print(dictionary4)

del dictionary4[2]
print(dictionary4)

print(dictionary1['name'])

#불가한 딕셔너리
# a = {[1, 2]: 'hi'}

#딕셔너리 함수들
#Key 리스트
print(dictionary1.keys())

for key in dictionary1.keys():
    print(key)

#value 리스트
print(dictionary1.values())

#key로 값 가져오기
print(dictionary1.get('name'))
#[]는 없을떄 에러가 나지만 get은 None을 돌려줌 = 좀더 안전한 처리

#Key가 딕셔너리에 있는지 판단
print('name' in dictionary1)

