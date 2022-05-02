import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    X = input()
    stack = []
    cnt = 0
    for i in range(len(X)):
        if X[i] == ")":
            stack.pop()
            if X[i-1] == "(":
                cnt += len(stack)
            else:
                cnt += 1
        elif X[i] == "(":
            stack.append("(")
    
    print(cnt)
        

    
    

if __name__ == '__main__':
    main()