# Function to generate chatbot response
def get_response(user_input):

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"

    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks!"

    elif user_input in ["your name", "what is your name"]:
        return "I'm a simple chatbot created using Python."

    elif user_input in ["thanks", "thank you"]:
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand that."


# Main chatbot function
def chatbot():

    print("Chatbot: Hello! I am your assistant 🤖")
    print("Type 'bye' to exit.\n")

    while True:  # Loop
        user_input = input("You: ").lower()  # Input

        response = get_response(user_input)  # Function call
        print("Chatbot:", response)  # Output

        if user_input == "bye":  # Exit condition
            break


# Run chatbot
chatbot()
