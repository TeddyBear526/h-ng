import random
ord = ["galaxy", "bucket", "whisper", "velvet", "cactus", "journey", "puzzle", "echo", "lantern", "orbit", "breeze", "mosaic", "anchor", "lemon", "guitar", "fossil", "shadow", "rocket", "pillow", "canyon", "marble", "fabric", "drift", "ember", "jungle", "novel", "quilt", "harbor", "insect", "wagon", "yield", "kite", "ocean", "xenon", "frost", "glitch", "meadow", "nickel", "umbrella", "violin", "waffle", "yacht", "zebra", "alarm", "bridge", "camera", "doctor", "eagle", "flame", "grape"]
word = random.choice(ord)
blank = ["_"]*len(word)
guesses = 8
guesses_left = 0
right = 0
guessed_letters = []

while guesses > guesses_left:
    correct_plats = 0
    guessed = str(input("gissa en bokstav "))
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
        guesses += 1; print(f"Du har {guesses_left} Gissningar kvar")
        print(f"Du har gissat", guessed_letters)
    if right == len(word) :
        print("Hela ordet gissat")
        print(f"ordet var", word)
        break
