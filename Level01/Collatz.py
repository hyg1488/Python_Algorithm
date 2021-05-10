# 1937년 Collatz란 사람에 의해 제기된 이 추측은, 
# 주어진 수가 1이 될때까지 다음 작업을 반복하면, 
# 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

#1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12943?language=python3

def solution(num):
    x=0
    i=0

    while(num != 1):
        if(num%2 == 0):
            num = num/2
        else:
            num = num*3+1
        i=i+1
        if(i==500):
            i=-1
            break
    answer = i
    return answer