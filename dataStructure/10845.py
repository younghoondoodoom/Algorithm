import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    queue = deque()
    for _ in range(N):
        command = input().split(' ')
        if command[0] == 'push':
            queue.append(command[1])
        elif command[0] == 'pop':
            try:
                print(queue.popleft())
            except IndexError:
                print(-1)
        elif command[0] == 'size':
            print(len(queue))
        elif command[0] == 'empty':
            if len(queue) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == 'front':
            try:
                print(queue[0])
            except IndexError:
                print(-1)
        elif command[0] == 'back':
            try:
                print(queue[-1])
            except IndexError:
                print(-1)

if __name__ == '__main__':
    main()