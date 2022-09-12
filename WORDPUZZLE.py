import random  
def choose ():#making the dict. of selected words 
    dict=['PYTHON','JUMP','BREAK','SNAKE','DECORATOR','CLASS','DEBUG','VIRUS','COMPUTER','PROGRAM','ERORR','LOOP','LENGTH','ENCAPSULATION']
    word=random.choice(dict)
    return word
#asking user info
p=input("ENTER YOUR NAME :")
n=int(1)
point=0
turn =0 
while n==1:
    select=choose()#will produce the word in jumbled format
    mixing=''.join(random.sample(select,len(select)))
   
    print("CAN YOU IDENTIFY THIS WORD : ",mixing)#asking user to identify the word
    guess = input(" ")

    if guess == select :
                print(" CORRECT ANS YOU GOT +1 P0INT ")#if identify the correct word
                point += 1
                turn += 1
            
    else:
                print("WRONG ANS YOU LOSE YOUR -1 POINT :")#if not able to identyfy
                point -= 1
                turn += 1
#only 5 chances are given to participant after 5 chances it will ask user 
# 1 for continue 0 to quit
    if turn == 5 :
        n=int(input(("IF YOU WANT TO PLAY AGAIN TYPE 1 OR 0 TO QUIT : ")))
    else : 
        pass
print ("----------THANK YOU FOR PARTICIPATING----------")
print("YOUR TOTAL SCORE IS : " , point )#produce total score 
print()
    