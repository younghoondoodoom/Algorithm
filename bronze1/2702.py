import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    for _ in range(N):
        lis = list(map(int, input().split(' ')))
        a = min(lis)
        b = max(lis)
        for i in range(b , a*b+1):
            if i % a == 0 and i % b == 0:
                print(i, end=' ')
                break
        for i in range(a+1, 0, -1):
            if a % i == 0 and b % i == 0:
                print(i)
                break
        

if __name__ == '__main__':
    main()