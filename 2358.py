import sys
import math

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    x_dic = dict()
    y_dic = dict()
    
    for _ in range(N):
        x, y = map(int, input().split(' '))
        if x in x_dic.keys():
            x_dic[x].append(y)
        else:
            x_dic[x] = [y]
        
        if y in y_dic.keys():
            y_dic[y].append(x)
        else:
            y_dic[y] = [x] 
    
    cnt = 0
    
    for i in x_dic.keys():
        if len(x_dic[i]) >= 2:
            cnt += 1
            
    for i in y_dic.keys():
        if len(y_dic[i]) >= 2:
            cnt += 1
            
    return cnt



if __name__ == '__main__':
    print(main())