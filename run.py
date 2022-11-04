import gspread
from google.oauth2.service_account import Credentials
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

#welcome the user
print("Welcome to Learners Drivers Test! ")
username = input("Username?: ")
print("hey", username,"you need to get all quesntions/Begin Test!")

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


def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

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


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False




questions = {
 "When can you overtake on the left?: ": "A",
 "When driving at night when should you dip your headlights?: ": "B",
 "What does a broken yellow line mean?: ": "C",
 "What does a single continuous yellow line mean??: ": "A"
}
options = [["A.  When the driver in front of you is turning right", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B.  You’re meeting on-coming traffic", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. A broken yellow line signifies the edge of the roadway", "D. SNL"],
          ["A. A single yellow line signifies parking is prohibited at certain times","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
