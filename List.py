# 리스트
odd = [1, 3, 5, 7, 9]
listA = []
listA2 = list()
listB = [1, 2, 3]
listC = ['Life', 'is', 'too', 'short']
listD = [1, 2, 'Life', 'is']
listE = [1, 2, ['Life', 'is']]

# 리스트 인덱싱
print(odd[0])
print(odd[-1])

# 리스트 내의 리스트
print(listE[2])

print(listE[2][1])
print(listE[2][-2])

# 리스트의 슬라이싱
print(listC[1:3])

# 리스트 연산
# 리스트 더하기
print(listC + listD)

# 리스트 반복
print(listC * 3)

# 길이 재기
print(len(listC))

# 요소삭제
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)
del array[1]
print(array)

# List Function
array2 = [1, 2, 3, 4]
print(array2)
array2.append(111)
print(array2)

# 정렬
unsortedArray = [1, 6, 3, 87, 2, 34, 2, 5, 8, 2]
print(unsortedArray)
unsortedArray.sort()
print(unsortedArray)

# 뒤집기
unsortedArray.reverse()
print(unsortedArray)

# 값을 찾아 인덱스 찾기
print(unsortedArray.index(3));
# print(unsortedArray.index(7)); // 없으면 에러남

# 리스트에 요소 삽임
unsortedArray.insert(0, 111111)
print(unsortedArray)

# 리스트 요소 제거
unsortedArray.remove(34)
print(unsortedArray)

# 리스트 마지막 요소 제거
unsortedArray.pop()
print(unsortedArray)

# 특정 값의 개수
print(unsortedArray.count(2))

# 리스트 확장
print(unsortedArray)
unsortedArray.extend([1, 2, 3, 4, 5, 6])
print(unsortedArray)