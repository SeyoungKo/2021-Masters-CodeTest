alpha = ['B','W','O','G','Y','R']
arr = []

# 큐브 3차원 리스트 생성
for i in range(len(alpha)):
    n = [ [0] * 3 for m in range(3)]
    for j in range(3):
        for k in range(3):
            n[j][k] = alpha[i]
    arr.append(n)

# 큐브 상태 출력
for i, value in enumerate(arr):
    for j, value1 in enumerate(range(3)):
        for k, value2 in enumerate(range(3)):
            print(arr[i][j][k], end=" ")
        print(' ')
    print('')

