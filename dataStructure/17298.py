import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = list(map(int,input().split(' ')))
    stack = []
    res = [-1 for _ in range(N)]
    
    for i in range(N):
        while stack:
            if lis[i]>lis[stack[-1]]:
                res[stack.pop()]=lis[i]
            else:
                break
        stack.append(i)
        
    print(*res)

if __name__ == '__main__':
    main()