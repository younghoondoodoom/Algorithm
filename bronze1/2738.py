import sys
import string

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, M = list(map(int, input().split(' ')))
    res = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(2):
        for i in range(N):
            lis = list(map(int, input().split(' ')))
            for j in range(M):
                res[i][j] += lis[j]
    
    for i in range(N):
        for j in range(M):
            print(res[i][j], end=' ')
        print()
    
if __name__ == '__main__':
    main()