def add_student():
    with open("students.txt", "a") as file:
        sid = input("Enter ID: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(f"{sid},{name},{marks}\n")
    print("✅ Student Added Successfully\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            data = file.readlines()
            if not data:
                print("No records found.\n")
                return
            
            print("\n--- Student Records ---")
            for line in data:
                sid, name, marks = line.strip().split(",")
                print(f"ID: {sid}, Name: {name}, Marks: {marks}")
            print()
    except FileNotFoundError:
        print("File not found.\n")


def search_student():
    sid_search = input("Enter ID to search: ")
    found = False
    
    try:
        with open("students.txt", "r") as file:
            for line in file:
                sid, name, marks = line.strip().split(",")
                if sid == sid_search:
                    print(f"✅ Found: {sid}, {name}, {marks}\n")
                    found = True
                    break
        
        if not found:
            print("❌ Student not found\n")
    
    except FileNotFoundError:
        print("File not found.\n")


def delete_student():
    sid_delete = input("Enter ID to delete: ")
    lines = []
    found = False

    try:
        with open("students.txt", "r") as file:
            lines = file.readlines()

        with open("students.txt", "w") as file:
            for line in lines:
                sid, name, marks = line.strip().split(",")
                if sid != sid_delete:
                    file.write(line)
                else:
                    found = True

        if found:
            print("🗑️ Student Deleted Successfully\n")
        else:
            print("❌ Student not found\n")

    except FileNotFoundError:
        print("File not found.\n")


# 🔹 Main Menu
while True:
    print("===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")