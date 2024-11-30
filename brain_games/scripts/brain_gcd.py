from random import randint
from brain_games.cli import welcome_user
import prompt


def main():
    brain_gcd()


if __name__ == '__main__':
    main()


def brain_gcd(questions_to_ask=3):
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for _ in range(questions_to_ask):
        user_was_correct: bool = ask_user_question(name)
        if not user_was_correct:
            break
    if user_was_correct:
        print(f'Congratulations, {name}!')


def ask_user_question(name):
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
