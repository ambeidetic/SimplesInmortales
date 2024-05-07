class Animal:
    isEating = False
    isSleeping = False
    diet = "unknown"

    def __init__(self, name):
        self.name = name
    
    def eat(self, food="Canned food"):
        if(food == "meat"):
            self.diet = "carnivore"
        elif(food == "grass" and self.diet == "meat"):
            self.diet = "omnivore"
        elif(food == "grass"):
            self.diet = "herbivore"

        if(self.isSleeping):
            print(f"{self.name} is speeping, can't eat now")
            return

        self.isEating = True
        print(f"{self.name} is eating {food}")
        self.isEating = False
    
    def sleep(self):
        self.isSleeping = True
        print(f"{self.name} is sleeping")

    def StopSleeping(self):
        self.isSleeping = False
        print(f"{self.name} is awake")

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")
        


animal = Animal("Animal")

print(animal.diet)
animal.eat("meat")
print(animal.diet)
animal.sleep()
animal.eat("grass")
print(animal.diet)
animal.StopSleeping()
animal.eat()

class Dog(Animal):
    def speak(self):
        print(f"Woof from dog {self.name}")

class Cat(Animal):
    def speak(self):
        print("Meow")

dogs = []

# for i in [1,2,3,4,5,6,7,8,9,10]:
for i in range(10):
    dog = Dog(f"Dog_{i}")
    dogs.append(dog)

for dog in dogs:
    dog.speak()