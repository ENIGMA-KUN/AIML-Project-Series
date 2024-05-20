import aiml

# Create a Kernel object
kernel = aiml.Kernel()

# Load the AIML file
kernel.learn("chatbot.aiml")

# Function to get the chatbot's response
def get_response(user_input):
    return kernel.respond(user_input)

# Main loop for user interaction
while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("Chatbot:", response)