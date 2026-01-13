word = "test" 

g = 8
gl = 0
guessed_letters = []
while g > gl:
    a = str(input("gissa en bokstav "))
    if a in guessed_letters:
        print("Du har redan gissat den bokstaven.")
        continue
    guessed_letters.append(a)
    input("hej ")