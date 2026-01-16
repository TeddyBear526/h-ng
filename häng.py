import random
ord = ["__","__","__","__"]
p = ["fest", "pest", "mest", "best", "cest"]

print(p[2])

print(list(p[2]))

g = 8
gl = 0
guessed_letters = []
while g > gl:
    word = random.choice(p)
    a = str(input("gissa en bokstav "))
    if a in guessed_letters:
        print("Du har redan gissat den bokstaven.")
        continue
    guessed_letters.append(a)
    if a in word:
        print("Correct gisning")
