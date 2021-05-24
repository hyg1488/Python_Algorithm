def solution(arr):
    answer = []
    if(len(arr) == 1): answer = arr
    else :
        for i in range(len(arr)-1):
            if(i == len(arr)-2): 
                answer.append(arr[i])
                if(arr[i] != arr[i+1]):
                    answer.append(arr[i+1])
            elif(arr[i] == arr[i+1]): continue
            else: answer.append(arr[i])
        
    print(answer)


solution([1,1,3,3,0,1,1,0])



# 추천 코드
# 감탄 : 이걸 슬라이싱으로 만들수 있구나.... 핵심은 a[-1:]
def no_continuous(s):
    a = []
    for i in s:
        print(a)
        print(a[-1:])
        if a[-1:] == [i]: continue
        a.append(i)
    return a

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( no_continuous( "133303" ))