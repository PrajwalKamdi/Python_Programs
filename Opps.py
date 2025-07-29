#Class and Object 

class Apple:
   #Constructor
   def __init__(self, color, size):
        self.color = color
        self.size = size
apple = Apple("red", "medium")
# print(f"Apple color: {apple.color}, size: {apple.size}")

#Single Inheritance Example
class A:
   def method_a(self):
       return "This is a method in class A."
class B(A):
   def method_b(self):
       return "This is a method in class B."

a = A()
b = B()
# print(a.method_a())
# print(b.method_a())  # Inherited from class A
# print(b.method_b())  # Method from class B


#Mutlti Level Inheritance Example
class Opps:
  def common(self):
    return "This is a common method in the Opps class."
class Parent(Opps):
  def parent_method(self):
    return "This is a method in the Parent class."
class Child(Parent):
  def child_method(self):
    return "This is a method in the Child class."
# op = Opps()
# parent = Parent()   
# child = Child()
# print(op.common())
# print(parent.parent_method()) 
# print(child.child_method())
# print(child.common())  # Inherited from Opps class
# print(parent.common())  # Inherited from Opps class 
# print(child.parent_method())  # Inherited from Parent class
# print("All methods executed successfully.")


# Example of multiple inheritance

class Father:
    def father_method(self):
        return "This is a method in the Father class."
class Mother:
    def mother_method(self):
        return "This is a method in the Mother class."
class Child(Father, Mother):
    def child_method(self):
        return "This is a method in the Child class."
child = Child() 
# print(child.father_method())
# print(child.mother_method())    
# print(child.child_method())  

# Example of hierarchical inheritance
class Animal:
    def animal_method(self):
        return "This is a method in the Animal class."
class Mammal(Animal):
    def mammal_method(self):
        return "This is a method in the Mammal class."
class Reptile(Animal):
    def reptile_method(self):
        return "This is a method in the Reptile class."

animal = Animal()
mammal = Mammal() 
reptile = Reptile()
# print(animal.animal_method())
# print(mammal.animal_method())  # Inherited from Animal class
# print(reptile.reptile_method())  # Method from Mammal class 

# Polymorphism Example
class Animal:
    def sound(self):
        return "Some generic animal sound"
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"
a=Animal()
d = Dog()
c = Cat() 
print(a.sound())  # Output: Some generic animal sound
print(d.sound())  # Output: Woof! 
print(c.sound())  # Output: Meow!

