# Virtual Pet Simulator - OOP Challenge

## 🐾 Project Overview

This Python project implements a Virtual Pet Simulator using Object-Oriented Programming (OOP) principles. The application allows you to create and interact with a virtual pet by feeding it, playing with it, letting it sleep, and even teaching it new tricks!

## 🧠 Learning Objectives

This project demonstrates several key OOP concepts in Python:
- Classes and Objects
- Attributes (properties) and Methods (behaviors)
- Constructors (`__init__`)
- Instance methods
- State management through attribute values
- Basic user interaction through the command line

## 🛠️ Features

The Virtual Pet has the following characteristics:

### Attributes:
- `name`: The name of your pet
- `hunger`: Integer representing hunger level (0 = full, 10 = very hungry)
- `energy`: Integer representing energy level (0 = tired, 10 = fully rested)
- `happiness`: Integer representing happiness level (0-10)
- `tricks`: List of tricks the pet has learned (bonus feature)

### Methods:
- `eat()`: Reduces hunger by 3 points (but not below 0) and increases happiness by 1
- `sleep()`: Increases energy by 5 points (but not above 10)
- `play()`: Decreases energy by 2, increases happiness by 2, and increases hunger by 1
- `get_status()`: Displays the current state of all pet attributes
- `train(trick)`: Teaches your pet a new trick (bonus feature)
- `show_tricks()`: Displays all tricks your pet has learned (bonus feature)

## 📁 Project Structure

```
OOP-Challenge/
│
├── pet.py            # Contains the Pet class definition
├── main.py           # Main program for interacting with your pet
├── README.md         # Project documentation
│
└── screenshots/      # Folder containing output screenshots
    └── virtual_pet_demo.png  # Screenshot of the running application
```

## 🚀 How to Run

1. Clone this repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd OOP-Challenge
   ```

3. Run the main program:
   ```
   python main.py
   ```

4. Follow the on-screen prompts to interact with your virtual pet!

## 📝 Code Examples

### Creating a Pet (from main.py)
```python
from pet import Pet

# Create a new pet
pet_name = input("What would you like to name your pet? ")
my_pet = Pet(pet_name)
```

### Pet Class Example (from pet.py)
```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Starting value
        self.energy = 5  # Starting value
        self.happiness = 5  # Starting value
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
```

## 📸 Screenshots

The `screenshots` folder contains visual examples of the application in action:

- `virtual_pet_demo.png`: Shows the interactive menu and pet status display

## 🎯 Bonus Challenges Completed

- Added method `train(trick)` that teaches the pet a new trick and stores it in a list
- Added method `show_tricks()` that displays all learned tricks
- Implemented boundary checking to ensure attribute values stay within proper ranges
- Created an interactive menu system for better user experience

## 🧪 Future Enhancements

Possible enhancements for this project could include:
- Graphical user interface (GUI)
- Saving/loading pet progress
- Different pet types with unique behaviors
- Pet aging system
- Health status based on other attributes
- Various types of food and activities

## 📜 License

This project is created for educational purposes as part of the OOP Challenge.

## 👏 Acknowledgements

Original challenge by [Evans-mutuku](https://github.com/Evans-mutuku/OOP-Challenge)
