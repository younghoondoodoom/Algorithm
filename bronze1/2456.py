import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    candidate = [0] * 3
    squared = [0] * 3
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        candidate[0] += a
        candidate[1] += b
        candidate[2] += c

        squared[0] += a ** 2
        squared[1] += b ** 2
        squared[2] += c ** 2

    m = max(candidate)
    if candidate.count(m) == 1:
        for i in range(len(candidate)):
            if candidate[i] == m:
                print(i+1, m)
                break;
    else:
        pow_m = max(squared)
        elected = squared.index(pow_m)

        # 회장 선출 불가능한 경우
        if squared.count(pow_m) > 1:
            print(0, candidate[elected])
        # 회장 선출 가능한 경우
        else:
            print(elected+1, candidate[elected])

    
            

if __name__ == '__main__':
    main()