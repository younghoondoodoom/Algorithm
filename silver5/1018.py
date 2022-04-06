# 8x8이 될 수 있는 모든 경우의 수를 찾는다.
# 일단 자르고 왼쪽 맨끝을 기준으로 오른쪽으로 가면서 cnt를 한다.
import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    N, M = list(map(int, input().split(' ')))
    board = []
    for _ in range(N):
        board.append(input())
    
    min_cnt = 64
    
    for i in range(N-7):
        for j in range(M-7):
            for std in ["W", "B"]:
                cnt = 0
                # 1, 3, 5, 7번째 줄은 std와 첫번째 색이 같다.
                for k in range(0, 7, 2):
                    for l in range(0, 7, 2):
                        if board[i+k][j+l] != std:
                            cnt += 1
                    for l in range(1, 8, 2):
                        if board[i+k][j+l] == std:
                            cnt += 1
                # 2, 4, 6, 8번째 줄은 std와 첫번째 색이 다르다.
                for k in range(1, 8, 2):
                    for l in range(0, 7, 2):
                        if board[i+k][j+l] == std:
                            cnt += 1
                    for l in range(1, 8, 2):
                        if board[i+k][j+l] != std:
                            cnt += 1
                if cnt < min_cnt:
                    min_cnt = cnt
    
    print(min_cnt)
    
if __name__ == "__main__":
    main()