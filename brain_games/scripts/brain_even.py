from random import randint
from brain_games.cli import welcome_user
import prompt


def main():
    brain_even()


if __name__ == '__main__':
    main()


def brain_even(questions_to_ask=3):
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for question_num in range(questions_to_ask):
        user_was_correct: bool = ask_user_question(name)
        if not user_was_correct:
            break
    if question_num == questions_to_ask - 1:
        print(f'Congratulations, {name}!')


def ask_user_question(name):
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
