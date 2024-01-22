# Generator Password using Python
# Joao Pedro Costa
import string
import random

numbers = string.digits
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
special_digits = ['?', '&', '$', '#', '£', '§', '%', '€', '!', '/']


def generate_password(password):
    char_list = ''
    password_gen = ''

    if not (password[1] == 's' or password[2] == 's' or password[3] == 's' or password[4] == 's' or
            password[1] == 'S' or password[2] == 'S' or password[3] == 'S' or password[4] == 'S'):
        print("Erro: Pelo menos uma opção de caracteres deve ser selecionada.")
        return

    print("\nThe pasword will have {} characters.".format(password[0]))

    # Here a random number is created, with this number we access the array and add the respective character to the
    # string
    while len(char_list) < password[0]:
        if (password[1] == 's' or password[1] == 'S') and len(char_list) < password[0]:
            rand = random.randint(0, 23)
            char_list = char_list + lowercase_letters[rand]

        if (password[2] == 's' or password[2] == 'S') and len(char_list) < password[0]:
            rand = random.randint(0, 23)
            char_list = char_list + uppercase_letters[rand]

        if (password[3] == 's' or password[3] == 'S') and len(char_list) < password[0]:
            rand = random.randint(0, 9)
            char_list = char_list + numbers[rand]

        if (password[4] == 's' or password[4] == 'S') and len(char_list) < password[0]:
            rand = random.randint(0, 9)
            char_list = char_list + special_digits[rand]

    # Here takes randomly a character from char_list, to don't let the password with a sequence
    for i in range(len(char_list)):
        password_gen = ''.join(random.sample(char_list, len(char_list)))
    print("\nThis is your password: {}\n".format(password_gen))


def user_interface():
    tam = -1
    while True:
        while True:
            # Don't let the user introduce a string or char on password tam
            # And give a user a password limit
            try:
                tam = int(input("How many characters do you want in password - (0 to 50): "))
                if tam < 0 or tam > 50:
                    continue
            except ValueError:
                continue
            else:
                break

        choice_lowercase = input("Do you want lowercase letters in your password (s/n): ")
        choice_uppercase = input("Do you want uppercase letters in your password (s/n): ")
        choice_numbers = input("Do you want numbers in your password (s/n): ")
        choice_special_digits = input("Do you want special digits in your password (s/n): ")

        # Store the type of characters that users want and the password length
        password = [tam, choice_lowercase, choice_uppercase, choice_numbers, choice_special_digits]

        generate_password(password)
        retry = input("Do you want create another password - (s/n): ")
        if retry == "s" or retry == 'S':
            continue
        else:
            break


user_interface()
