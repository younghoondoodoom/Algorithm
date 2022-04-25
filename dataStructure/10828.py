import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    stack = []
    
    for _ in range(N):
        put = input().split(' ')
        
        if put[0] == 'push':
            stack.append(put[1])
        elif put[0] == 'pop':
            try:
                print(stack.pop())
            except IndexError:
                print(-1)
        elif put[0] == 'size':
            print(len(stack))
        elif put[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif put[0] == 'top':
            try:
                print(stack[-1])
            except IndexError:
                print(-1)

if __name__ == '__main__':
    main()