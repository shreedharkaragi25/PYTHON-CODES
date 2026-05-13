
# Mini Shopping Cart System

cart = []

while True:
    print("\n1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Calculate Total Bill")
    print("5. Show Duplicate Items")
    print("6. Display Cart")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item name: ")
        cart.append(item)
        print(item, "added to cart.")

    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart.")
        else:
            print("Item not found.")

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print(item, "is in the cart.")
        else:
            print(item, "not found.")

    elif choice == 4:
        prices = []
        for item in cart:
            price = float(input("Enter price for " + item + ": "))
            prices.append(price)
        print("Total Bill =", sum(prices))

    elif choice == 5:
        duplicates = []
        for item in cart:
            if cart.count(item) > 1 and item not in duplicates:
                duplicates.append(item)

        if duplicates:
            print("Duplicate Items:", duplicates)
        else:
            print("No duplicate items.")

    elif choice == 6:
        print("Cart Items:", cart)

    elif choice == 7:
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice.")