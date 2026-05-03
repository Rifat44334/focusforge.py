import time

print("🔥 Welcome to FocusForge")

name = input("Enter your name: ")
print(f"Hello {name}, let's focus!\n")

sessions = []

while True:
    print("\n1. Start Study Session")
    print("2. View History")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        duration = int(input("Enter study time (seconds): "))
        print("Session started... Stay focused!")

        time.sleep(duration)

        mood = input("How do you feel? (happy/neutral/sad): ")

        if mood == "happy":
            suggestion = "Great! Keep going 🚀"
        elif mood == "neutral":
            suggestion = "Maybe take a short break 🙂"
        else:
            suggestion = "Rest a bit 😴"

        sessions.append((duration, mood))

        print("Session complete!")
        print("Suggestion:", suggestion)

    elif choice == "2":
        print("\n📊 Session History:")
        for s in sessions:
            print(f"Time: {s[0]} sec | Mood: {s[1]}")

    elif choice == "3":
        print("Goodbye 👋")
        break

    else:
        print("Invalid choice")
