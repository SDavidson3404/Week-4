print("1. Say Hello")
print("2. Count to 5")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == "1":
    print("Hello!")
elif choice == "2":
    x = 1
    while x <= 5:
        print(x)
        x += 1
elif choice == "3":
    print("Exiting the program.")
else:
    print("Invalid choice. Please try again.")