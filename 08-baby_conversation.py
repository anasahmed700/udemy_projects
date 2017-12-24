from random import choice
questions = ["why is the sky blue?",
             "why is there a face on the moon?",
             "where are all the dinosaurs?"]
answer = input(choice(questions)).lower().strip()

while answer != "just because":
    answer = input("why?: ").strip().lower()
print("Oh... Okay!")