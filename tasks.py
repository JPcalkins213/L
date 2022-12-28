import main
import pyjokes

L = main
name = 'El'
def joke():
    funny = pyjokes.get_joke()
    print(funny)
    L.say(funny)

command = ""

while True and "goodbye" not in command:
    command = L.listen()
    print("command was ", command)
    if name in command:
    #having L tell me a joke
        if "joke" in command:
            joke()
    


L.say("goodbye, i'm going to sleep")

