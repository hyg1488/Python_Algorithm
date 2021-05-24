#단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 제한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

# 문제 링크  https://programmers.co.kr/learn/courses/30/lessons/12903?language=python3

def solution(s):
    num = int(len(s)/2)
    answer = ''
    if(len(s)%2 == 0):
      answer = s[num-1]+s[num]
    elif(len(s) == 1): 
      answer = s
    elif(len(s)==2): 
      answer = s
    else : answer = s[num]
    return answer



# 추천 코드
def string_middle(str):
    # 함수를 완성하세요

    return str[(len(str)-1)//2:len(str)//2+1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(string_middle("power"))