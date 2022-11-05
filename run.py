# welcome user
print("Welcome to Learners Drivers Test! ")
username = input("Enter your name?: ")
id_number = input("Enter your ID number")
email = input("Enter your email address")
print("hey", username, " you need to get all quesntions/Begin Test!")

# guesses
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# answers
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# scores
def display_score(correct_guesses, guesses):
    print("RESULTS")
    

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# ask user if they want to restart test
def play_again():

    response = input("Do you want to start again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions = {
 "What is the lagal age to drive a car?: ": "A",
 "Are you allowed to overtake?: ": "B",
 "How much is the penalty for overspeeding?: ": "C",
 "How many passengers are allowed in a car?: ": "A"
}

options = [["A. 18", "B. 21", "C. 16", "D. 18 and 21"],
          ["A. Yes", "B. No", "C. Maybe", "D. Someimes"],
          ["A. 1000", "B. 2000", "C. 3000", "4000"],
          ["A. 8","B. 9", "C. 10", "D. 2"]]

new_game()

while play_again():
    new_game()

print("Thank you!")

# end
