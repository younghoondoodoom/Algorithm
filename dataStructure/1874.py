import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    n = int(input())
    res = []
    stack = []
    flag = True
    cur = 1
    for i in range(n):
        num = int(input())
        while cur <= num:
            stack.append(cur)
            res.append("+")
            cur+=1
        
        if num == stack[-1]:
            stack.pop()
            res.append("-")
        else:
            print("NO")
            flag = False
            break
    
    if flag:
        for i in res:
            print(i)
            

if __name__ == '__main__':
    main()