# Lesson 19. Capstone project: Scrabble, Art Edition
word=("art","hue","ink","oil","pen","wax","clay","draw","film","crosshatching")

tiles="arrthusse"
possible_word=()

for oneword in word:
    tiles2=tiles
    found=""
    for letter in oneword:
        if tiles2.find(letter)>=0:
            tiles2=tiles2.replace(letter,"")
            found=found+letter
        else:
            found=""
            break
    possible_word=possible_word+(found,)

for k in possible_word:
    if k: # only print non empty object in a tuple
        print("Possible word is", k)



