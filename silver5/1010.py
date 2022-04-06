import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    for _ in range(T):
        N, M = list(map(int, input().split(' ')))
        if M > N:
            R = M - N
            m, n, r = 1, 1, 1
            for i in range(1,M+1):
                m *= i
            for i in range(1, N+1):
                n *= i
            for i in range(1, R+1):
                r *= i
            print(m // (n * r))
        else: 
            print(1)
                

if __name__ == '__main__':
    main()