import random

def load_words_from_file(filename):
    with open(filename, 'r') as file:
        words = file.readlines()
        words = [word.strip() for word in words]
    return words

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + ' '
        else:
            displayed_word += '_ '
    return displayed_word

def choose_random_word(words):
    return random.choice(words)

def display_game_info(word, guessed_letters, lives):
    print("\nWord:", display_word(word, guessed_letters))
    print("Remaining Lives:", lives)
    print("Guessed Letters:", ' '.join(guessed_letters))
    print("\n  ____")
    print(" |    |")
    print(" |    " + ("O" if lives < 6 else ""))
    print(" |   " + ("/|\\" if lives < 5 else "") + ("|" if lives < 4 else ""))
    print(" |   " + ("/ \\" if lives < 3 else ""))
    print("_|_")

def process_guess(guess, guessed_letters, word, lives, score):
    if guess in guessed_letters:
        print("You already guessed that letter.")
    else:
        guessed_letters.append(guess)
        if guess not in word:
            print("Incorrect guess.")
            lives -= 1
            score -= 1
        else:
            print("Correct guess!")
    return lives, score

def check_game_status(word, guessed_letters):
    if all(letter in guessed_letters for letter in word):
        return True
    return False

def save_player_score(player_name, score):
    with open('resourses/task2_resourse_files/scores.txt', 'a') as file:
        file.write(f"{player_name};{score}\n")

def end_game_message(word, score):
    if score == 100:
        print("\nCongratulations! You guessed the word:", word)
    else:
        print("\nGame over! The word was:", word)
    print("Your final score:", score)

def play_hangman(word, lives):
    guessed_letters = []
    initial_score = 100

    print("\nWelcome to Hangman!")
    print("Try to guess the word.")

    while lives > 0:
        display_game_info(word, guessed_letters, lives)
        guess = input("\nEnter a letter: ").lower()
        lives, _ = process_guess(guess, guessed_letters, word, lives, 0)
        if check_game_status(word, guessed_letters):
            end_game_message(word, initial_score)
            break
        lives -= 1

    else:
        final_score = initial_score - (5 - lives)
        end_game_message(word, final_score)

    return final_score

def main():
    words_list = load_words_from_file('resourses/task2_resourse_files/words.txt')
    player_name = input("Enter your name: ")
    chosen_word = choose_random_word(words_list)
    lives_left = 6
    player_score = play_hangman(chosen_word, lives_left)
    save_player_score(player_name, player_score)

if __name__ == "__main__":
    main()
