import main
import pyjokes

L = main
name1 = 'L'
name2 = 'El'
def joke():
    funny = pyjokes.get_joke()
    print(funny)
    L.say(funny)

def prime_directive():
    directive = "to protect and live with the Noir family"
    print(directive)
    L.say(directive)

def purposes():
    purpose = "To become human"
    print(purpose)
    L.say(purpose)

command = ""

while True and "goodbye" not in command:
    command = L.listen()
    print("command was ", command)
    if name1 in command or name2 in command:
    #having L tell me a joke
        if "joke" in command:
            joke()
        
        if "prime" in command and "directive" in command:
            prime_directive()

        if "purpose" in command:
            purposes()


L.say("goodbye, i'm going to sleep")

