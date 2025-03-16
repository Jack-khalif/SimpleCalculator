import random

# List of programming jokes
jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs! 🐞",
    "Why did the Python programmer break up with Java? Because he didn’t like the class structure! 😆",
    "How do you comfort a JavaScript bug? You console it. 😜",
    "Why do Python programmers prefer snakes? Because they don’t have to declare variables! 🐍",
    "Why was the function feeling sad? Because it lost its scope! 📏"
]

def tell_joke():
    """Function to display a random programming joke."""
    print("\n🤣 Here's a joke for you:")
    print(random.choice(jokes))

# Display a joke every time the program runs
tell_joke()
