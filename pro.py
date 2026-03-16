
food_list = []

def add_food():
    restaurant = input("Restaurant Name: ")
    food_item = input("Food Item: ")
    quantity = input("Quantity (e.g., 5 plates): ")
    location = input("Location: ")
    time_available = input("Time Available: ")

    food_list.append({
        "restaurant": restaurant,
        "food": food_item,
        "quantity": quantity,
        "location": location,
        "time": time_available
    })
    print("Food added successfully!\n")


def view_food():
    if not food_list:
        print("No food available.\n")
        return
    print("\nAvailable Food:\n")
    for i, food in enumerate(food_list, 1):
        print(f"{i}. {food['restaurant']} - {food['food']} - {food['quantity']} - {food['location']} - {food['time']}")
    print()


def claim_food():
    if not food_list:
        print("No food available.\n")
        return
    view_food()
    try:
        choice = int(input("Enter food number to claim: "))
        if 0 < choice <= len(food_list):
            claimed_food = food_list.pop(choice-1)
            print(f"You claimed: {claimed_food['food']} from {claimed_food['restaurant']}\n")
        else:
            print("Invalid choice.\n")
    except ValueError:
        print("Enter a valid number.\n")


def main():
    while True:
        print("\n=== Mini Food Waste App ===")
        print("1. Add Food (Restaurant)")
        print("2. View Available Food (User)")
        print("3. Claim Food (User)")
        print("4. Exit")

        choice = input("Choose option: ")
        if choice == "1":
            add_food()
        elif choice == "2":
            view_food()
        elif choice == "3":
            claim_food()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    main()