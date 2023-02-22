# quiz.py

# Define a list of questions and answers
questions = [
    "What is the capital of India?",
    "What is the largest planet in our solar system?",
    "What is the largest country in world?"
]
answers = [
    "New Delhi",
    "Jupiter",
    "Russia"
]

# Define a function to run the quiz
def run_quiz():
    score = 0
    for i in range(len(questions)):
        user_answer = input(questions[i] + " ")
        if user_answer.lower() == answers[i].lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print("Your final score is " + str(score) + " out of " + str(len(questions)))

# Run the quiz
run_quiz()
