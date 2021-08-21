print("Welcome to the Quiz")

playing = input("Do you want to play? ")
score = 0

if playing.lower() != "yes":
    print("Sorry to hear that")
    quit()

print("WELCOME TO THE RICE FIELDS BIH"+ "\n")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Well Done Mate!'+ "\n")
    score += 1
else: 
    print("Incorrect! Get good at the game!"+ "\n")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Yalla Habibi, your on a roll!'+ "\n")
    score += 1
else: 
    print("You know what you are... An idiot sandwich!"+ "\n")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Fuck me, you truly are insane at the game!'+ "\n")
    score += 1
else: 
    print("You know what you are... An idiot sandwich!"+ "\n")

answer = input("What is the best console? ")
if answer.lower() == "ps4":
    print('Mate you deserve this... Drinks on me!'+ "\n")
    score += 97
else: 
    print("You... Get the fuck outta me face!" + "\n")

if score <= 20:
    print("YOUR SHIT AT THE GAME" + "\n")

print("You got a score of " + str(score) + "!")
print("You got " + str(score/4 * 100) + "% of questions correct!")

