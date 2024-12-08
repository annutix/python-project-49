from brain_games.cli import ask_quiz_questions
from brain_games.games.calc import ask_brain_calc_question


def main():
    ask_quiz_questions(
        ask_brain_calc_question,
        'What is the result of the expression?'
    )


if __name__ == '__main__':
    main()
