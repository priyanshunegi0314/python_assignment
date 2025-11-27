def add_record():
    with open("vaccine.txt", "a") as f:
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        dose = input("Dose Number (1/2): ")
        date = input("Vaccination Date: ")

        f.write(f"{name:<15}{age:<10}{dose:<10}{date:<10}\n")
    print("Record added successfully!\n")

def display_records():
    try:
        with open("vaccine.txt", "r") as f:
            print(f"{'Name':<15}{'Age':<10}{'Dose':<10}{'Date':<10}")
            print("-" * 45)
            for line in f:
                print(line, end="")
    except FileNotFoundError:
        print("No records found!")

while True:
    print("\n1. Add New Record")
    print("2. Display Records")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_record()
    elif choice == '2':
        display_records()
    else:
        break
