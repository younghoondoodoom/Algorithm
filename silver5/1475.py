import sys
import math

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = list(map(int, input()))
    lis = [0] * 10
    
    for i in N:
        if i == 9:
            i = 6
        lis[i] += 1
    lis[6] = (lis[6] + 1) // 2
    return(max(lis))
               
        


if __name__ == '__main__':
    print(main())