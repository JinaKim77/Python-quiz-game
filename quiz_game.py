import time
import quiz_lists
import random
import string

# Each function should have a single purpose
# and a name that describes that purpose.


# Add a default delay
def print_pause(message_to_print, delay=1):
    print(message_to_print)
    time.sleep(delay)


def intro():
    typewriter_simulator("Look, we get it;\nwe've all done a fair"
                         "amount of quizzing over the past two years\n")
    typewriter_simulator("and you might find yourself "
                         "feeling a bit quizzed-out,\n")
    typewriter_simulator("but now that we can see each other in person\n"
                         "we're also realising\n"
                         "that we might need a bit of a structure "
                         "to socialising.\n")
    typewriter_simulator("Because we've basically forgotten how to do it...\n")
    typewriter_simulator("Which is why an easy quiz is "
                         "the perfect solution.\n")


# Make text simulate typing
def typewriter_simulator(message):
    for char in message:
        print(char, end='', flush=True)
        if char in string.punctuation:
            time.sleep(0.5)
        time.sleep(0.03)


def valid_input(prompt, options):

    while True:
        choice = input(prompt)
        if choice == options:
            typewriter_simulator("Wait.......")
            return choice
        else:
            return choice


def choices(score, level):
    level_choice = valid_input("\nThere are three different levels "
                               "to choose from\n"
                               u'♠'"  Enter 1. Easy\n"
                               u'♠'"  Enter 2. Medium\n"
                               u'♠'"  Enter 3. Difficult\n"
                               u'♠'"  Enter 4. Quit\n",
                               ['1', '2', '3', '4'])
    if '1' == level_choice:
        typewriter_simulator("Easy level.\n")
        play_game(score, 0)
    elif '2' == level_choice:
        typewriter_simulator("Medium level.\n")
        play_game(score, 1)
    elif '3' == level_choice:
        typewriter_simulator("difficult level.\n")
        play_game(score, 2)
    elif '4' == level_choice:
        typewriter_simulator("\nGood bye!\n")
        quit()
    else:
        choices(score, level)


def play_game(score, level):
    typewriter_simulator("Answer 10 questions!\n")
    score = 0
    # Questions will be randomly picked
    for quiz in range(10):
        typewriter_simulator(f"\nQuestion{quiz+1}. ")
        choice = input(quiz_lists.questions[level][quiz]+"\nEnter Answer : ")

        if quiz_lists.answers[level][quiz].lower() in choice.lower():
            typewriter_simulator("Correct!\nThe answer is : "
                                 + quiz_lists.answers[level][quiz] + "\n")
            score += 1
        else:
            typewriter_simulator("Wrong!\nThe answer is : "
                                 + quiz_lists.answers[level][quiz] + "\n")

    if score >= 7:
        win(score)
    else:
        lose(score)


def win(score):
    print_pause("\n")
    typewriter_simulator("You got it!\n"
                         f"Your final score is {score}.\n")

    play_again()


def lose(score):
    print_pause("\n")
    typewriter_simulator("Lose!\n"
                         f"Your final score is {score}.\n")

    play_again()


def play_again():
    choice = valid_input(u'♠'" Play again? [y|n]", ['y', 'n'])
    # The game should start over from the beginning
    # with the original setting.
    if choice == 'y':
        typewriter_simulator("\nWait.......\n")
        game()
    elif choice == 'n':
        typewriter_simulator("\nThanks for playing! Good bye!\n")
        exit(0)
    else:
        play_again()


def game():
    level = 0
    score = 0
    choices(score, level)
    play_game(score, level)


if __name__ == '__main__':
    intro()
    game()
    play_again()
