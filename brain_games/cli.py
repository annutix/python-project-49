import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome, {name}!')
    return name


def ask_quiz_questions(ask_user_question, task, questions_to_ask=3):
    name = welcome_user()
    print(task)
    for _ in range(questions_to_ask):
        user_was_correct: bool = ask_user_question(name)
        if not user_was_correct:
            break
    if user_was_correct:
        print(f'Congratulations, {name}!')
