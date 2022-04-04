import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main() :
    N = int(input())
    deq = deque()
    for i in range(1, N+1):
        deq.append(str(i))
    
    while len(deq) > 1:
        print(deq.popleft(), end=' ')
        deq.append(deq.popleft())    
    
    print(deq[0])

if __name__ == '__main__':
    main()