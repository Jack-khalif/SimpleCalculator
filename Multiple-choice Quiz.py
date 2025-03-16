#import random

# List of quiz questions
quiz_questions = [
    {
        "question": "What does the 'print' function do in Python?",
        "options": ["A. Prints documents", "B. Displays output", "C. Saves a file", "D. Deletes files"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "Who directed the movie 'Inception'?",
        "options": ["A. Steven Spielberg", "B. Christopher Nolan", "C. James Cameron", "D. Quentin Tarantino"],
        "answer": "B"
    },
    {
        "question": "Which of these is NOT a Python data type?",
        "options": ["A. List", "B. String", "C. Tuple", "D. Array"],
        "answer": "D"
    }
]

def play_quiz():
    """Function to play the multiple-choice quiz."""
    score = 0
    print("\n🎯 Welcome to the Fun Quiz! 🎯")
    
    for q in quiz_questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("\nYour answer (A, B, C, or D): ").strip().upper()
        
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.")

    print(f"\n🏆 Your final score: {score}/{len(quiz_questions)} 🏆")

    # Ask if the user wants to play again
    again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if again == "yes":
        play_quiz()

# Start the quiz
play_quiz()
