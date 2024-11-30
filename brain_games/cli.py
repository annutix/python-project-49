import prompt


def welcome_user():
    print('Welcome to the brain games!')
    name = prompt.string('May I have your name? ')
    print(f'Welcome, {name}!')
    return name
