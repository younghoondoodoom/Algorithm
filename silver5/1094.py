import sys

def intput():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    
    length = [64]
    flag = True
    
    while flag:
        summary = sum(length) 
        if summary == N:
            flag = False
        
        if summary > N:
            x = length.pop(-1)
            length.append(x//2)
            if sum(length) < N:
                length.append(x//2)
    
    print(len(length))
    

if __name__ == '__main__':
    main()