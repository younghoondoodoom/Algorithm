import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    board_list = input().split('.')
    for i in range(len(board_list)):
        length = len(board_list[i])
        if length == 0:
            continue
        if length % 4 == 0:
            board_list[i] = board_list[i].replace('X', 'A')
        elif length % 4 == 2:
            board_list[i] = board_list[i].replace('XXXX', 'AAAA')
            board_list[i] = board_list[i].replace('XX', 'BB')
        elif length % 2 == 0:
            board_list[i] = board_list[i].replace('XX', 'BB')
        else:
            return -1
    return('.'.join(board_list))
    
if __name__ == '__main__':
    print(main())
