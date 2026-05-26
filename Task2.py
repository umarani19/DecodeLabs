print("=== Daily Expense Calculator ===")
grand_total = 0
while True:
    user_input = input("Add your expense (type 'stop' to finish): ")
    if user_input.lower() == "stop":
        break
    try:
        amount = float(user_input)
        if amount < 0:
            print("Expense cannot be negative!")
            continue
        grand_total = grand_total + amount
        print("Updated Balance Spent =", grand_total)
    except:
        print("Please enter a valid amount!")
print("\n===== Expense Summary =====")
print("Total Money Spent:", grand_total)
print("Thank you for using Expense Calculator!")