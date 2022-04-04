import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = 1
    while True:
        if N > (10 ** M):
            N = round(N+0.1, -M)
        else: break
        
        M += 1
            
    print(int(N))
            
    
    
    
if __name__ == '__main__':
    main()