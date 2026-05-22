print("Hi there I am Anibot your friend and chat partner!")
name = input("What can I call you my friend? ")

print("hi", name,"nice to meet you 👍")
print("Anibot: ",name,"what can i help you with today?")

while True:
    response = input("").lower().strip()
    if response == "hello" or response == "hi" or response == "hey":
        print("Anibot: hi", name,"nice to meet you 😍")
    elif response == "how are you?" or response == "how are you" or response == "how are you doing?" or response == "how are you doing" or response == "how far":
        print("Anibot: I'm fine thanks for asking.")
    elif response == "what is your name":
        print("Anibot: My name is Anibot, your AI friend 🤖")

   
    elif response == "python":
        print("Anibot: Python is a very beginner-friendly programming language!")

    # asking about AI
    elif response == "what is ai":
        print("Anibot: AI means Artificial Intelligence.")
        print("Anibot: It helps computers think and make decisions like humans.")

    # nested condition example
    elif "weather" in response:

        city = input("Anibot: Which city are you in? ").lower()

        if city == "aba":
            print("Anibot: Aba is usually warm today ☀️")

        elif city == "lagos":
            print("Anibott: Lagos weather can be hot and humid 🌤️")

        else:
            print("Anibot: Sorry, I don't know the weather for that city yet.")

    # hobbies
    elif "music" in response:
        print("Anibot: I enjoy all kinds of music 🎵")
        print("Anibot: What type of music do you like?")
        muRe = input("").lower().strip()
        if "afro beat" in muRe or "hip pop" in muRe or "blues" in muRe or "rnb" in muRe:
            print(f"I like {muRe} as well.")
        else:
            print(f"Anibot: I don't know about {muRe} yet")

    elif "football" in response:
        print("Anibot: Football is exciting ⚽")
        print("Anibot: My favorite part is the last-minute goals!")

    # jokes
    elif "joke" in response:
        print("Anibot: Why did the computer go to school?")
        print("Anibot: Because it wanted to improve its memory 😂")

    # motivation
    elif "motivate me" in response:
        print("Anibot: Never stop learning.")
        print("Anibot: Every expert was once a beginner 💪")

    # exit command
    elif "bye" in response or "exit" in response:
        print(f"Goodbye {name}! Have a wonderful day 👋")
        break

    # unknown responses
    else:
        print("Anibot: Hmm... I don't understand that yet 🤔")
        print("Anibot: Try asking me about AI, music, football, weather, or jokes.")