from abc import ABC, abstractmethod

# ---------- ABSTRACT CLASS ----------
class Expense(ABC):
    def __init__(self, amount, note):
        self.amount = amount
        self.note = note

    @abstractmethod
    def category(self):
        pass


# ---------- CHILD CLASSES ----------
class FoodExpense(Expense):
    def category(self):
        return "Food"


class TravelExpense(Expense):
    def category(self):
        return "Travel"


class OtherExpense(Expense):
    def category(self):
        return "Other"


# ---------- USER CLASS ----------
class User:
    def __init__(self, name):
        self.name = name
        self.__income = 0
        self.__expenses = []

    def add_income(self, amount):
        self.__income += amount
        print("Income added successfully!")

    def add_expense(self, expense):
        self.__expenses.append(expense)
        print(f"{expense.category()} expense added!")

    def total_expense(self):
        return sum(exp.amount for exp in self.__expenses)

    def balance(self):
        return self.__income - self.total_expense()

    def show_expenses(self):
        if not self.__expenses:
            print("No expenses found.")
            return
        print("\n--- Expense List ---")
        for exp in self.__expenses:
            print(f"{exp.category()} | ₹{exp.amount} | {exp.note}")

    def summary(self):
        print("\n--- Expense Summary ---")
        print("Total Income :", self.__income)
        print("Total Expense:", self.total_expense())
        print("Balance      :", self.balance())


# ---------- KEYWORDS BY CATEGORY ----------
expense_keywords = {
    "Food": [
        "food", "lunch", "dinner", "breakfast", "snacks",
        "groceries", "vegetables", "fruits", "market"
    ],
    "Travel": [
        "bus", "train", "metro", "flight", "auto", "taxi", "cab"
    ],
    "Other": [
        "rent", "electricity", "water", "gas",
        "mobile", "recharge", "shopping", "market"
    ]
}

category_map = {
    "1": "Food",
    "2": "Travel",
    "3": "Other"
}


# ---------- MAIN PROGRAM ----------
while True:
    user_name = input("Enter your name: ").strip()
    vowels = "aeiouAEIOU"
    

    if len(user_name) < 3:
        print("❌ Name must contain at least 3 characters.")
        continue
    
    if not any(char in vowels for char in user_name):
        print("❌ Name should contain at least one vowel.")
        continue


    if not user_name.replace(" ", "").isalpha():
        print("❌ Name should contain only letters and spaces.")
        continue

    break   # valid name

user = User(user_name)

while True:
    print("\n1.Add Income  2.Add Expense  3.View Expenses  4.View Summary  5.Exit")
    choice = input("Enter choice: ")

    # -------- ADD INCOME --------
    if choice == "1":
        try:
            amt = float(input("Enter income amount: "))
            if amt <= 0:
                print("❌ Income must be greater than zero.")
                continue
            user.add_income(amt)
        except ValueError:
            print("❌ Invalid amount! Enter numbers only.")

    # -------- ADD EXPENSE --------
    elif choice == "2":
        print("1.Food  2.Travel  3.Other")
        exp_choice = input("Choose expense type: ")

        if exp_choice not in category_map:
            print("⚠️ Invalid selection! Please choose 1, 2, or 3.")
            continue

        category = category_map[exp_choice]
        keywords = expense_keywords[category]

        # Amount validation
        try:
            amt = float(input("Enter expense amount: "))
            if amt <= 0:
                print("❌ Amount must be greater than zero.")
                continue
        except ValueError:
            print("❌ Invalid amount! Enter numbers only.")
            continue

        # Note validation
        note = input("Enter note: ").strip()
        note_lower = note.lower()

        if len(note) < 3:
            print("❌ Note must contain at least 3 characters.")
            continue

        if not note.replace(" ", "").isalnum():
            print("❌ Note should contain only letters and spaces.")
            continue

        if not any(word in note_lower for word in keywords):
            print(f"⚠️ Please enter a valid {category} related note.")
            continue

        # Create expense object
        if exp_choice == "1":
            expense = FoodExpense(amt, note)
        elif exp_choice == "2":
            expense = TravelExpense(amt, note)
        else:
            expense = OtherExpense(amt, note)

        user.add_expense(expense)

    # -------- VIEW EXPENSES --------
    elif choice == "3":
        user.show_expenses()

    # -------- VIEW SUMMARY --------
    elif choice == "4":
        user.summary()

    # -------- EXIT --------
    elif choice == "5":
        print("Thank you for using Smart Expense Tracker!")
        break

    else:
        print("❌ Invalid choice! Try again.")
