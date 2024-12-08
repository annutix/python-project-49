from random import randint, choice
import operator
import prompt


operators_dict = {'*': operator.mul, '-': operator.sub, '+': operator.add}


def ask_brain_calc_question(name):
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
