input_list = input().split()

num = int(input_list[1])
sentence = input_list[0]
move = input_list[2]

# 입력한 정수가 0보다 큰 경우
if num > 0 :
    # 입력한 정수가 단어길이보다 작은 경우
    if num <= len(sentence):
        if move.upper() == 'R':
            transfer = sentence[-num:]+sentence[:-num]

        elif move.upper() == 'L':
            transfer = sentence[num:] + sentence[:num]

    # 입력한 정수가 단어길이보다 큰 경우
    elif len(sentence) < num:
        if move.upper() == 'R':
            transfer = sentence[-num % len(sentence):] + sentence[:-num % len(sentence)]

        elif move.upper() == 'L':
            transfer = sentence[num % len(sentence):] + sentence[:num % len(sentence)]

# 입력한 정수가 0보다 작은 경우
else:
    # 입력한 정수가 단어 길이보다 큰 경우
    if num < -(len(sentence)):
        transfer = sentence[-num % len(sentence):] + sentence[:-num % len(sentence)]
    # 입력한 정수가 단어 길이보다 작은 경우
    else:
        transfer = sentence[-num:] + sentence[:-num]

print(transfer)
