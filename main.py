# main.py

import importlib

# Dictionary to map chef names to their corresponding modules
chefs = {
    "default": "default_chef",
    "indian": "Abhi_mIOHa2",
    "B": "B",
    "C": "C",
    "D": "D",
    "E": "E"
}

def handle_interaction(chef_module, user_input):
    try:
        module = importlib.import_module(chef_module)
        module.handle_request(user_input)
    except Exception as e:
        print(f"Error interacting with {chef_module}: {e}")

def main():
    while True:
        print("Choose a chef to interact with: default, indian, B, C, D, E")
        chef_choice = input().strip()
        if chef_choice in chefs:
            user_input = input("Enter your request (Ingredients:/Dish:/Recipe:):\n")
            handle_interaction(chefs[chef_choice], user_input)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
