import json
import os

FILENAME = "shopping_list.json"

def load_list(filename):
    """Load the shopping list from a JSON file, or return an empty list if not found."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_list(filename, shopping_list):
    """Save the shopping list to a JSON file."""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(shopping_list, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("Error saving file:", e)

def show_list(shopping_list):
    """Display the shopping list in a numbered format."""
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("\n--- Current Shopping List ---")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

def buy_list():
    """Main program loop for managing the shopping list."""
    print("----------------------------------")
    print("-------- Shopping List -----------")
    print("----------------------------------")

    shopping_list = load_list(FILENAME)

    while True:
        print("\nMenu:")
        print("1 - Add product")
        print("2 - View list")
        print("3 - Remove product")
        print("4 - Edit product")
        print("0 - Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            # Add one or more items
            while True:
                product = input("Enter the product to add (or press Enter to go back): ").strip()
                if product == "":
                    break
                if product not in shopping_list:  # prevent duplicates
                    shopping_list.append(product)
                    print(f"You added: {product}")
                else:
                    print("This item is already in the list.")
            save_list(FILENAME, shopping_list)

        elif choice == "2":
            # View list
            show_list(shopping_list)

        elif choice == "3":
            # Remove product
            if not shopping_list:
                print("The shopping list is empty.")
                continue

            print("\nRemove by:")
            print("a - Number")
            print("b - Name")
            method = input("Choose an option (a/b) or press Enter to cancel: ").strip().lower()

            if method == "a":
                show_list(shopping_list)
                idx = input("Enter the number of the product to remove: ").strip()
                if idx.isdigit():
                    idx = int(idx) - 1
                    if 0 <= idx < len(shopping_list):
                        removed = shopping_list.pop(idx)
                        print(f"Removed: {removed}")
                    else:
                        print("Invalid number.")
                else:
                    print("Invalid input.")
            elif method == "b":
                name = input("Enter the product name to remove: ").strip()
                if name in shopping_list:
                    shopping_list.remove(name)
                    print(f"Removed: {name}")
                else:
                    print("Product not found.")
            else:
                print("Removal canceled.")

            save_list(FILENAME, shopping_list)

        elif choice == "4":
            # Edit an item
            if not shopping_list:
                print("The shopping list is empty.")
                continue

            show_list(shopping_list)
            idx = input("Enter the number of the product to edit (or press Enter to cancel): ").strip()
            if idx == "":
                continue
            if idx.isdigit():
                idx = int(idx) - 1
                if 0 <= idx < len(shopping_list):
                    new_name = input("Enter the new name: ").strip()
                    if new_name:
                        old_name = shopping_list[idx]
                        shopping_list[idx] = new_name
                        print(f"Changed '{old_name}' to '{new_name}'.")
                        save_list(FILENAME, shopping_list)
                    else:
                        print("Empty input. Edit canceled.")
                else:
                    print("Invalid number.")
            else:
                print("Invalid input.")

        elif choice == "0":
            save_list(FILENAME, shopping_list)
            print("Exiting... Shopping list saved. Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    buy_list()
