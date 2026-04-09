import requests
import json

while True:
    print("1 to add a question")
    print("2 save with all the options")
    print("3 to modify")
    print("4 to delete")
    print("5 exit")

    opt = int(input("Enter you option"))

    if opt == 1:
        url = "http://127.0.0.1:5000/add_question"

        payload = json.dumps({
        "question": "Captial of India",
        "op1": "Hyderabad",
        "op2": "New Delhi",
        "op3": "Mumbai",
        "op4": "Chennai",
        "correct": "op2"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        print(response.text)

    elif opt == 2:
        url = "http://127.0.0.1:5000/get_questions"

        payload = ""
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
    elif opt == 3:
        url = "http://127.0.0.1:5000/update_question/3"

        payload = json.dumps({
        "question": "Capital of India is?",
        "op1": "Delhi",
        "op2": "New Delhi",
        "op3": "Mumbai",
        "op4": "Kolkata",
        "correct": "op2"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("PUT", url, headers=headers, data=payload)

        print(response.text)

    elif opt == 4:
        url = "http://127.0.0.1:5000/delete_question/3"

        payload = json.dumps({
        "question": "Capital of India is?",
        "op1": "Delhi",
        "op2": "New Delhi",
        "op3": "Mumbai",
        "op4": "Kolkata",
        "correct": "op2"
        })
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("DELETE", url, headers=headers, data=payload)

        print(response.text)

    elif opt == 5:
        break 