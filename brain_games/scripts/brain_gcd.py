from brain_games.cli import ask_quiz_questions
from brain_games.games.gcd import ask_brain_gcd_question


def main():
    ask_quiz_questions(
        ask_brain_gcd_question,
        'Find the greatest common divisor of given numbers.'
    )


if __name__ == '__main__':
    main()
