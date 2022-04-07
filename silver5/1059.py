import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    L = int(input())
    S = list(map(int, input().split(' ')))
    n = int(input())
    
    if n in S:
        return 0
    
    S.append(n)
    S.sort()
    
    i = S.index(n)
    min_num = S[i-1]
    max_num = S[i+1]
    return (n-min_num-1) * (max_num-n) + (max_num-n-1)
   
if __name__ == '__main__':
   print(main())