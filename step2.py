arr = [['R', 'R', 'W'],
       ['G', 'C', 'W'],
       ['G', 'B', 'B']]


def print_cube():
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print(' ')


# 이동한 큐브 재배치
def relocation(n, num, loc):
    transfer = n[num:] + n[:num]
    if loc == 'vertical':
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if j == idx:
                    arr[i][j] = transfer[i]

    elif loc == 'horizontal':
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i == idx:
                    arr[i][j] = transfer[j]

    print_cube()


# 위/아래 큐브 이동
def vertical_transfer(num, idx):
    n = []
    for i in arr:
        n.append(i[idx])
    relocation(n, num, loc='vertical')


# 오/왼 큐브 이동
def horizontal_transfer(num, idx):
    n = []
    for i in range(len(arr)):
        if i == idx:
            for j in range(len(arr[i])):
                n.append(arr[i][j])
    relocation(n, num, loc='horizontal')


print_cube()

while True:
    input_list = input('CUBE > ').split()
    idx = 0

    if input_list[0].find('\'') is -1:
        num = 1
        if input_list[0] == 'R' or 'B':
            idx = 2
            if input_list[0] == 'R':
                vertical_transfer(int(num), int(idx))
            # B의 경우 U와 방향이 반대
            elif input_list[0] == 'B':
                horizontal_transfer(-num, idx)

        if input_list[0] == 'L' or 'U':
            idx = 0
            if input_list[0] == 'L':
                # L의 경우 R과 방향이 반대
                vertical_transfer(int(-num), int(idx))
            elif input_list[0] == 'U':
                horizontal_transfer(num, idx)

    else:
        num = -1
        if input_list[0] == 'R\'' or 'B\'':
            idx = 2
            if input_list[0] == 'R\'':
                vertical_transfer(int(num), int(idx))
            # B의 경우 U와 방향이 반대
            elif input_list[0] == 'B\'':
                horizontal_transfer(-num, idx)

        if input_list[0] == 'L\'' or 'U\'':
            idx = 0
            if input_list[0] == 'L\'':
                # L의 경우 R과 방향이 반대
                vertical_transfer(int(-num), int(idx))
            elif input_list[0] == 'U\'':
                horizontal_transfer(num, idx)

    # 종료
    if input_list[0] == 'Q':
        print('Bye~')
        break
