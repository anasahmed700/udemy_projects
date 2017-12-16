known_users = ['Anas', 'Asad', 'Ali']

while True:
    print('\nHi! my name is Travis')
    name = input('what is your name?: ').strip().capitalize()

    if name in known_users:
        print('Hello {}!'.format(name))
        remove = input('would you like to be removed from the system (y/n)?: ').lower().strip()
        if remove == 'y':
            known_users.remove(name)
        elif remove == 'n':
            print("No problem, i didn't want you to leave anyway!")
    else:
        print("Hmmm i don't think i have met you yet {}".format(name))
        add_me = input('would you like to be added to the system (y/n)?: ').lower().strip()
        if add_me == 'y':
            known_users.append(name)
        elif add_me == 'n':
            print('No worries, see you around!')
    print(known_users)