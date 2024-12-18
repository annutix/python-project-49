from brain_games.cli import ask_quiz_questions
from brain_games.games.progression import ask_brain_progression_question


def main():
    ask_quiz_questions(
        ask_brain_progression_question,
        'What number is missing in the progression?'
    )


if __name__ == '__main__':
    main()
