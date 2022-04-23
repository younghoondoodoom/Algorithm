import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    S = int(input())
    
    if S == 1 or S == 2:
        return 1
    m = 0
    for n in range(1, S):
        if n*(n+1) > 2*S:
            m = n-1
            break
        elif n*(n+1) == 2*S:
            m = n
    return m

if __name__ == '__main__':
    print(main()) 