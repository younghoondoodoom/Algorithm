import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = list(map(int, input().split(' ')))
    lis.sort()
    
    if N % 2 == 0:
        print(lis[0] * lis[-1])
    else: 
        print(lis[N//2] **2)
    

if __name__ == '__main__':
    main()