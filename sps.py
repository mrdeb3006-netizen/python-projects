'''
-1 for stone
0 for paper
1 for scissor 
'''
import random
computer=random.choice([1,-1,0])
youstr=input("enter your choice:")
youDict={"s":-1,"p":0,"sc":1}
reverseDict={-1:"stone",0:"paper",1:"scissor"}
you=youDict[youstr]
print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("its a draw!")
else:
    if(computer==-1 and you==0):
        print("you win!")
    elif(computer==-1 and you==1):
        print("you lose!")
    elif(computer==0 and you==-1):
        print("you lose!")
    elif(computer==0 and you==1):
        print("you win!")
    elif(computer==1 and you==0):
        print("you lose!")
    elif(computer==1 and you==-1):
        print("you win!")
    else:
        print("something went wrong")


