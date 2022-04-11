import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    X = input()
    res = []
    for i in range(1, len(X)-1):
        for j in range(i+1, len(X)):
            lis = []
            lis.append(X[0:i][::-1])
            lis.append(X[i:j][::-1])
            lis.append(X[j:len(X)][::-1])
            res.append(''.join(lis))
    
    print(sorted(res)[0])    
    
if __name__ == '__main__':
    main()