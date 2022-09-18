#B. Write a python function to print following shape
def sh(n):
    for i in range(0,(5*n)+1):
        for j in range(0,(5*n)+1):
            if i+j==0 or i%5==j%5==0:
                print('+',end='')
            elif(i==0 or i%5==0):
                print('-',end='')
            elif(j%5==0 or j==0):
                print('|',end='')
            else:
                print(' ',end='')
        print('')
sh(4)
