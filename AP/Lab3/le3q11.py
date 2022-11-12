#11. Compute the area of a rectangular prism, when its all sides are given.
def arp(l,b,h):
    return 2*(l*b+b*h+l*h)
l=int(input())
b=int(input())
h=int(input())
print(arp(l,b,h))

def arp(l,b,h):
    print(2*(l*b+b*h+l*h))
l=int(input())
b=int(input())
h=int(input())
arp(l,b,h)
