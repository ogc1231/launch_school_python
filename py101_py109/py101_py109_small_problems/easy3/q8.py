def get_grade(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum / 3
    
    if avg <= 100 and avg >= 90:
        return 'A'
    elif avg <= 89 and avg >= 80:
        return 'B'
    elif avg <= 79 and avg >= 70:
        return 'C'
    elif avg <= 69 and avg >= 60:
        return 'D'
    elif avg <= 59 and avg >= 0:
        return 'F'
    
    



print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True