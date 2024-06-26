#chatbot
qaPairs = {
    "hello": "hi",
    "how are you": "fine",
    "bye": "bye bye"
}

def getResponse(userInput):
    for question, answer in qaPairs.items():
        if question == userInput:
            return answer
    return "Please try later"

while True:
    userInput = input("You: ").lower()
    response = getResponse(userInput)
    print(f"Chatter: {response}")
    if userInput == 'bye':
        break