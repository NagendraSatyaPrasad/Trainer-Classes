import requests
import random

URL = "http://127.0.0.1:5000/get_questions"

def start_quiz():
    res = requests.get(URL)
    data = res.json()

    score = 0

    number_of_ques = int(input("Enter number of questions: "))

    selected_questions = random.sample(data, number_of_ques)

    for i, q in enumerate(selected_questions, start=1):
        print(f"\n{i}) {q['question']}")
        print(f"a) {q['op1']}")
        print(f"b) {q['op2']}")
        print(f"c) {q['op3']}")
        print(f"d) {q['op4']}")

        ans = input("Enter your option (a/b/c/d): ")

        mapping = {
            "a": "op1",
            "b": "op2",
            "c": "op3",
            "d": "op4"
        }

        if mapping.get(ans) == q['correct']:
            score += 1
    print(f"\nMarks = {score}/{len(selected_questions)}")

if __name__ == "__main__":
     start_quiz()