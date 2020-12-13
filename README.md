# 1단계 : 단어 밀어내기 구현하기

1단계 단어밀어내기 문제

### 1. 프로젝트 소개 & 환경

1. 입력: 사용자로부터 단어 하나, 정수 숫자 하나( -100 <= N < 100) , L 또는 R을 입력받는다. L 또는 R은 대소문자 모두 입력 가능하다.
2. 주어진 단어를 L이면 주어진 숫자 갯수만큼 왼쪽으로, R이면 오른쪽으로 밀어낸다.
3. 밀려나간 단어는 반대쪽으로 채워진다.

- Python
 ```bash
 Python 3.7.3
 ```

### 2. 코딩 요구사항
- 컴파일 및 실행되지 않을 경우 불합격
- 자기만의 기준으로 최대한 간결하게 코드를 작성한다.


### 3. 해결 방안
파이썬 리스트 슬라이싱(list Slicing) 사용


### 4. 코드 설명

1단계 구현의 핵심은 다음 코드와 같습니다.
 ```
 transfer = sentence[-num:]+sentence[:-num]
 ```
 * [-num:] - 리스트의 뒤에서 num 번째 요소값부터 마지막 요소값까지
 * [:-num] - 리스트의 맨 앞부터 뒤에서 num 번째 요소값 전까지
 
 
예를 들어 입력이 A B C D와 1, R으로 주어졌을 때 
* 맨 마지막 원소 1개(앞으로 이동) + 나머지 원소 3개(뒤로 이동) = D A B C
 
패턴을 발견할 수 있습니다.
 
 
단어를 이동시킬때 고려할 조건은 다음과 같습니다.

1. 입력한 정수가 0보다 큰 경우 / 작은 경우
2. 입력한 정수가 단어의 길이보다 큰 경우 / 작은 경우

입력한 정수가 0보다 크면 R

