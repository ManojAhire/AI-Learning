from question import question
question_prompts = ["what is the capital of India?\n(a) New Delhi\n(b) Mumbai\n(c) Kolkata",
                    "what is 2+2?\n(a) 3\n(b) 4\n(c) 5",
                    "what is 3*2?\n(a) 6\n(b) 9\n(c) 12"]


questions=[
    question(question_prompts[0],"a"),
    question(question_prompts[1],"b"),
    question(question_prompts[2],"a")
]


def run_quiz(questions):
    score=0
    for q in questions:
        print(q.prompt)
        answer=input()
        if answer==q.answer:
            score+=1
    print("you got",score,"out of",len(questions),"correct")
run_quiz(questions)



