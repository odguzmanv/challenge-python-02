# Resolve the problem!!
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
     caracteres = str(SYMBOLS) + string.ascii_letters + string.digits
    longitud = random.randint(8,16)
    minusculas = random.randint(1,4);
    mayusculas = random.randint(1,4);
    numeros = random.randint(1,4);
    simbolos = random.randint(1,4);

   

    while True:
        password = ("").join(random.choice(caracteres) for index in range(longitud))
        if(sum(caracter.islower() for caracter in password) >= minusculas
            and sum(caracter.isupper() for caracter in password) >= mayusculas
            and sum(caracter.isdigit() for caracter in password) >= numeros):
            for caracter in password:
                    if caracter in SYMBOLS:
                        False
                    else:
                        True
            break
    return password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
