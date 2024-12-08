from random import randint
import prompt


def ask_brain_gcd_question(name):
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    correct_answer = str(gcd(num1, num2))

    print(f'Question: {num1} {num2}')

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


def gcd(num1, num2):
    a = max(num1, num2)
    b = min(num1, num2)

    remainder = a % b
    while remainder > 0:
        a = b
        b = remainder
        remainder = a % b
    return b
