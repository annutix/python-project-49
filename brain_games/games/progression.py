from random import randint
import prompt


def ask_brain_progression_question(name):
    initial_number = randint(0, 50)
    step = randint(1, 10)
    progression = ''
    missed_number = randint(0, 9)

    for i in range(10):
        num = initial_number + i * step
        if i == missed_number:
            correct_answer = str(num)
            progression += '.. '
        else:
            progression += str(num) + ' '

    print('Question: ' + str(progression))
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
