import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    X, Y, W, S = map(int, input().split())
    X, Y = min(X, Y), max(X, Y)
    m = (X+Y)%2
    print(min((X+Y)*W, X*S + (Y-X)*W, (Y-m)*S + m*W))
    
if __name__ == '__main__':
    print(main())