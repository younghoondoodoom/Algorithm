import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = [0, 1]
    for x in range(2, N+1):
        y = lis[x-2] + lis[x-1]
        lis.append(y)
    print(lis[N])
    
    
    
if __name__ == '__main__':
    main()