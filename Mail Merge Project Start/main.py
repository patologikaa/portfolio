


with open ('./Input/Names/invited_names.txt', 'r') as name_file:
    names = name_file.readlines()


with open ('./Input/Letters/starting_letter.txt', 'r') as letter_file:
    mail = letter_file.read()
    for name in names:
        stripped = name.strip()
        new_mail = mail.replace('[name]', stripped)
        with open(f'./Output/ReadyToSend/{stripped}.txt', mode='w') as output:
            output.write(new_mail)
