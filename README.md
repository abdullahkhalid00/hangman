# CLI Hangman

## Description

This project is written in python and consists of a simple game of hangman. The script generates a random word from the .txt file and the user has to guess that word letter by letter. 

This project is coded in accordance with the procedural paradigm of python meaning each task is converted into a function that returns a certain desired output.

## Rules

I have devised a certain set of rules to play the game which are as follows:

* The user gets a total of `7` guesses.
* There are two modes of playing this game (i.e. `easy mode` and `hard mode`).
* If the user is able to guess a word that occurs twice in the word, that letter is replaced twice.
* In `easy` mode, the user gets a maxiumum of `3` extra misses per word.
* If the user chooses to play in `easy` hard, the script will generate words having a letter count no greater than `4`.
* In `hard` mode, the user gets a maxiumum of `1` extra miss per word.
* If the user chooses to play in `hard` mode, the script will generate words having a letter count between `4` and `6`.
* The game finishes if the user has guessed all the letters correctly or has run out of guesses.
* The user can only enter one letter per guess.
* The `words.txt` only consists of alphabetical words, thus the user must enter an alphabet as a guess.

## Usage

In order to play this game first you would have to clone the repository using a simple command like this:

```
git clone {url-link}
```
Instead of `{url-link}` you would have to paste the link of the repository.

Alternatively, you can download the contents of the repository as a `.zip` file and extract it to your desired folder.

After that, open up a terminal and navigate to the directory in which you have cloned the repo.

Run this command to navigate inside the src folder.
```
cd src
```
After you are inside the src folder run:
```
py __main__.py {difficulty}
```
Replace `{difficulty}` with the difficulty level you wish to play at (i.e. `easy` or `hard`)

If you do not enter the difficulty level, you will be prompted to do so later on in the game.

## Acknowledgements

The contents of the `words.txt` file has been retrieved from [Capitalize My Title](https://capitalizemytitle.com/random-word-generator/#). 