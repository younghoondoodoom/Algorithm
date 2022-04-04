import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lis = ['.'*(N+2)] + ['.'+input()+'.' for _ in range(N)] + ['.'*(N+2)]
    res = [] 
    for i in range(N):
        i += 1
        s = ''
        for j in range(N):
            j += 1
            if ord('0') <= ord(lis[i][j]) <= ord('9'):
                s += '*'
            else:
                bomb = 0
                for k in range(i-1, i+2):
                    for l in range(j-1, j+2):
                        doo = lis[k][l]
                        if ord('0') <= ord(doo) <= ord('9'):
                            bomb += int(doo)
                s += str(bomb) if bomb < 10 else "M"
        res.append(s)
    for s in res:
        print(s)
    
    
    
if __name__ == '__main__':
    main()