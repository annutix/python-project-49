import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Welcome, {name}!')
    return name
