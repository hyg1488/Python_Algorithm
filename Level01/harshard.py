# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
# 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/12947?language=python3

def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0 # 반복문 돌리면 str문자열을 char 로 c에 집어넣는다.
                # sum 에 list 를 넣으면 알아서 모든 리스트 값을 더함.
        # [c for c in str(n)] c라는 리스트에 넣고 int(c) 로 정수로 변환

print(Harshad(18))

# n = "테스트"
# for i in str(n):
#     print(i)

# list = (1,2,3,4)

# print(sum(list))