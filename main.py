from pet import Pet

def main():
    # Create a new pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"Welcome to Virtual Pet Simulator! You've adopted {pet_name}!")
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Train your pet a new trick")
        print("6. Show pet's tricks")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            print(my_pet.eat())
        elif choice == '2':
            print(my_pet.sleep())
        elif choice == '3':
            print(my_pet.play())
        elif choice == '4':
            print(my_pet.get_status())
        elif choice == '5':
            trick = input("What trick would you like to teach? ")
            print(my_pet.train(trick))
        elif choice == '6':
            print(my_pet.show_tricks())
        elif choice == '7':
            print(f"Goodbye! Take care of {pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()