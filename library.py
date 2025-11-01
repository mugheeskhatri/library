import pyttsx3
import time

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

books = ["English Grammar", "Mathematics", "Rich Dad Poor Dad", "Physics"]

while True:
    print("\nWelcome to the Neurasphere Library")
    speak("Welcome to the Neurasphere Library")

    print("1. Show all books")
    print("2. Add a book")
    print("3. Remove a book")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print("\nAvailable Books:")
        speak("Here are the available books")
        for book in books:
            print(f"- {book}")
            engine.say(book)
            engine.runAndWait() 
            time.sleep(1.5)  

    elif choice == "2":
        new_book = input("Enter book name to add: ").strip()
        if new_book in books:
            print("This book is already added!")
            speak("This book is already added")
        else:
            books.append(new_book)
            print(f"'{new_book}' has been added successfully!")
            speak(f"{new_book} has been added successfully")

    elif choice == "3":
        remove_book = input("Enter book name to remove: ").strip()
        if remove_book in books:
            books.remove(remove_book)
            print(f"'{remove_book}' has been removed from the library!")
            speak(f"{remove_book} has been removed from the library")
        else:
            print("Book not found in the library!")
            speak("Book not found in the library")

    elif choice == "4":
        print("Exiting Library System. Goodbye!")
        speak("Exiting Library System. Goodbye")
        break

    else:
        print("Invalid choice! Please enter a number from 1 to 4.")
        speak("Invalid choice! Please enter a number from one to four")
