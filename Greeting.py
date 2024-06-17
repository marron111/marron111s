import random
import time

def get_word():
    words = ['python', 'java', 'ruby', 'javascript', 'swift', 'kotlin', 'php', 'html', 'css']
    return random.choice(words)

def game():
    print("Welcome to Continuous Typing Game!")
    print("You will be shown a word. Type it as fast as you can.")
    input("Press Enter to start...")

    while True:
        word = get_word()
        print("Your word is:")
        print(word)
        
        start_time = time.time()
        user_input = input("Type the word: ").strip()
        end_time = time.time()

        if user_input == word:
            print("Congratulations! You typed the word correctly.")
            print(f"Time taken: {end_time - start_time:.2f} seconds")
        else:
            print(f"Oops! You made a mistake. The correct word was '{word}'.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

if __name__ == "__main__":
    game()

print("Thank you for playing Continuous Typing Game!")
