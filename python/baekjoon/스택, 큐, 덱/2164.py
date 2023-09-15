'''
카드2(https://www.acmicpc.net/problem/2164)
큐를 사용하여 동작을 구현하는 문제
input 6, output 4
'''

# n = int(input())
n = 6

def sol(N):
    cards = [i for i in range(1, N+1)]
    while len(cards) > 1 :
        cards.pop(0)
        cards.append(cards.pop(0))
    return cards[0]

print('시간초과:', sol(n))


# 시간초과 되지 않게 deque 사용
from collections import deque

def sol2(N):
    cards = deque([i for i in range(1, N+1)], maxlen=500000)

    while len(cards) > 1 :
        cards.popleft()
        cards.append(cards.popleft())
    
    return cards[0]
print('정답:',sol2(n))