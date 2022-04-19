import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lis = [0] * 10001
    for _ in range(N):
        n = int(input())
        lis[n] += 1
    
    for i in range(10001):
        if lis[i] != 0:
            for j in range(lis[i]):
                print(i)

if __name__ == '__main__':
    main()