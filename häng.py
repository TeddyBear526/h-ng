import random
ord = ["galaxy", "bucket", "whisper", "velvet", "cactus", "journey", "puzzle", "echo", "lantern", "orbit", "breeze", "mosaic", "anchor", "lemon", "guitar", "fossil", "shadow", "rocket", "pillow", "canyon", "marble", "fabric", "drift", "ember", "jungle", "novel", "quilt", "harbor", "insect", "wagon", "yield", "kite", "ocean", "xenon", "frost", "glitch", "meadow", "nickel", "umbrella", "violin", "waffle", "yacht", "zebra", "alarm", "bridge", "camera", "doctor", "eagle", "flame", "grape"]
word = random.choice(ord)
blank = ["_"]*len(word)
g = 8
gl = 0
rätt = 0
guessed_letters = []

while g > gl:
    correct_plats = 0
    a = str(input("gissa en bokstav "))
    if a in guessed_letters:
        print("Du har redan gissat den bokstaven.")
        continue
    guessed_letters.append(a)
    if a in word:
        print(f"Correct gisning, Bokstaven är på plats")
        for i, letter in enumerate(word):
            if letter == a:
                blank[i] = a
                correct_plats += 1
        print(blank)
        rätt += correct_plats
    else:
        print("bokstaven är inte i ordet")
        g+= 1
    if rätt == len(word) :
        print("Hela ordet gissat")
        print(f"ordet var", word)
        break
