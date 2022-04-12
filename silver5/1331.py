import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    lis = list()
    for _ in range(36):
        lis.append(input())
    
    if len(set(lis)) == 36:
        flag = True
        x1, y1 = list(lis[0])
        x2, y2 = list(lis[-1])
        l1 = abs(ord(x1) - ord(x2))
        l2 = abs(int(y1) - int(y2))
        if l1 == 2 and l2 == 1:
            pass
        elif l2 == 2 and l1 == 1:
            pass
        else:
            return("Invalid")
        for i in range(35):
            a, n = list(lis[i])
            b, m = list(lis[i+1])
            k1 = abs(ord(a) - ord(b))
            k2 = abs(int(n) - int(m))
            if k1 == 2 and k2 == 1:
                continue
            elif k2 == 2 and k1 == 1:
                continue
            else:
                flag = False
                break
        if flag:
            return("Valid")
        else:
            return("Invalid")                
    else:   
        return("Invalid")

if __name__ == '__main__':
    print(main())