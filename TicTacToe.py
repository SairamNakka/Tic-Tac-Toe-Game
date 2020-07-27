import random
import time
def table(board):
    print("   |"+"   | "+"   ")
    print(" "+board[0]+" | "+ board[1]+" | "+ board[2] )
    print("   |"+"   | "+"   ")
    print("-----------")
    print("   |"+"   | "+"   ")
    print(" "+board[3]+" | "+ board[4]+" | "+ board[5] )
    print("   |"+"   | "+"   ")
    print("-----------")
    print("   |"+"   | "+"   ")
    print(" "+board[6]+" | "+ board[7]+" | "+ board[8] )
    print("   |"+"   | "+"   ")

def toss():
    c=[0,1]
    toss=random.choice(c)
    if toss==0:
        return "computer"
    else:
        return "player"
    
def choice(first_turn):
    if first_turn=="computer":
        return "X"
    else:
        return "O"
    
def winner(board,le):
    if((board[0]==board[1]==board[2]==le) or (board[3]==board[4]==board[5]==le) or
       (board[6]==board[7]==board[8]==le) or (board[0]==board[4]==board[8]==le) or
       (board[2]==board[4]==board[6]==le) or (board[0]==board[3]==board[6]==le) or
       (board[1]==board[4]==board[7]==le) or (board[2]==board[5]==board[8]==le)):
        return True
    else:
        return False
print("The moves in the game is as follows..")
print("0|1|2")
print("-----")
print("3|4|5")
print("-----")
print("6|7|8")
first=toss()
choice(first)
print("The",first,"will go first")
choices=["X","O"]
if first=="computer":
    cmp_choice=random.choice(choices)
    if cmp_choice=="X":
        ply_choice="O"
    else:
        ply_choice="X"
else:
    print("Do you want to be X or O?")
    ply_choice=input()
    if ply_choice=="X":
        cmp_choice="O"
    else:
        cmp_choice="X"
choice(first)
print("")
print("The computer's letter is ",cmp_choice)
print("The player's letter is ",ply_choice)
print("-----------")
board=[" "," "," "," "," "," "," "," "," "]
nums=[0,1,2,3,4,5,6,7,8]
while(len(nums)!=0):    
    if first=="player":
        print("what is your move?(0-8)")
        p=int(input())
        if p in nums:
            board[p]=ply_choice
            nums.remove(p)
        else:
            print("That choice is already selected..You lost one choice")
        if(winner(board,ply_choice)==True):
            print("-----------")
            print("Congratulations you won the Game!!")
            break
        if len(nums)!=0:
            c=random.choice(nums)
            board[c]=cmp_choice
            nums.remove(c)
        if(winner(board,cmp_choice)==True):
            print("-----------")
            print("Computer won the game!!")
            break
    else:
        c=random.choice(nums)
        print("computer's choice is ",c)
        nums.remove(c)
        board[c]=cmp_choice
        if(winner(board,cmp_choice)==True):
            print("-----------")
            print("Computer won the game!!")
            break
        if len(nums)!=0: 
            print("what is your move?(0-8)")
            p=int(input())
            if p in nums:
                nums.remove(p)
                board[p]=ply_choice
            else:
                print("Oops! That choice is already selected..You lost one Choice")
        if(winner(board,ply_choice)==True):
            print("-----------")
            print("Congratulations you won the Game!!")
            break       
            
            
    table(board)
time.sleep(2)    
table(board)
