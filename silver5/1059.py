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
    
    if 0 < i < L:
        min_num = S[i-1]
        max_num = S[i+1]
        return (n-min_num) * (max_num-n) - 1
    
    elif i == 0:
        max_num = S[1]
        return n * (max_num-n) - 1
    
    
if __name__ == '__main__':
   print(main())