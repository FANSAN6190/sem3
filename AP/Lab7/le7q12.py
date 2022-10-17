#12. Write a python script to make word guessing game. The game runs as follows:
def repl(nwor,p,ch):
    nwor=list(nwor)
    nwor[p]=ch
    nstr="".join(nwor) 
    return nstr

import random
word_lis=["hello","freinds","birthday","home","computer","father"]
word=word_lis[random.randint(0,4)]
atmp=len(word)
msk_word='*'*atmp
p=(-1)
while(atmp>0):
    print("--------------------------------------------")
    print("word is ",msk_word," its length is ",atmp)
    print("you have ",atmp," attempts left")
    ch=input("Enter a Char(lowercase) = ")
    prv_guess=""
    prv_guess=prv_guess+ch
    if ch in word:
        p=word.index(ch)
        msk_word=repl(msk_word,p,ch)
        print("correct..")
        
    else:
        print("previous guess ",prv_guess)
        print("try again...")
        atmp-=1
    print("word is ",msk_word)
    if(msk_word==word):
        print("CONGRATULATIONS! you got the word.")
        p=0
        break
    print("--------------------------------------------")

if p!=0:
    print("sorry, You have lost.")
    print("the Correct word is ",word)
