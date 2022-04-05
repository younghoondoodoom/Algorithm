import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = list()
    for _ in range(N):
        dist = list(map(int, input().split(" ")))
        lis.append(dist)
    
    space = [[0 for _ in range(101)] for _ in range(101)]
    
    for i in range(N):
        x = lis[i][0]
        y = lis[i][1]
        for a in range(x, x+10):
            for b in range(y, y+10):
                space[a][b] = 1
            
    cnt = 0
    for x in space:
        cnt += x.count(1)
    
    print(cnt)   
    
if __name__ == '__main__':
    main()