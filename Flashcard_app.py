import random

class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class FlashcardApp:
    def __init__(self):
        self.flashcards = []
        self.score = 0
        self.total_questions = 0

    def add_flashcard(self):
        question = input("Enter the question: ")
        answer = input("Enter the answer: ")
        flashcard = Flashcard(question, answer)
        self.flashcards.append(flashcard)
        print("Flashcard added successfully!\n")

    def take_quiz(self):
        if not self.flashcards:
            print("No flashcards available. Add some flashcards first.\n")
            return

        random.shuffle(self.flashcards)
        self.score = 0
        self.total_questions = len(self.flashcards)

        for flashcard in self.flashcards:
            print(f"Question: {flashcard.question}")
            user_answer = input("Your answer: ")

            if user_answer.lower() == flashcard.answer.lower():
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is: {flashcard.answer}\n")

        self.display_score()

    def display_score(self):
        print(f"Quiz complete! You got {self.score}/{self.total_questions} correct.\n")

    def menu(self):
        while True:
            print("Flashcard Quiz App")
            print("1. Add a flashcard")
            print("2. Take a quiz")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_flashcard()
            elif choice == '2':
                self.take_quiz()
            elif choice == '3':
                print("Exiting the app.")
                break
            else:
                print("Invalid choice. Please try again.\n")

# Running the app
if __name__ == "__main__":
    app = FlashcardApp()
    app.menu()
