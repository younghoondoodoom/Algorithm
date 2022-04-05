import sys

def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        res = [0 for _ in range(8)]
        test = input()
        for i in range(2, 40):
            s = ""
            s += test[i-2]
            s += test[i-1]
            s += test[i]
            if s == "TTT":
                res[0] += 1
            elif s == "TTH":
                res[1] += 1
            elif s == "THT":
                res[2] += 1
            elif s == "THH":
                res[3] += 1
            elif s == "HTT":
                res[4] += 1
            elif s == "HTH":
                res[5] += 1
            elif s == "HHT":
                res[6] += 1
            else:
                res[7] += 1
        for x in res:
            print(x, end=" ")


if __name__ == '__main__':
    main()