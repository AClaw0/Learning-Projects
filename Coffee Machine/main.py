MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def choose_drink():
    while True: # Keep prompting until a valid choice is made
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

        valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]

        if choice == "off":
            print("Turning off.")
            break
        elif choice == "report":
            print("\n---- Resource Report ----")
            for item, amount in resources.items():
                if item == "money":
                    print(
                        f"{item.capitalize()}: ${amount:.2f}")  # Format money with a dollar sign and two decimal places
                else:
                    print(f"{item.capitalize()}: {amount}")
            print("-------------------------\n")
        elif choice not in valid_choices:
            print("Invalid Input. Please try again.")
        else:
            check_resources(choice)

def check_resources(choice):
    # Get ingredients needed for the selected drink
    water_needed = MENU[choice]["ingredients"].get("water", 0)
    milk_needed = MENU[choice]["ingredients"].get("milk", 0)
    coffee_needed = MENU[choice]["ingredients"].get("coffee", 0)

    # Check that there is enough ingredients
    if water_needed > resources["water"]:
        print("Sorry there is not enough water.")
    elif milk_needed > resources["milk"]:
        print("Sorry there is not enough milk.")
    elif coffee_needed > resources["coffee"]:
        print("Sorry there is not enough coffe.")
    else:
        collect_money(choice)

def collect_money(choice):
    amount_owed = MENU[choice]["cost"]
    print(f"You owe: ${amount_owed:.2f}.")
    print("Please insert coins.")

    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies

    if total < amount_owed:
        print("Sorry that's not enough money. Money refunded.")
    elif total > amount_owed:
        change = total - amount_owed
        print(f"Here is ${change:.2f} dollars in change.")
        resources["money"] += amount_owed
        make_drink(choice)
    else:
        resources["money"] += amount_owed
        make_drink(choice)

def make_drink(choice):
    resources["water"] -= MENU[choice]["ingredients"].get("water", 0)
    resources["milk"] -= MENU[choice]["ingredients"].get("milk", 0)
    resources["coffee"] -= MENU[choice]["ingredients"].get("coffee", 0)
    print(f"Here is your {choice} ☕. Enjoy!")

choose_drink()