import sys

def intput():
    return sys.stdin.readline().rstrip()

def main():
    a, b = map(int, input().split(' '))
    lis = [0]
    for i in range(46):
        for j in range(i):
            lis.append(i)
    
    print(sum(lis[a:b+1]))
    
if __name__ == '__main__':
    main()