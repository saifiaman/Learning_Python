# Python Quiz Game
# This script implements a simple quiz game that asks the user multiple-choice questions.

# Queestion and Options for the Quiz Game
questions = ("How many elements are there in the Periodic Table?",
             "What is the capital of France?",
             "What is the largest planet in our solar system?",
             "What is the smallest prime number?",)

options = (("A) 118", "B) 120", "C) 115", "D) 100"),
           ("A) Paris", "B) London", "C) Berlin", "D) Madrid"),
           ("A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"),
           ("A) 0", "B) 1", "C) 2", "D) 3"),)

input_answer = []
score = 0
correct_answers = ("A", "A", "B", "C")

for question in range(len(questions)):
    print()
    print("-------------------*************************---------------------")
    print()
    print(questions[question])
    for option in options[question]:
        print(option)
    answer = input("Enter your answer (A, B, C, or D): ").upper()
    input_answer.append(answer)
    if (input_answer[question] == correct_answers[question]):
        print("correct")
        score += 1
    else:
        print("incorrect, The correct answer is", correct_answers[question])

# Check if the answers are correct
if len(input_answer) != len(questions):
    print("You did not answer all questions.")
    exit()
if (len(input_answer) == len(questions)):
    print("You answered all questions.")
# Print the score
print("Your score is", score, "out of", len(questions))
# Print the percentage score
percentage_score = (score / len(questions)) * 100
print("Your percentage score is", percentage_score, "%")
