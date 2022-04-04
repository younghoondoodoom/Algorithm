import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lis = list()
    
    for _ in range(N):
        sent = list()
        for __ in range(5):
            s = input()
            sent.append(s)
        lis.append(sent)
    
    samecnt = 0
    first = 0
    second = 0
    for i in range(N-1):
        for j in range(i+1, N):
            cnt = 0
            for x in range(5):
                for y in range(7):
                    if lis[i][x][y] == lis[j][x][y]:
                        cnt += 1
            if cnt > samecnt:
                samecnt = cnt
                first = i
                second = j
    if first == 0 and second == 0:
        print("1 2")
    else:
        print(f"{first+1} {second+1}")
                
if __name__ == "__main__":
    main()