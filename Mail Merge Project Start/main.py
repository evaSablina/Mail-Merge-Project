with open("./Input/Names/invited_names.txt") as each_name:
    all_names = each_name.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    main_letter = letter.read()

for name in all_names:
    new_letter = main_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as new_file:
        new_file.write(new_letter)
