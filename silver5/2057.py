import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    
    if N == 0: N = -1
    res = 2432902008176640000
    for i in range(20, 0, -1):
       res //= i
       if N >= res:
           N = N - res
    
    if N == 0:
        print("YES")
    else:
        print("NO")
    


if __name__ == '__main__':
    main()