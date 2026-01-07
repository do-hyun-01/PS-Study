import sys
input = sys.stdin.readline

# 단어를 입력받고 대문자로 변환
word = input().strip().upper()

# 중복 없는 알파벳 리스트 생성
words_list = list(set(word)) # set을 사용해서 중복 제거 필수

cnt_list = []

# 각 알파벳이 원본 단어에 몇 개 있는지 세기
for x in words_list:
    cnt = word.count(x)
    cnt_list.append(cnt)  # 개수를 리스트에 저장

# 가장 많이 사용된 알파벳이 여러 개인지 확인
if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    # 가장 많이 사용된 알파벳의 인덱스(위치)를 찾아서 출력
    max_index = cnt_list.index(max(cnt_list))
    print(words_list[max_index])