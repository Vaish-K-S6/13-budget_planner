import os

FILE_NAME = "data.txt"

def load_data():
    budget = 0
    expenses = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
            if lines:
                budget = float(lines[0].strip())
                for line in lines[1:]:
                    category, amount = line.strip().split(",")
                    expenses.append({
                        "category": category,
                        "amount": float(amount)
                    })

    return budget, expenses


def save_data(budget, expenses):
    with open(FILE_NAME, "w") as f:
        f.write(str(budget) + "\n")
        for exp in expenses:
            f.write(f"{exp['category']},{exp['amount']}\n")


def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    expenses.append({"category": category, "amount": amount})
    print("✅ Expense added.")


def show_summary(budget, expenses):
    total_spent = sum(e["amount"] for e in expenses)
    remaining = budget - total_spent

    print("\n📊 Budget Summary")
    print("Budget:", budget)
    print("Total Spent:", total_spent)
    print("Remaining:", remaining)

    if remaining < 0:
        print("⚠️ You exceeded your budget!")

    category_totals = {}
    for e in expenses:
        category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]

    print("\nCategory Breakdown:")
    for cat, amt in category_totals.items():
        print(cat, ":", amt)


def main():
    budget, expenses = load_data()

    while True:
        print("\n💰 Budget Planner")
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            budget = float(input("Enter monthly budget: "))
            print("Budget updated.")
        elif choice == "2":
            add_expense(expenses)
        elif choice == "3":
            show_summary(budget, expenses)
        elif choice == "4":
            save_data(budget, expenses)
            print("Data saved. Goodbye 👋")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
