import os
import shutil

# Create File
def create_file():
    try:
        filename = input("Enter file name: ")
        with open(filename, "w") as file:
            content = input("Enter content: ")
            file.write(content)

        print("File created successfully!")

    except Exception as e:
        print("Error:", e)


# Read File
def read_file():
    try:
        filename = input("Enter file name: ")

        with open(filename, "r") as file:
            print("\nFile Content:")
            print(file.read())

    except FileNotFoundError:
        print("File not found!")


# Rename File
def rename_file():
    try:
        old_name = input("Enter current file name: ")
        new_name = input("Enter new file name: ")

        os.rename(old_name, new_name)

        print("File renamed successfully!")

    except FileNotFoundError:
        print("File not found!")


# Move File
def move_file():
    try:
        filename = input("Enter file name: ")

        backup_folder = "Backup"

        if not os.path.exists(backup_folder):
            os.mkdir(backup_folder)

        shutil.move(filename, backup_folder)

        print("File moved successfully!")

    except FileNotFoundError:
        print("File not found!")


# Delete File
def delete_file():
    try:
        filename = input("Enter file name: ")

        os.remove(filename)

        print("File deleted successfully!")

    except FileNotFoundError:
        print("File not found!")


# Main Menu
while True:

    print("\n========== SMART FILE AUTOMATION SYSTEM ==========")
    print("1. Create File")
    print("2. Read File")
    print("3. Rename File")
    print("4. Move File")
    print("5. Delete File")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_file()

    elif choice == "2":
        read_file()

    elif choice == "3":
        rename_file()

    elif choice == "4":
        move_file()

    elif choice == "5":
        delete_file()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")