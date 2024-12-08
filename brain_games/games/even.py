from random import randint
import prompt


def ask_brain_even_question(name):
    number = randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    print('Question: ' + str(number))
    user_answer = prompt.string('Your answer: ')
    result = user_answer == correct_answer
    if result:
        print('Correct!')
    else:
        print(
            f"'{user_answer}' is wrong answer ;(. "
            + f"Correct answer was '{correct_answer}'.\n"
            + f"Let's try again, {name}!")
    return result
