def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1


    for key in questions:
        print(key)
        for i in options[question_num-1]:
            print(i)

def check_answer():
    pass
def display_score():
    pass
def try_again():
    pass
    
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


