def is_palindrome(a):
      if a == a[::-1]:
        return True
      else:
        return False
    
   

a= str(input('Enter your name\n'))
#a = print(reverse(string))
print(is_palindrome(a))
    
