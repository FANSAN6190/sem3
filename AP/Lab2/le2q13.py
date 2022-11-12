#13: A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn
#      is input through the keyboard in tens, hundreds or thousands, find the total number of
#      currency notes of each denomination the cashier will have to give to the withdrawer.
wa=float(input("Withdrawl Amount = "))
n100=n50=n10=0
while wa>=10:
    if wa>=100:
        wa=wa-100
        n100+=1
    elif wa>=50:
        wa=wa-50
        n50+=1
    elif wa >=10:
        wa=wa-10
        n10+=1
    else:
        print("Wrong Input")
print("Rs. 100 Notes = ",n100 )
print("Rs. 50 Notes = ",n50 )
print("Rs. 10 Notes = ",n10 )
print("Remaining amount = ",wa)
