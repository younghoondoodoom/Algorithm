import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = [int(input()) for _ in range(N)]
    cnt = 0
    while True:
        maximum = max(lis)
        idx = lis.index(maximum)
        if idx == 0:
            if lis.count(maximum) >= 2:
                cnt += 1
            break;
        lis[idx] -= 1
        lis[0] += 1
        cnt += 1
    print(cnt)
    
        
    
    
    

if __name__ == '__main__':
    main()