#1. making a list of items
items_list = {}

while True:
    try :
        item = input("").upper()
        if item not in items_list:
            items_list[item] = 1
        else:
            items_list[item] += 1

    except KeyError:
        pass
    except EOFError:
        break
"""
# 키 값만 모아서 k 변수안에 넣는다.
k = items_list.keys()
k = sorted(k) # 키 값을 알파벳 순으로 정렬한다.

print() # 공백을 출력한다.

s_k = {} # 새로운 빈 딕션너리를 만든다.


for value in k:
    s_k[value] = items_list[value]

 #s_k라는 새로운 딕셔너리안에 키와 값을 한줄씩 프린트!!
for key, value in s_k.items():
    print(value, key)
"""
print()
#items()는 딕셔너리의 모든 키-값(key-value) 쌍을 한 번에
# 가져오는 딕셔너리 메서드입니다.
# sorted() 함수는 이 키-값 쌍들을 정렬하는 데 사용
for key, value in sorted(items_list.items()):
    print(value, key)


