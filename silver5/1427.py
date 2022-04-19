import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = list(input())
    N.sort(reverse=True)
    print(''.join(N))    


if __name__ == '__main__':
    main()