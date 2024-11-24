import random

# Define a list of questions, each with choices and correct answer
questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic", "Pacific", "Indian", "Arctic"],
        "answer": "Pacific"
    },
    {
        "question": "Who developed the theory of relativity?",
        "choices": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"],
        "answer": "Albert Einstein"
    },
    {
        "question": "What is the square root of 64?",
        "choices": ["6", "7", "8", "9"],
        "answer": "8"
    }
]

# Function to display the question and check the answer
def ask_question(question, choices, correct_answer):
    print(f"\n{question}")
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    try:
        user_answer = int(input("\nChoose an option (1-4): "))
        if choices[user_answer - 1] == correct_answer:
            print("Correct!")
            return True
        else:
            print("Incorrect. The correct answer was:", correct_answer)
            return False
    except (ValueError, IndexError):
        print("Invalid input. Please choose a number between 1 and 4.")
        return False

# Function to run the quiz
def run_quiz():
    score = 0
    random.shuffle(questions)  # Shuffle questions to make it different every time

    # Loop through each question
    for question in questions:
        is_correct = ask_question(question["question"], question["choices"], question["answer"])
        if is_correct:
            score += 1

    # Display the score
    print(f"\nYour total score is: {score}/{len(questions)}")

# Main function to start the quiz
def main():
    print("Welcome to the Quiz Test Application!")
    print("Please answer the following questions:\n")

    run_quiz()

    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")

# Run the quiz
if __name__ == "__main__":
    main()
