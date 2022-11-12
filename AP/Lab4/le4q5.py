'''P5. Write a python program to solve a classic ancient Chinese puzzle.
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits
and how many chickens do we have?
Sample Input
Expected Output
heads-150 legs-400 100
50
heads-3 legs-11 No solution
heads-3 legs-12 0
3
heads-5 legs-10 5
0'''

l=int(input("Enter the Number of Legs = "))
h=int(input("Enter the Number of Heads = "))
R=(l-(2*h))/2
H=((4*h)-l)/2
print(R,H)