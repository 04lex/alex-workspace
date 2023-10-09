import nltk
import random
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the AI assistant
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you|how\'s it going', ['I\'m just a computer program, but I\'m here to help!', 'I\'m doing well, thank you!']),
    (r'bye|goodbye', ['Goodbye!', 'Take care!', 'Have a great day!']),
    (r'(.*)', ['I\'m sorry, I don\'t quite understand. Could you rephrase that?', 'Please tell me more.'])
]

# Create a Chat instance with the patterns and responses
chatbot = Chat(patterns, reflections)

# Main loop for interacting with the AI assistant
print("AI Assistant: Hi! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("AI Assistant: Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("AI Assistant:", response)
