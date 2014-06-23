from starters import choice

def compare(choice1, choice2):
    """rock, paper, scissors match evaluator"""
    if choice1 == choice2:
        print("It is a tie!")
    elif choice1 == 'rock':
        if choice2 == 'scissors':
            print('Rock wins!')
        elif choice2 == 'paper':
            print('Paper wins!')
    elif choice1 == 'paper':
        if choice2 == 'Scissors':
            print('Scissors wins!')
        elif choice2 == 'rock':
            print('Rock wins!')
        elif choice == 'Scissors':
            if choice == 'paper':
                print ("Scissors Win!")
            elif choice2 =='rock':
                       print("Rock Wins!")
        else:
            print ("Something is Wrong!")
    
games = raw_input("Enter number of Sounds: ")
counter = 0
while counter != rounds:
    choice1 = choice()
    choice2 + choice()
    compare(choice1, choice2)
    counter += 1
                       

