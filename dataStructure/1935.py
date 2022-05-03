import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    rear = list(input())
    lis = []
    for _ in range(N):
        lis.append(int(input()))
    res = []
    for i in rear:
        x = ord(i)
        if x >= 65:
            res.append(lis[ord(i)-65])
        else:
            res.append(i)

    stack = []
    for i in range(len(res)):
        if type(res[i]) == int:
            stack.append(res[i])
        else:
            int1 = stack.pop()
            int2 = stack.pop()
            
            if res[i] == "+":
                stack.append(int2+int1)
            elif res[i] == "-":
                stack.append(int2-int1)
            elif res[i] == "*":
                stack.append(int2*int1)
            else:
                stack.append(int2/int1)
    print('%.2f' %stack[0])
            
    
    

if __name__ == '__main__':
    main()