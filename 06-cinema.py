films = {"Finding Dory": [3,5],
         "Bourne": [18,5],
         "Tarzan": [15,5],
         "Ghost Busters": [12,5]
         }

while True:
    choice = input("what film would you like to watch?: ").strip().title()

    if choice in films:
        age = int(input("how old are you?: ").strip())
        # check user age
        if age >= films[choice][0]:
            # check enough seats
            if films[choice][1] > 0:
                print("enjoy the film!")
                films[choice][1] = films[choice][1]-1
            else:
                print("sorry their is not enough tickets!")
        else:
            print("you are too young to see that film!")
    else:
        print("we don't have that movie...")
