easyQuestions = {
    "3 + 7": "10",
    '"hi" * 3': "hihihi",
    "len([1, 2, 3])": "3",
    "5 > 2": "True"
}
mediumQuestions = {
    "python[1:4]": "yth",
    "17 % 5": "2",
    "9 // 2": "4",
    "[4, 5, 6][1]": "5"
}
hardQuestions = {
    'len("abc" * 2)': "6",
    "(3 + 2) * 4": "20",
    'len("abcdef"[2:5])': "3",
    "[4, 5, 6][1]": "5"
}
points = 0

def questionMode(mode):
    global points
    if mode == easyQuestions:
        print("EASY MODE\n")
    elif mode == mediumQuestions:
        print("MEDIUM MODE\n")
    elif mode == hardQuestions:
        print("HARD MODE\n")
    for question in mode:
        print(f"Question: {question}")
        answer = input("Answer: ")
        if answer.lower() == mode[question].lower():
            points += 1
            print("Correct\n")
        else:
            print("Incorrect")
            print(f"Correct answer: {mode[question]}\n")

questionMode(easyQuestions)
questionMode(mediumQuestions)
questionMode(hardQuestions)

print(f"Points: {points}")