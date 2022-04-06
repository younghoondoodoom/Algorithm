import sys

def input() :
    return sys.stdin.readline().rstrip()

def main() :
    N = int(input())
    lis = list()
    for _ in range(N):
        lis.append(int(input()))
    lis.sort()
    for i in range(N):
        print(lis[i])

if __name__ == '__main__':
    main()