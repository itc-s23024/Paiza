def vision_test():
    answers = [input().split() for _ in range(5)]
    correct_count = sum(1 for displayed, answered in answers if displayed == answered)

    return "OK" if correct_count >= 3 else "NG"


result = vision_test()
print(result)
