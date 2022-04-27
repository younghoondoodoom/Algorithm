import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    st1 = list(input())
    st2 = []
    
    for _ in range(int(input())):
        command = input().split(' ')
        if command[0] == "L":
            if st1:
                st2.append(st1.pop())
        
        elif command[0] == "D":
            if st2:
                st1.append(st2.pop())
        
        elif command[0] == "B":
            if st1:
                st1.pop()
        
        else:
            st1.append(command[1])
        
    st1.extend(reversed(st2))
    print(''.join(st1))
    
if __name__ == '__main__':
    main()