# Personal Finance Tracker with Exception Handling

def finance_tracker():
    try:
        income = float(input("Enter total monthly income: "))

        n = int(input("How many expenses do you want to enter? "))
        expenses = []

        for i in range(n):
            amount = float(input(f"Enter expense {i+1}: "))
            expenses.append(amount)

        total_expenses = sum(expenses)
        savings = income - total_expenses
        percent_spent = (total_expenses / income) * 100

        # Categorization
        if percent_spent < 30:
            category = "LOW"
            message = "Good control!"
        elif percent_spent < 70:
            category = "MODERATE"
            message = "Be careful!"
        else:
            category = "HIGH"
            message = "Financial Risk!"

        print("\n------ FINANCE SUMMARY ------")
        print(f"Total Income: ₹{income}")
        print(f"Total Expenses: ₹{total_expenses}")
        print(f"Savings: ₹{savings}")
        print(f"Percentage Spent: {percent_spent:.2f}%")
        print(f"Spending Category: {category}")
        print(f"Message: {message}")

    except ValueError:
        print("Error: Please enter numeric values only!")
    except ZeroDivisionError:
        print("Error: Income cannot be zero!")
    except Exception as e:
        print("Unexpected Error:", e)

finance_tracker()
