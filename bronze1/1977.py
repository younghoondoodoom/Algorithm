import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    M = int(input())
    N = int(input())

    # for문으로 무조건 돌려보기
    lis = list()

    for i in range(1, 100+1):
        n=i**2
        if M <= n <= N:
            lis.append(n)
            continue
        elif n > N:
            break
    
    if not lis:
        print(-1)
    else:
        print(sum(lis))
        print(lis[0])

if __name__ == "__main__":
    main()