import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    X = int(input())
    cnt = 0
    
    while True:
        if X < 10:
            break
        X = list(map(int, str(X)))
        X = sum(X)
        cnt += 1
        
    print(cnt)
    if X % 3 == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()