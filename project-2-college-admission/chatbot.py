import aiml
import requests

# Create a Kernel object
kernel = aiml.Kernel()

# Load the AIML files
kernel.learn("chatbot.aiml")

# Function to get the chatbot's response
def get_response(user_input):
    return kernel.respond(user_input)

# Main loop for user interaction
print("Welcome to the College Admission Q&A Bot!")
print("How can I assist you with your admission queries?")

while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("Chatbot:", response)

    if response.lower() == "goodbye":
        break

# Function to get admission information from the backend API
def get_admission_info():
    url = 'http://localhost:8000/admission-info/'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to get the chatbot's response
def get_response(user_input):
    if 'admission requirements' in user_input.lower():
        admission_info = get_admission_info()
        if admission_info:
            requirements = admission_info['requirements']
            return f"The admission requirements are: {requirements}"
        else:
            return "Sorry, I couldn't fetch the admission requirements at the moment."
    else:
        return kernel.respond(user_input)