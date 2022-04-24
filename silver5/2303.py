import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    res = []
    
    for _ in range(N):
        lis = list(map(int, input().split(' ')))
        max_one = 0
        for i in range(3):
            for j in range(i + 1, 4):
                for k in range(j + 1, 5):
                    one = int(str(lis[i] + lis[j] + lis[k])[-1])
                    if  one > max_one:
                        max_one = one
        res.append(max_one)
    
    max_num = max(res)
    if res.count(max_num) > 1:
        lis = [i for i in range(N) if res[i] == max_num]
        return(max(lis) + 1)
    return(res.index(max(res))+1)


if __name__ == '__main__':
    print(main())