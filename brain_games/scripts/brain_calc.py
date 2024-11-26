from random import randint, choice
import operator
from brain_games.cli import welcome_user
import prompt


def main():
    print('Welcome to the Brain Games!')
    brain_calc()


if __name__ == '__main__':
    main()


def brain_calc(questions_to_ask=3):
    name = welcome_user()
    print('What is the result of the expression?')
    for _ in range(questions_to_ask):
        user_was_correct: bool = ask_user_question(name)
        if not user_was_correct:
            break
    if user_was_correct:
        print(f'Congratulations, {name}!')


operators_dict = {'*': operator.mul, '-': operator.sub, '+': operator.add}


def ask_user_question(name):
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    operator_str = choice(list(operators_dict.keys()))
    f = operators_dict[operator_str]
    correct_answer = str(f(num1, num2))

    print(f'Question: {str(num1)} {operator_str} {str(num2)}')

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
