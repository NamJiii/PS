def solution(scores):
    answer = ''
    student_num = len(scores)
    
    for i in range(student_num):
        self_review = scores[i][i]
        high = 0
        low = 100
        total_scores = 0
        
        for j in range(student_num):
            total_scores = total_scores + scores[j][i]
            if i == j :
                continue
            else :
                if high < scores[j][i]:
                    high = scores[j][i]
                elif low > scores[j][i]:
                    low = scores[j][i]
                    
        if self_review > high or self_review < low:
            result = (total_scores-self_review)/(student_num-1)
        else :
            result = total_scores/student_num
        if result>=90:
            answer = answer +'A'
        elif result>=80:
            answer = answer +'B'
        elif result>=70:
            answer = answer +'C'
        elif result>=50:
            answer = answer +'D'
        else:
            answer = answer +'F'

    return answer
