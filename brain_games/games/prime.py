from random import randint
import prompt


def ask_brain_prime_question(name):
    number = randint(-100, 100)
    if number <= 1:
        correct_answer = 'no'
    else:
        for n in range(2, number):
            if number % n == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
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
