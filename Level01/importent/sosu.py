# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
# 문제 링크 https://programmers.co.kr/learn/courses/30/lessons/12921?language=python3


# !!! 문제는 크게 어렵지 않은데, 효율을 따질때 문제가 생김... !!!
#에라토스테네스의 체 사용하기
# https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4



def solution(n): 
    answer = 0 
    prime_num=[] 
    chk=[False]*2+[True]*(n-1)    # initialize chk, chk[0],chk[1] is not prime number
    for i in range(2,n+1): 
        if chk[i]:         # if chk[i] is 
            prime_num.append(i)
            for j in range(2*i,n+1,i): 
                if chk[j]:          # chk is True
                    chk[j]=False    # chk changes false 
    answer = len(prime_num) 
    return answer


# 추천코드
