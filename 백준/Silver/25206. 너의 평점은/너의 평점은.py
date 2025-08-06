import sys

dict_grade = {
    'A+': 4.5,'A0': 4.0,'B+': 3.5,'B0': 3.0,'C+': 2.5,'C0': 2.0,'D+': 1.5,'D0': 1.0,'F': 0.0
}

cal_score = 0.0
total_score = 0.0

for _ in range(20):
    subject, score, grade = sys.stdin.readline().strip().split()
    score = float(score)
    
    if grade != "P":
        cal_score += score * dict_grade[grade]
        total_score += score

if cal_score == 0.0:
    print(0.000000)
else:
    print(round(cal_score/total_score, 6))
    