import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    space = [[0 for _ in range(101)] for _ in range(101)]
    
    for _ in range(4):
        x, y, X, Y = [int(x) for x in input().split(" ")]
        for i in range(y, Y+1):
            for j in range(x, X+1):
                space[i][j] = 1
    
    cnt = 0
    for a in space:
        cnt += a.count(1)
    
    print(cnt) 
    


if __name__ == '__main__':
    main()