import random
blank = ["_"]*4
ord = ["fest", "pest", "mest", "best", "cest"]

g = 8
gl = 0
rätt = 0
guessed_letters = []
word = random.choice(ord)

while g > gl:
    a = str(input("gissa en bokstav "))
    if a in guessed_letters:
        print("Du har redan gissat den bokstaven.")
        continue
    guessed_letters.append(a)
    if a in word:
        print("Correct gisning")
        rätt +=1
    else:
        print("bokstaven är inte i ordet")
        g+= 1
    if rätt == len(word):
        print("fullt gissat")
        print(f"ordet var", word)
        break
