import controller.user_controller as UserController
import controller.income_controller as IncomeController
import controller.expense_controller as ExpenseController
import controller.category_controller as CategoryController
import controller.report_controller as ReportController
import database.database as Database

from datetime import datetime


def main():

    # ==========================
    # INITIALIZE DATABASE
    # ==========================

    Database.initialize_database()

    while True:

        print("\n================================")
        print("   EXPENSE TRACKER - TESTING")
        print("================================")

        print("1. Register")
        print("2. Login")
        print("3. Get User")
        print("4. Update User")
        print("5. Delete User")

        print("6. Add Income")
        print("7. View Income")
        print("8. View Income Record")
        print("9. Update Income")
        print("10. Delete Income")

        print("11. Add Expense")
        print("12. View Expenses")
        print("13. View Expense Record")
        print("14. Update Expense")
        print("15. Delete Expense")
        print("16. Find Expenses by Date")
        print("17. Find Expenses by Category")

        print("18. Add Category")
        print("19. View Categories")
        print("20. Update Category")
        print("21. Delete Category")

        print("22. Financial Summary")

        print("23. Exit")

        choice = input("\nChoose an option: ")

        # ==================================================
        # REGISTER
        # ==================================================

        if choice == "1":

            username = input("Username: ")
            email = input("Email: ")
            password = input("Password: ")

            created_at = datetime.now()

            success, message = UserController.register_user(
                username,
                email,
                password,
                created_at
            )

            print("\n" + message)

        # ==================================================
        # LOGIN
        # ==================================================

        elif choice == "2":

            username_or_email = input(
                "Username or Email: "
            )

            password = input("Password: ")

            success, message = UserController.login_user(
                username_or_email,
                password
            )

            print("\n" + message)

        # ==================================================
        # GET USER
        # ==================================================

        elif choice == "3":

            user_id = int(
                input("User ID: ")
            )

            success, result = UserController.get_user(
                user_id
            )

            if success:

                print("\n===== USER INFORMATION =====")

                print("ID:", result.id)
                print("Username:", result.username)
                print("Email:", result.email)
                print("Created At:", result.created_at)

            else:

                print("\n" + result)

        # ==================================================
        # UPDATE USER
        # ==================================================

        elif choice == "4":

            user_id = int(
                input("User ID: ")
            )

            username = input(
                "New username (leave blank to keep current): "
            )

            email = input(
                "New email (leave blank to keep current): "
            )

            password = input(
                "New password (leave blank to keep current): "
            )

            username = username if username else None
            email = email if email else None
            password = password if password else None

            success, message = UserController.update_user(
                user_id,
                username,
                email,
                password
            )

            print("\n" + message)

        # ==================================================
        # DELETE USER
        # ==================================================

        elif choice == "5":

            user_id = int(
                input("User ID: ")
            )

            success, message = UserController.delete_user(
                user_id
            )

            print("\n" + message)

        # ==================================================
        # ADD INCOME
        # ==================================================

        elif choice == "6":

            user_id = int(
                input("User ID: ")
            )

            amount = float(
                input("Amount: ")
            )

            source = input(
                "Income source: "
            )

            description = input(
                "Description: "
            )

            date = datetime.now()

            success, message = IncomeController.create_income(
                user_id,
                amount,
                source,
                description,
                date
            )

            print("\n" + message)

        # ==================================================
        # VIEW INCOME
        # ==================================================

        elif choice == "7":

            user_id = int(
                input("User ID: ")
            )

            success, incomes = IncomeController.get_income(
                user_id
            )

            if success:

                if not incomes:

                    print("\nNo income records found.")

                else:

                    print("\n===== INCOME RECORDS =====")

                    for income in incomes:

                        print("\nID:", income.id)
                        print("Amount:", income.amount)
                        print("Source:", income.source)
                        print("Description:", income.description)
                        print("Date:", income.date)

            else:

                print("\n" + incomes)

        # ==================================================
        # VIEW ONE INCOME
        # ==================================================

        elif choice == "8":

            user_id = int(
                input("User ID: ")
            )

            income_id = int(
                input("Income ID: ")
            )

            success, result = IncomeController.get_income_by_id(
                user_id,
                income_id
            )

            if success:

                print("\n===== INCOME INFORMATION =====")

                print("ID:", result.id)
                print("Amount:", result.amount)
                print("Source:", result.source)
                print("Description:", result.description)
                print("Date:", result.date)

            else:

                print("\n" + result)

        # ==================================================
        # UPDATE INCOME
        # ==================================================

        elif choice == "9":

            user_id = int(
                input("User ID: ")
            )

            income_id = int(
                input("Income ID: ")
            )

            amount_input = input(
                "New amount (leave blank to keep current): "
            )

            source = input(
                "New source (leave blank to keep current): "
            )

            description = input(
                "New description (leave blank to keep current): "
            )

            date_input = input(
                "New date YYYY-MM-DD (leave blank to keep current): "
            )

            amount = (
                float(amount_input)
                if amount_input
                else None
            )

            source = (
                source
                if source
                else None
            )

            description = (
                description
                if description
                else None
            )

            if date_input:

                date = datetime.strptime(
                    date_input,
                    "%Y-%m-%d"
                )

            else:

                date = None

            success, message = IncomeController.update_income(
                user_id,
                income_id,
                amount,
                source,
                description,
                date
            )

            print("\n" + message)

        # ==================================================
        # DELETE INCOME
        # ==================================================

        elif choice == "10":

            user_id = int(
                input("User ID: ")
            )

            income_id = int(
                input("Income ID: ")
            )

            success, message = IncomeController.delete_income(
                user_id,
                income_id
            )

            print("\n" + message)

        # ==================================================
        # ADD EXPENSE
        # ==================================================

        elif choice == "11":

            user_id = int(
                input("User ID: ")
            )

            amount = float(
                input("Amount: ")
            )

            category = input(
                "Category: "
            )

            description = input(
                "Description: "
            )

            date = datetime.now()

            success, message = ExpenseController.create_expense(
                user_id,
                amount,
                category,
                description,
                date
            )

            print("\n" + message)

        # ==================================================
        # VIEW EXPENSES
        # ==================================================

        elif choice == "12":

            user_id = int(
                input("User ID: ")
            )

            success, expenses = ExpenseController.get_expenses(
                user_id
            )

            if success:

                if not expenses:

                    print("\nNo expense records found.")

                else:

                    print("\n===== EXPENSE RECORDS =====")

                    for expense in expenses:

                        print("\nID:", expense.id)
                        print("Amount:", expense.amount)
                        print("Category:", expense.category)
                        print("Description:", expense.description)
                        print("Date:", expense.date)

            else:

                print("\n" + expenses)

        # ==================================================
        # VIEW ONE EXPENSE
        # ==================================================

        elif choice == "13":

            user_id = int(
                input("User ID: ")
            )

            expense_id = int(
                input("Expense ID: ")
            )

            success, result = ExpenseController.get_expense(
                user_id,
                expense_id
            )

            if success:

                print("\n===== EXPENSE INFORMATION =====")

                print("ID:", result.id)
                print("Amount:", result.amount)
                print("Category:", result.category)
                print("Description:", result.description)
                print("Date:", result.date)

            else:

                print("\n" + result)

        # ==================================================
        # UPDATE EXPENSE
        # ==================================================

        elif choice == "14":

            user_id = int(
                input("User ID: ")
            )

            expense_id = int(
                input("Expense ID: ")
            )

            amount_input = input(
                "New amount (leave blank to keep current): "
            )

            category = input(
                "New category (leave blank to keep current): "
            )

            description = input(
                "New description (leave blank to keep current): "
            )

            date_input = input(
                "New date YYYY-MM-DD (leave blank to keep current): "
            )

            amount = (
                float(amount_input)
                if amount_input
                else None
            )

            category = (
                category
                if category
                else None
            )

            description = (
                description
                if description
                else None
            )

            if date_input:

                date = datetime.strptime(
                    date_input,
                    "%Y-%m-%d"
                )

            else:

                date = None

            success, message = ExpenseController.update_expense(
                user_id,
                expense_id,
                amount,
                category,
                description,
                date
            )

            print("\n" + message)

        # ==================================================
        # DELETE EXPENSE
        # ==================================================

        elif choice == "15":

            user_id = int(
                input("User ID: ")
            )

            expense_id = int(
                input("Expense ID: ")
            )

            success, message = ExpenseController.delete_expense(
                user_id,
                expense_id
            )

            print("\n" + message)

        # ==================================================
        # FIND EXPENSES BY DATE
        # ==================================================

        elif choice == "16":

            user_id = int(
                input("User ID: ")
            )

            date_input = input(
                "Date YYYY-MM-DD: "
            )

            try:

                date = datetime.strptime(
                    date_input,
                    "%Y-%m-%d"
                )

                success, expenses = (
                    ExpenseController.get_expenses_by_date(
                        user_id,
                        date
                    )
                )

                if not expenses:

                    print("\nNo expenses found.")

                else:

                    print("\n===== EXPENSES =====")

                    for expense in expenses:

                        print("\nID:", expense.id)
                        print("Amount:", expense.amount)
                        print("Category:", expense.category)
                        print("Description:", expense.description)
                        print("Date:", expense.date)

            except ValueError:

                print(
                    "\nInvalid date format."
                    " Please use YYYY-MM-DD."
                )

        # ==================================================
        # FIND EXPENSES BY CATEGORY
        # ==================================================

        elif choice == "17":

            user_id = int(
                input("User ID: ")
            )

            category = input(
                "Category: "
            )

            success, expenses = (
                ExpenseController.get_expenses_by_category(
                    user_id,
                    category
                )
            )

            if not expenses:

                print("\nNo expenses found.")

            else:

                print("\n===== EXPENSES =====")

                for expense in expenses:

                    print("\nID:", expense.id)
                    print("Amount:", expense.amount)
                    print("Category:", expense.category)
                    print("Description:", expense.description)
                    print("Date:", expense.date)

        # ==================================================
        # ADD CATEGORY
        # ==================================================

        elif choice == "18":

            user_id = int(
                input("User ID: ")
            )

            name = input(
                "Category name: "
            )

            success, message = (
                CategoryController.create_category(
                    user_id,
                    name
                )
            )

            print("\n" + message)

        # ==================================================
        # VIEW CATEGORIES
        # ==================================================

        elif choice == "19":

            user_id = int(
                input("User ID: ")
            )

            success, categories = (
                CategoryController.get_categories(
                    user_id
                )
            )

            if not categories:

                print("\nNo categories found.")

            else:

                print("\n===== CATEGORIES =====")

                for category in categories:

                    print(
                        category.id,
                        "-",
                        category.name
                    )

        # ==================================================
        # UPDATE CATEGORY
        # ==================================================

        elif choice == "20":

            user_id = int(
                input("User ID: ")
            )

            category_id = int(
                input("Category ID: ")
            )

            name = input(
                "New category name: "
            )

            success, message = (
                CategoryController.update_category(
                    user_id,
                    category_id,
                    name
                )
            )

            print("\n" + message)

        # ==================================================
        # DELETE CATEGORY
        # ==================================================

        elif choice == "21":

            user_id = int(
                input("User ID: ")
            )

            category_id = int(
                input("Category ID: ")
            )

            success, message = (
                CategoryController.delete_category(
                    user_id,
                    category_id
                )
            )

            print("\n" + message)

        # ==================================================
        # FINANCIAL SUMMARY
        # ==================================================

        elif choice == "22":

            user_id = int(
                input("User ID: ")
            )

            _, total_income = (
                ReportController.calculate_total_income(
                    user_id
                )
            )

            _, total_expenses = (
                ReportController.calculate_total_expenses(
                    user_id
                )
            )

            _, balance = (
                ReportController.calculate_balance(
                    user_id
                )
            )

            print("\n===== FINANCIAL SUMMARY =====")

            print(
                "Total Income:",
                total_income
            )

            print(
                "Total Expenses:",
                total_expenses
            )

            print(
                "Balance:",
                balance
            )

        # ==================================================
        # EXIT
        # ==================================================

        elif choice == "23":

            print(
                "\nExiting Expense Tracker Testing..."
            )

            break

        # ==================================================
        # INVALID OPTION
        # ==================================================

        else:

            print(
                "\nInvalid choice. Please try again."
            )


if __name__ == "__main__":
    main()