class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting value (0 = full, 10 = very hungry)
        self.energy = 5  # Starting value (0 = tired, 10 = fully rested)
        self.happiness = 5  # Starting value (0-10)
        self.tricks = []  # For bonus functionality
    
    def eat(self):
        if self.hunger >= 3:
            self.hunger -= 3
        else:
            self.hunger = 0
        self.happiness += 1
        if self.happiness > 10:
            self.happiness = 10
        return f"{self.name} has eaten and is feeling better!"
    
    def sleep(self):
        self.energy += 5
        if self.energy > 10:
            self.energy = 10
        return f"{self.name} took a nap and is feeling refreshed!"
    
    def play(self):
        if self.energy < 2:
            return f"{self.name} is too tired to play!"
        self.energy -= 2
        self.happiness += 2
        if self.happiness > 10:
            self.happiness = 10
        self.hunger += 1
        if self.hunger > 10:
            self.hunger = 10
        return f"{self.name} had fun playing!"
    
    def get_status(self):
        status = f"Pet Status for {self.name}:\n"
        status += f"Hunger: {self.hunger}/10 (0 = full, 10 = very hungry)\n"
        status += f"Energy: {self.energy}/10 (0 = tired, 10 = fully rested)\n"
        status += f"Happiness: {self.happiness}/10\n"
        return status
    
    # Bonus functionality
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.energy -= 1  # Training is tiring
            self.happiness += 1  # But rewarding!
            if self.energy < 0:
                self.energy = 0
            if self.happiness > 10:
                self.happiness = 10
            return f"{self.name} learned to {trick}!"
        else:
            return f"{self.name} already knows how to {trick}!"
    
    def show_tricks(self):
        if not self.tricks:
            return f"{self.name} doesn't know any tricks yet."
        return f"{self.name} knows these tricks: {', '.join(self.tricks)}"