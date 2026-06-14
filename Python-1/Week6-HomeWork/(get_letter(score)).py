# الدالة الأولى: تحويل الدرجة إلى حرف
def get_letter(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def pass_or_fail(letter):
    if letter == "F":
        return "Fail"
    else:
        return "Pass"

user_score = 20

result = pass_or_fail(get_letter(user_score))
print(f"Result: {result}")