#7. Convert a temperature from Fahrenheit to Celsius.
def fc(f):
    return (f-32)*5/9
f=int(input(" F = "))
print("C=",fc(f))
