def solution(a, b):
    if(a<=12 and a>0):
      month01 = [31,29,31,30,31,30,31,31,30,31,30,31]
      answer = ['FRI','SAT','SUN','MON','TUE','WED','THU']

      if(month01[a-1]>=b and b>0):
        totalDays = 0

        for i in range(0,a-1,1):
          totalDays+= month01[i]
        totalDays += b
        print(totalDays)
        totalDays = totalDays%7-1
      
        return answer[totalDays]

print(solution(5,16))