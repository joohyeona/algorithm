'''
서울에서 김서방 찾기: https://school.programmers.co.kr/learn/courses/30/lessons/12919
리스트 배열에서 특정 값 찾아서 인덱스 반환
'''

s = ['Jane', 'Kim']
# return 김서방은 1에 있다.

# for 문 사용
def solution(seoul):
    i=0
    for k in seoul:
        if k=='Kim':
            return f'김서방은 {i}에 있다'
        else:
            i +=1

print(solution(s))

# index 사용 가능
def solution2(seoul):
    return '김서방은 %d에 있다' %seoul.index('Kim')
print(solution2(s))