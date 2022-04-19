import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    cnt = 0
    six_n = 666
    while True:
        if '666' in str(six_n):
            cnt += 1
        if cnt == N:
            print(six_n)
            break
        six_n += 1
    


if __name__ == '__main__':
    main()