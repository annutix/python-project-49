from brain_games.cli import ask_quiz_questions
from brain_games.games.even import ask_brain_even_question


def main():
    ask_quiz_questions(
        ask_brain_even_question,
        'Answer "yes" if the number is even, otherwise answer "no".'
    )


if __name__ == '__main__':
    main()
