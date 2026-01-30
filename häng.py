import random
ord = [
    "algorithm", "argument", "asynchronous", "attribute", "boolean",
    "breakpoint", "bytecode", "callable", "class", "closure",
    "compilation", "concatenation", "concurrency", "conditional", "constructor",
    "context", "coroutine", "decorator", "dependency", "dictionary",
    "encapsulation", "exception", "expression", "framework", "generator",
    "immutable", "inheritance", "instantiation", "interpreter", "iteration",
    "keyword", "lambda", "metaclass", "module", "multithreading",
    "mutable", "namespace", "operator", "parameter", "polymorphism",
    "recursion", "refactoring", "repository", "serialization", "syntax",
    "traceback", "tuple", "variable", "virtualenv", "yield"
]
word = random.choice(ord)
blank = ["_"]*len(word)
guesses = 8
guesses_left = 0
alphabet = list("qwertyuiopasdfghjklzxcvbnm")
right = 0
guessed_letters = []

while guesses > guesses_left:
    correct_plats = 0
    guessed = str(input("gissa en bokstav "))
    if guessed in alphabet:
        if guessed in guessed_letters:
            print("Du har redan gissat den bokstaven.")
            print(f"Du har gissat", guessed_letters)
            continue
        guessed_letters.append(guessed)
        if guessed in word:
            print(f"Correct gisning, Bokstaven är på plats")
            for i, letter in enumerate(word):
                if letter == guessed:
                    blank[i] = guessed
                    correct_plats += 1
            print(blank)
            right += correct_plats
        else:
            print("bokstaven är inte i ordet")
            guesses_left += 1; print(f"du har {guesses-guesses_left} gissningar kvar")
            print(f"Du har gissat", guessed_letters)
        if right == len(word) :
            print("Hela ordet gissat")
            print(f"ordet var", word)
            if guesses_left == 0:
                print("""
            ────────────████████────── 
            ───────────██████████───── 
            ──────────█▄▄▄████▄▄▄█──── 
            ─────▄───█░░░░░██░░░░░█─── 
            ─────█──░░░▓■▓░░░░▓■▓░░░── 
            ─────█──▐█░▓▓▓░██░▓▓▓░█▌── 
            ─────█──▐██░░░████░░░██▌── 
            ─────█──▐█▛██████████▛█▌── 
            ──▌▌▌▄▄──██▚████████▞██─── 
            ──▌▌▌▀█──████▀████▀████─── 
            ──▄▄▄██───████▄■■▄████──── 
            ──▜███▛────██████████───── 
            ───███──────████████──────
                """)
            break
    elif guessed != alphabet:
        print("det måste vara EN bokstav")
if guesses_left == guesses:
    print("du fick slut på gissningar")
    print("""
    ░░░░░░░░░░░░░░░░░░░░░░░░░░ 
    ░█░░░█░█▀█░█░░░█░█▀▄░░░░░░ 
    ░█░▄░█░█░█░██░██░█░█░░░░░░ 
    ░▀▄█▄▀░█░█░█░▀░█░█▀▀░░░░░░ 
    ░░▀░▀░░▀▀▀░▀░░░▀░█░░░░░░░░ 
    ░░░░░░░░░░░░░░░░░▀░░░░░░░░ 
    ░░░░░░░░░░░░░░░░░░░░░░░░░░ 
    ░░░░░█░░░█░█▀█░█░░░█░█▀▄░░ 
    ░░░░░█░▄░█░█░█░██░██░█░█░░ 
    ░░░░░▀▄█▄▀░█░█░█░▀░█░█▀▀░░ 
    ░░░░░░▀░▀░░▀▀▀░▀░░░▀░█░░░░ 
    ░░░░░░░░░░░░░░░░░░░░░▀░░░░ 
    ░░░░░░░░░░░░░░░░░░░░░░░░░░    
    """)
    print(f"ordet var {word}")