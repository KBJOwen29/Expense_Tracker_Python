from controller.user_controller import UserController
from datetime import datetime


def main():
    user_controller = UserController()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Register")
        print("2. Login")
        print("3. Get User")
        print("4. Update User")
        print("5. Delete User")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")

            created_at = datetime.now()

            success, message = user_controller.register_user(
                username,
                email,
                password,
                created_at
            )

            print(message)

        elif choice == "2":
            username_or_email = input("Username or Email: ")
            password = input("Password: ")

            success, message = user_controller.login_user(
                username_or_email,
                password
            )

            print(message)

        elif choice == "3":
            user_id = int(input("User ID: "))

            success, result = user_controller.get_user(user_id)

            if success:
                print("\nUser Information")
                print("ID:", result.id)
                print("Username:", result.username)
                print("Email:", result.email)
                print("Created At:", result.created_at)
            else:
                print(result)

        elif choice == "4":
            user_id = int(input("User ID: "))

            username = input("New username (leave blank to keep current): ")
            email = input("New email (leave blank to keep current): ")
            password = input("New password (leave blank to keep current): ")

            username = username if username else None
            email = email if email else None
            password = password if password else None

            success, message = user_controller.update_user(
                user_id,
                username,
                email,
                password
            )

            print(message)

        elif choice == "5":
            user_id = int(input("User ID: "))

            success, message = user_controller.delete_user(user_id)

            print(message)

        elif choice == "6":
            print("Exiting Expense Tracker...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()