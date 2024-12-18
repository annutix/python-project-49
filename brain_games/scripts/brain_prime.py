from brain_games.cli import ask_quiz_questions
from brain_games.games.prime import ask_brain_prime_question


def main():
    ask_quiz_questions(
        ask_brain_prime_question,
        'Answer "yes" if given number is prime. Otherwise answer "no".'
    )


if __name__ == '__main__':
    main()
