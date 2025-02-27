import time
import webbrowser
import subprocess

def show_commands():
    print("\nI can perform the following tasks:")
    print("1. Open Notepad - Type: 'open notepad'")
    print("2. Tell the current time - Type: 'tell me the time'")
    print("3. Search on Google - Type: 'search on google'")
    print("4. Open YouTube - Type: 'open youtube'")
    print("5. Open WhatsApp - Type: 'open whatsapp'")  # ✅ Added WhatsApp option
    print("6. Exit the assistant - Type: 'exit'\n")

def execute_command(command):
    command = command.lower()  # Convert input to lowercase for consistency

    if "open notepad" in command:
        print("Opening Notepad...")
        subprocess.run(["notepad"])

    elif "tell me the time" in command:
        print("Current time:", time.strftime("%I:%M:%S %p"))
        print("Date:", time.strftime("%A, %d %B %Y"))

    elif "search on google" in command:
        query = input("What do you want to search for? ")
        webbrowser.open(f"https://www.google.com/search?q={query}")
        print(f"Searching Google for: {query}")

    elif "open youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in command:  # ✅ Added condition for WhatsApp
        print("Opening WhatsApp...")
        webbrowser.open("https://web.whatsapp.com")  # Opens WhatsApp Web

    else:
        print("Sorry, I don't understand that command.")

print("Welcome to your Virtual Assistant!")
show_commands()

while True:
    user_input = input("Enter a command: ")
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    execute_command(user_input)
