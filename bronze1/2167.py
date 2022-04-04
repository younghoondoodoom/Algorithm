import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    lis = [int(x) for x in input().split(' ')]
    N, M = lis
    graph = [[] for _ in range(N)]
    
    for i in range(N):
        lis = [int(x) for x in input().split(' ')]
        for j in range(M):
            graph[i].append(lis[j])
    
    K = int(input())
    res = list()
    for _ in range(K):
        summary = 0
        lis = [int(x) for x in input().split(' ')]
        i, j, x, y = lis
        for n in range(i-1, x):
            for m in range(j-1, y):
                summary += graph[n][m]
        res.append(summary)

    for i in range(K):
        print(res[i])
    
if __name__ == "__main__":
    main()