import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N = int(input())
    cnt = 0
    for _ in range(N):
        word = input()
        dic = dict()
        flag = True
        for i in range(len(word)):
            let = word[i]
            if let in dic.keys():
                if (i - dic[let]) != 1:
                    flag = False
                    break
                else:
                    dic[let] = i
            else:
                dic[let] = i
        if flag:
            cnt += 1
    print(cnt)
    

if __name__ == '__main__':
    main()