import random
import os

CARDS=[11,2,3,4,5,6,7,8,9,10,10,10,10]
USER_CARDS=[]
COMPUTER_CARDS=[]

   
def deal_user():
    USER_CARDS.append(random.choice(CARDS))

def deal_computer():
    COMPUTER_CARDS.append(random.choice(CARDS))



def isblackjack():
    isace()
    if sum(USER_CARDS)==21 or sum(COMPUTER_CARDS)==21:
        return 0
    
    if sum(USER_CARDS)>21 or sum(COMPUTER_CARDS)>21:
        return 0  
    return True


def isace():
    if 11 in USER_CARDS and sum(USER_CARDS)>21:
        place=USER_CARDS.index(11)
        USER_CARDS[place]=1

    if 11 in COMPUTER_CARDS and sum(COMPUTER_CARDS)>21:
        place=COMPUTER_CARDS.index(11)
        COMPUTER_CARDS[place]=1



def stand_or_take():
    while True:
        result=isblackjack()
        print(f"Your cards are: {USER_CARDS}")
        print(f"Your total hand is: {sum(USER_CARDS)}")
        print(f"Computer first card is: {COMPUTER_CARDS[0]}")    
        if result:
            choice=input("Do you want to take another card? (y/n): ").lower()
            if choice=="y":
                deal_user()
            else:
                computer_stand_or_take()
                break
        else:
            break
              
    compare()


def computer_stand_or_take():
    while sum(COMPUTER_CARDS)<17:
        deal_computer()
        isace()
    
    os.system("cls")

    print(f"Your cards are: {USER_CARDS}")
    print(f"Your total hand is: {sum(USER_CARDS)}")

    print(f"Computer cards are: {COMPUTER_CARDS}")
    print(f"Computer total hand is: {sum(COMPUTER_CARDS)}")
    


def compare():
    if sum(USER_CARDS)>21:
        print("computer won!")

    elif sum(USER_CARDS)==21:
        print("You won!")

    elif sum(USER_CARDS)==sum(COMPUTER_CARDS):
        print("it's a tie!")

    elif sum(USER_CARDS)>sum(COMPUTER_CARDS):
        print("you won!")
    
    elif sum(COMPUTER_CARDS)>21:
        print("you won")
    
    else:
        print("computer won!")



while True:    
    USER_CARDS=random.choices(CARDS,k=2)
    COMPUTER_CARDS=random.choices(CARDS,k=2)
    stand_or_take()
    input("Press enter to play again: ")
    os.system("cls")

