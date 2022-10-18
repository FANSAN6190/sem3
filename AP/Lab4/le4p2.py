#P2. Pure Gems Store sells different varieties of gems to its customers.
#    Emerald, Ivory, Jasper, Ruby, Garnet and their prices are 1760, 2119, 1599, 3920, 3999
#    respectively.
#    Write a Python program to calculate the bill amount to be paid by a customer based on the list
#    of gems and quantity purchased. Any purchase with a total bill amount above Rs.30000 is
#    entitled for 5% discount. If any gem required by the customer is not available in the store,
#    then consider total bill amount to be -1.
#    Assume that quantity required by the customer for any gem will always be greater than 0.
#    Perform case-sensitive comparison wherever applicable
gem=('Emerald','Ivory', 'Jasper', 'Ruby', 'Garnet')
price=(1760, 2119, 1599, 3920, 3999)
print(gem)
print(price)
g=input("Enter the gem Name = ")
q=int(input("Enter the Quantity = "))
if g not in gem:
    amount=-1
else:
    a=gem.index(g)
    amount=price[a]*q
    if amount>30000:
        amount=amount-((5/100)*amount)
print("Total Bill Amount = ",amount)

                                                                        
