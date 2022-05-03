import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = list(map(int, input().split(' ')))
    dic = dict()
    res = [-1] * N
    stack = []
    
    for i in lis:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    
    for i in range(N):
        while stack:
            if dic[lis[i]] > dic[lis[stack[-1]]]:
                res[stack.pop()] = lis[i]
            else:
                break
        stack.append(i)
    
    print(*res)
    
if __name__ == '__main__':
    main()