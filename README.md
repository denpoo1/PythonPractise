![Logo](https://i.gifer.com/YQgT.gif)

# Repository Overview

This repository contains a collection of Python scripts for various tasks including data visualization, image processing, data anonymization, a Hangman game, and directory traversal for numerical computation.

## Table of Contents

- [Movie Gross Analysis](##movie-gross-analysis)
- [Meme Creator](##meme-creator)
- [Data Anonymization](##data-anonymization)
- [Hangman Game](##hangman-game)
- [Directory Traversal for Numerical Computation](##directory-traversal-for-numerical-computation)

## Movie Gross Analysis

This script analyzes the gross revenue of movies by genre based on the IMDb Top 1000 movies dataset.

### Features:
- Reads movie data from a CSV file.
- Cleans and converts the 'Gross' column to numerical values.
- Calculates the average gross revenue by genre.
- Plots bar charts of the average gross by genre and highlights genres with high average gross.

### Usage:
```python
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('movies/imdb_top_1000.csv')
data['Gross'] = data['Gross'].str.replace(',', '').astype(float)

average_gross = data.groupby('Genre')['Gross'].mean()

plt.figure(figsize=(14, 6))
average_gross.plot(kind='bar', color='skyblue')
plt.title('Average Movie Gross by Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Average Gross in $')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

high_gross_genres = average_gross[average_gross > data['Gross'].quantile(0.75)]

plt.figure(figsize=(12, 6))
high_gross_genres.plot(kind='bar', color='skyblue')
plt.title('Average Movie Gross by Genre')
plt.xlabel('Movie Genre')
plt.ylabel('Average Gross in $')
plt.xticks(rotation=45, fontsize=8, ha='right')
plt.ticklabel_format(axis='y', style='plain')
plt.ylim(min(high_gross_genres) * 0.9, max(high_gross_genres) * 1.1)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
```

## Meme Creator

This script allows users to create memes by adding text to images.

### Features:
- Reads an image from a specified path.
- Adds a border at the bottom of the image.
- Adds user-specified text to the image.
- Displays the created meme.

```python
import cv2

def create_meme(path_to_image, meme_text):
    original_image = cv2.imread(path_to_image)

    img_height, img_width = original_image.shape[:2]
    img_with_border = cv2.copyMakeBorder(original_image, 0, 100, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    font_style = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img_with_border, meme_text, (10, img_height + 50), font_style, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow("Meme", img_with_border)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    user_input = input("Podaj numer obrazka (np. 1, 2,
```

## Data Anonymization

This script anonymizes email addresses in a CSV file by replacing the local part of the email addresses with random characters.

### Features:

- Reads data from a CSV file.
- Replaces the local part of email addresses with random strings.
- Writes the anonymized data to a new CSV file.

```python
import csv
import random
import string

def hide_email(email):
    local_part, domain = email.split('@')
    random_local_part = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 20)))
    return f"{random_local_part}@{domain}"

def process_row(row):
    anonymized_row = []
    for item in row:
        if '@' in item:
            anonymized_item = hide_email(item)
        else:
            anonymized_item = item
        anonymized_row.append(anonymized_item)
    return anonymized_row

def hide_data(input_file, output_file):
    with open(input_file, 'r') as input_csv:
        with open(output_file, 'w', newline='') as output_csv:
            csv_reader = csv.reader(input_csv, delimiter=';')
            csv_writer = csv.writer(output_csv, delimiter=';')
            for row in csv_reader:
                anonymized_row = process_row(row)
                csv_writer.writerow(anonymized_row)

# Example usage
input_file = 'resourses/task3_resourse_files/departament.csv'
output_file = 'resourses/task3_resourse_files/departament_hidden.csv'
hide_data(input_file, output_file)
```

## Hangman Game

This script implements a text-based Hangman game.

### Features:

- Loads a list of words from a file.
- Chooses a random word for the player to guess.
- Displays the word with guessed letters and underscores for missing letters.
- Manages the game state and checks for correct and incorrect guesses.
- Displays a hangman figure based on remaining lives.
- Saves the player's score to a file.

```python
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
```

## Directory Traversal for Numerical Computation

This script traverses a directory and its subdirectories to compute the sum and count of all integer numbers found in text files.

### Features:

- Traverses a directory recursively.
- Reads text files and extracts integer numbers.
- Computes the sum and count of all numbers found.
- Handles both files and subdirectories.

```python
import os

def compute_sum_and_count(input_dir):
    total_sum = 0
    total_count = 0

    for item in os.listdir(input_dir):
        item_path = os.path.join(input_dir, item)

        if os.path.isfile(item_path) and item.endswith('.txt'):
            with open(item_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    for word in line.split():
                        try:
                            number = int(word)
                            total_sum += number
                            total_count += 1
                        except ValueError:
                            pass

        elif os.path.isdir(item_path):
            subdirectory_sum, subdirectory_count = compute_sum_and_count(item_path)
            total_sum += subdirectory_sum
            total_count += subdirectory_count

    return total_sum, total_count

def get_directory_path():
    directory_path = input("Enter the directory path: ")
    return directory_path

def main():
    directory_path = get_directory_path()

    if not os.path.exists(directory_path):
        print("The specified path does not exist.")
        return

    total_sum, total_count = compute_sum_and_count(directory_path)
    print("Total sum of numbers:", total_sum)
    print("Total count of numbers:", total_count)

if __name__ == "__main__":
    main()
```
