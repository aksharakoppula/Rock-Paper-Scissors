import random
score=0
game=["rock","paper","scissors"]
for i in range(len(game)):
    print(game[i])
while True:
    print("Pick Your Move")
    playermove=input()
    computerguess=random.choice(game)
    if playermove=="rock" and computerguess=="scissors":
        print("You Win!")
        score+=1
    if playermove==computerguess:
        print("Tie, Play Again")
    if playermove=="scissors" and computerguess=="paper":
        print("You Win!")
        score+=1
    if playermove=="paper" and computerguess=="rock":
        print("You Win!")
        score+=1
    if playermove=="rock" and computerguess=="paper":
        print("You Lose")
        score-=1
    if playermove=="scissors" and computerguess=="rock":
        print("You Lose")
        score-=1
    if playermove=="paper" and computerguess=="scissors":
        print("You Lose")
        score-=1
    print("score:",score) 
