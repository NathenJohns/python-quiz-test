def show_menu():
    print("1. Ask Questions")
    print("2. Add a question")
    print("3. Exit Game")
    
    option = input("Enter option: ")
    return option

def ask_questions():
    questions = []
    answers = []
    
    with open("questions.txt", "r") as file:
        lines = file.read().splitlines()
    
    for i, text in enumerate(lines):
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)
    
    for question, answer in zip(questions, answers):
        guess = input(question + "> ")

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            print(ask_questions())
        elif option == "2":
            print("You selected 'Add a question'")
        elif option == "3":
            break
        else:
            print("Invalid Option")
        print("")
        
game_loop()