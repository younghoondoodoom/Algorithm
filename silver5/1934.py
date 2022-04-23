import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    
    for _ in range(T):
        a, b = map(int, input().split(' '))
        max_num = max(a, b)
        for n in range(max_num, a * b + 1, max_num):
            if n % a == 0 and n % b == 0:
                print(n)
                break


if __name__ == "__main__":
    main()