#create a quiz game that asks the user questions and checks if the answer is correct

import time


questions = ("What is the capital of France?", 
             "What is 2 + 2?", 
             "What is the capital of the United States?")

#this is where we store the options for each question
options = (("A. Paris", "B. London", "C. Berlin"), 
           ("A. 3", "B. 4", "C. 5"), 
           ("A. New York", "B. Washington D.C.", "C. Los Angeles"))

answers = ("A. Paris", "B. 4", "B. Washington D.C.")

guesses = []
score = 0
question_number = 0


for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_number]: #use this inner loop to print the options for each question at the correct row number
        print(option)

    guess = input("Enter (A, B, or C): ").upper()
    guesses.append(guess)
    if guess == answers[question_number][0]:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
        time.sleep(1)
        print(f"The correct answer is {answers[question_number]}")
    time.sleep(1)
    question_number += 1
  


print("--------------------")
print("Quiz Results")
print("--------------------")

print("answers: ", answers)
for answer in answers:
    print(answer)
print()

print("guesses: ", guesses)
for guess in guesses:
    print(guess)
print()

score_percentage = int((score / len(questions)) * 100)

print(f"Your score is {score}/{len(questions)} or {score_percentage}%")