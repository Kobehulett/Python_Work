print("Hello and welcome to the game of Rock, Paper, Scissors!!!!")
answer =input("are you ready to play yes or no?")
computer_options = ["rock", "paper", "Scissors"]

if answer.lower() == "no":
    print ("welp! goodbye!")
else:
    print("Hooray!, well lets begin")
    print("Rock......Paper.....Scissors.....SHOOT!")
rounds = 0
score = 0

while rounds == 0:
    for i in range (3):
        answer =input("type your move")
        import random
        computer_results = random.choice(computer_options)
        print("My move is..." + str(computer_results))
        players_answer = answer
        if computer_results== players_answer:
            Print("tied")
            rounds+=1
            print("Your score is: ", score)
        elif computer_results=="rock" and players_answer=="scissors":
            print("I win")
            rounds+=1
            print("Your score is: ", score)
            
                
        elif computer_results=="paper" and players_answer=="rock":
            print("I win")
            rounds+=1
            print("Your score is: ", score)
        
        elif computer_results=="scissors" and players_answer=="paper":
            print("I win")
            rounds+=1
            print("Your score is: ", score)
        
        else:
            print("Aww man you win!")
            rounds +=1 
            score +=1
            print("your score: ", score)
    print(" ")
    if score >2:
        print("Congrats! You Won The Game!!")
        print("CLick to play again")
    else:
        print("Click run to try again")
            
    