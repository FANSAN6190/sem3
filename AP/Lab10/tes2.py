class Person:
  asg=23
  print(asg)
  def __init__(self, name, age):
    self.name = name
    self.age = age
    asd=124

p1 = Person("John", 36)

print(p1.name,p1.age)