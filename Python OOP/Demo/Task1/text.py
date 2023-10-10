from validations import validate_text


def enter_text():
    print('-' * 30)
    print('Enter your text (must be between 3 and 16 chars):')
    text = input()

    validate_text(text)

    print(f'Your text length is: {len(text)}')
