arr = [['R', 'R', 'W'],
       ['G', 'C', 'W'],
       ['G', 'B', 'B']]

# 큐브 상태 출력
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


# 큐브 초기 상태
print_cube()
while True:
# 사용자 입력
    input_str = input('CUBE > ')
    idx = 0

    for i in input_str:
        if i.find('\'') is -1:
            num = 1
            if i == 'R' or 'B':
                idx = 2
                if i == 'R':
                    vertical_transfer(num, idx)
                # B의 경우 U와 방향이 반대
                elif i == 'B':
                    horizontal_transfer(-num, idx)

            if i == 'L' or 'U':
                idx = 0
                if i == 'L':
                    # L의 경우 R과 방향이 반대
                    vertical_transfer(-num, idx)
                elif i == 'U':
                    horizontal_transfer(num, idx)

        else:
            num = -1
            if i == 'R\'' or 'B\'':
                idx = 2
                if i == 'R\'':
                    vertical_transfer(num, idx)
                # B의 경우 U와 방향이 반대
                elif i == 'B\'':
                    horizontal_transfer(-num, idx)

            if i == 'L\'' or 'U\'':
                idx = 0
                if i == 'L\'':
                    # L의 경우 R과 방향이 반대
                    vertical_transfer(-num, idx)
                elif i == 'U\'':
                    horizontal_transfer(num, idx)

    # 종료
    if input_str[0] == 'Q':
        print('Bye~')
        break
