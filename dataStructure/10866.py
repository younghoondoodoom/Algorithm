import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    deq = deque()
    for _ in range(N):
        comm = input().split(' ')
        if comm[0] == 'push_front':
            deq.appendleft(comm[1])
        elif comm[0] == 'push_back':
            deq.append(comm[1])
        elif comm[0] == 'pop_front':
            try:
                print(deq.popleft())
            except IndexError:
                print(-1)
        elif comm[0] == 'pop_back':
            try:
                print(deq.pop())
            except IndexError:
                print(-1)
        elif comm[0] == 'size':
            print(len(deq))
        elif comm[0] == 'empty':
            if len(deq) == 0:
                print(1)
            else:
                print(0)
        elif comm[0] == 'front':
            try:
                print(deq[0])
            except IndexError:
                print(-1)
        elif comm[0] == 'back':
            try:
                print(deq[-1])
            except IndexError:
                print(-1)

if __name__ == '__main__':
    main()