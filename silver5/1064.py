import sys

def intput():
    return sys.stdin.readline().rstrip()

def main():
    x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split(' '))
    try:
        i = (x_a - x_b) / (y_a - y_b)
    except ZeroDivisionError:
        i = 0
    try:
        j = (x_a - x_c) / (y_a - y_c)
    except ZeroDivisionError:
        j = 0
    try:
        k = (x_b - x_c) / (y_b - y_c)
    except ZeroDivisionError:
        k = 0
    
    if i == j == k:
        return -1.0
    
    lis = [((x_a - x_b)**2 + (y_a - y_b)**2)**0.5, ((x_a - x_c)**2 + (y_a - y_c)**2)**0.5, ((x_b - x_c)**2 + (y_b - y_c)**2)**0.5]
    lis.sort()
    return(abs(2*(lis[0] - lis[2])))
    
    
    

if __name__ == '__main__':
    print(main())