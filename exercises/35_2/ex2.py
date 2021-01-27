# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa
# usuária tenha que adivinhar uma palavra que será mostrada com as letras
# embaralhadas. O programa terá uma lista de palavras e escolherá uma
# aleatoriamente. O jogador terá três tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se a pessoa ganhou
# ou perdeu o jogo.
# Para embaralhar uma palavra faça:
# scrambled_word = "".join(random.sample(word, len(word)))
# O sorteio de uma palavra aleatória pode ser feito utilizando o método:
# random.choice(["word1", "word2", "word3"]) -> "word2".

import random

words = ["creative", "random", "word"]


def scrambled_word_game(words):
    drawn_word = random.choice(words)
    scrambled_word = "".join(random.sample(drawn_word, len(drawn_word)))
    print(f"A palavra é: {scrambled_word}")

    tries = 3
    while tries > 0:
        user_try = input(f"Adivinhe a palavra, você tem {tries} tentativas: ")

        if user_try == drawn_word:
            message = "Você acertou!"
            break
        else:
            message = "Não foi dessa vez..."
        tries -= 1

    print(f"{message} A palavra correta é {drawn_word}.")


# print(scrambled_word_game(["word1", "word2", "word3"]))

# RESPOSTA GABARITO
# WORDS = [
#     "cat",
#     "elephant",
#     "dog",
#     "monkey",
#     "duck",
#     "chameleon",
#     "bear",
#     "moose",
#     "rooster",
# ]
# MAX_ATTEMPTS = 3


# def draw_secret_word(words):
#     secret_word = random.choice(words)
#     scrambled_word = "".join(random.sample(secret_word, len(secret_word)))
#     return secret_word, scrambled_word


# def collect_guesses():
#     guesses = []
#     for attempt in range(MAX_ATTEMPTS):
#         guess = input("Guess the word: ")
#         guesses.append(guess)
#     return guesses


# def check_game_result(secret_word, guesses):
#     if secret_word in guesses:
#         print("You win")
#     else:
#         print("You lose")


# if __name__ == "__main__":
#     secret_word, scrambled_word = draw_secret_word(WORDS)
#     print(f"Scrambled word is {scrambled_word}")
#     guesses = collect_guesses()
#     check_game_result(secret_word, guesses)
