import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, K = map(int ,input().split(' '))
    deq = deque()
    for i in range(N):
        deq.append(i+1)
    print("<",end='')
    while len(deq) > 0:
        for i in range(K-1):
            deq.append(deq.popleft())
        if len(deq) == 1:
            print(deq.popleft(), end="")
        else:
            print(deq.popleft(), end=', ')
    print(">", end='')
    
            
if __name__ == '__main__':
    main()