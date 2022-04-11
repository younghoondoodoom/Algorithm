import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lis = list()
    for _ in range(N):
        lis.append(input())
    lis = list(set(lis))
    lis.sort(key=lambda x: (len(x), x))

    for i in range(len(lis)):
        print(lis[i])
    
if __name__ == '__main__':
    main()