import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    T = int(input())
    for _ in range(T):
        ps = input()
        lis = []
        flag = True
        for i in ps:
            if i == '(':
                lis.append(i)
            elif i == ')':
                if len(lis) == 0:
                    flag = False
                    break
                else:
                    lis.pop()
        if len(lis) != 0:
            flag = False
        if flag:
            print("YES")
        else:
            print("NO")
                

if __name__ == '__main__':
    main()