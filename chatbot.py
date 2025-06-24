def get_bot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your gender":
        return "I am genderless, I'm just a bot!"
    elif user_input == "how old are you":
        return "I was created recently, but I know a lot!"
    elif user_input == "where are you from":
        return "I'm from the digital world!"
    elif user_input == "who created you":
        return "I was created by a developer using Python!"
    else:
        return "Sorry, I didn't understand that."


def start_chat():
    print("ChatBot: Hello! Type something (type 'bye' to exit)")

    while True:
        user_input = input("You: ")
        response = get_bot_response(user_input)
        print("ChatBot:", response)

        if user_input.lower().strip() == "bye":
            break


start_chat()
