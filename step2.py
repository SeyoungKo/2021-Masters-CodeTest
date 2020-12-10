# U, U' - 가장 윗줄을 왼쪽/오른쪽 이동
# R, R' - 가장 오른쪽(세로)를 위/아래로 이동
# L, L' - 가장 왼쪽(세로)를 위/아래로 이동
# B, B' - 가장 아랫줄을 왼쪽/오른쪽 이동

arr = [['R', 'R', 'W'],
       ['G', 'C', 'W'],
       ['G', 'B', 'B']]

def print_cube():
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()

# 큐브 이동
def cube_transfer(num, idx):
    n = []
    for i in arr:
        n.append(i[idx])
    transfer = n[num:] + n[:num]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == idx:
                arr[i][j] = transfer[i]
    print_cube()

def move_vertical(move, idx):
    # 위로 이동
    if move.find('\'') is -1:
        num = -1
    # 아래로 이동
    else:
        num = 1
    cube_transfer(int(num), int(idx))

    # if move == 'R':
    #
    #     for i in arr:
    #         n.append(i[2])
    #     transfer = n[-1:] + n[:-1]
    #
    #     for i in range(len(arr)):
    #         for j in range(len(arr[i])):
    #             if j ==2:
    #                 arr[i][j] = transfer[i]
    #
    # elif move == 'R\'':
    #     for i in arr:
    #         n.append(i[2])
    #     transfer = n[1:] + n[:1]
    #
    #     for i in range(len(arr)):
    #         for j in range(len(arr[i])):
    #             if j ==2:
    #                 arr[i][j] = transfer[i]
    #
    # print_cube()

# def move_horizontal(move, index):

print_cube()
print(' ')
while True:
    input_list = input('CUBE > ').split()
    idx =0

    # 세로 이동
    if input_list[0] == 'R' or 'R\'':
        idx = 2

    elif input_list[0] == 'L' or 'L\'':
        idx = 0
    move_vertical(input_list[0], idx)

    # 가로 이동
    if input_list[0] == 'U' or 'U\'':
        idx = 0
        # move_horizontal(input_list[0], idx)

    elif input_list[0] == 'B' or 'B\'':
        idx = 2
        # move_horizontal(input_list[0], idx)

    # 종료
    if input_list[0] == 'Q':
        print('Bye~')
        break


