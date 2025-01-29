#Activity 1
# Base class: Device
class Device:
    def __init__(self, brand, model, battery_life):
        self.brand = brand
        self.model = model
        self.battery_life = battery_life

    def display_info(self):
        return f"{self.brand} {self.model} - Battery Life: {self.battery_life} hours"

# Derived class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, battery_life, operating_system, camera_quality):
        super().__init__(brand, model, battery_life)
        self.operating_system = operating_system
        self.camera_quality = camera_quality

    def display_info(self):
        return f"{super().display_info()} - OS: {self.operating_system}, Camera Quality: {self.camera_quality} MP"

# Example objects
iphone = Smartphone("Apple", "iPhone 13", 20, "iOS", 12)
galaxy = Smartphone("Samsung", "Galaxy S21", 18, "Android", 108)

# Display smartphone info
print(iphone.display_info())
print(galaxy.display_info())


#Activity 2
# Base class: Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Derived class: Dog
class Dog(Animal):
    def move(self):
        return "Running on four legs 🐕"

# Derived class: Bird
class Bird(Animal):
    def move(self):
        return "Flying through the air 🦅"

# Derived class: Fish
class Fish(Animal):
    def move(self):
        return "Swimming in the water 🐟"

# Example objects
dog = Dog()
bird = Bird()
fish = Fish()

# Display movement actions
print(f"Dog: {dog.move()}")
print(f"Bird: {bird.move()}")
print(f"Fish: {fish.move()}")
