def run_quiz(questions):
    score = 0
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{answer}'.\n")
    return score

if __name__ == "__main__":
    quiz_questions = {
        "What is the capital of France?": "Paris",
        "What is 7 + 3?": "10",
        "Which planet is known as the 'Red Planet'?": "Mars",
        "What is the chemical symbol for water?": "H2O",
        "Who painted the Mona Lisa?": "Leonardo da Vinci"
    }

    print("Welcome to the Quiz!")
    print("You will be asked some questions. Provide your answers to test your knowledge.\n")

    total_score = run_quiz(quiz_questions)

    print(f"Quiz completed!\nYour total score is: {total_score} out of {len(quiz_questions)}")
