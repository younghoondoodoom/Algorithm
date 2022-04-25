import sys


import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        lis = input().split(' ')
        for i in range(len(lis)):
            print(lis[i][::-1], end = ' ')


if __name__ == '__main__':
    main()