import database.database as Database

import controller.user_controller as UserController
import controller.income_controller as IncomeController
import controller.expense_controller as ExpenseController
import controller.category_controller as CategoryController
import controller.report_controller as ReportController

from datetime import datetime


def main():

    Database.initialize_database()

    logged_in = False

    current_user_id = None
    current_username = None

    while True:

        # ==================================================
        # LOGGED OUT MENU
        # ==================================================

        if not logged_in:

            print("\n===== EXPENSE TRACKER =====")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose an option: ")

            # ==================================================
            # REGISTER
            # ==================================================

            if choice == "1":

                username = input("Username: ")
                email = input("Email: ")
                password = input("Password: ")

                created_at = datetime.now()

                success, message = (
                    UserController.register_user(
                        username,
                        email,
                        password,
                        created_at
                    )
                )

                print("\n" + message)

            # ==================================================
            # LOGIN
            # ==================================================

            elif choice == "2":

                username_or_email = input(
                    "Username or Email: "
                )

                password = input(
                    "Password: "
                )

                success, message = (
                    UserController.login_user(
                        username_or_email,
                        password
                    )
                )

                print("\n" + message)

                if success:

                    success, user = (
                        UserController.get_user_by_login(
                            username_or_email
                        )
                    )

                    if success:

                        logged_in = True

                        current_user_id = user.id

                        current_username = (
                            user.username
                        )

                        print(
                            f"Welcome, "
                            f"{current_username}!"
                        )

                        print(
                            f"Logged in User ID: "
                            f"{current_user_id}"
                        )

            # ==================================================
            # EXIT
            # ==================================================

            elif choice == "3":

                print(
                    "Exiting Expense Tracker..."
                )

                break

            else:

                print(
                    "Invalid choice. Please try again."
                )

        # ==================================================
        # LOGGED IN MENU
        # ==================================================

        else:

            print("\n===== EXPENSE TRACKER =====")

            print(
                f"Logged in as: "
                f"{current_username}"
            )

            print(
                f"User ID: "
                f"{current_user_id}"
            )

            print("\n----- ACCOUNT -----")
            print("1. Get User")
            print("2. Update User")
            print("3. Delete User")

            print("\n----- INCOME -----")
            print("4. Add Income")
            print("5. View Income")
            print("6. View Income Record")
            print("7. Update Income")
            print("8. Delete Income")

            print("\n----- EXPENSE -----")
            print("9. Add Expense")
            print("10. View Expenses")
            print("11. View Expense Record")
            print("12. Update Expense")
            print("13. Delete Expense")
            print("14. Find Expenses by Date")
            print("15. Find Expenses by Category")

            print("\n----- CATEGORY -----")
            print("16. Add Category")
            print("17. View Categories")
            print("18. Update Category")
            print("19. Delete Category")

            print("\n----- REPORTS -----")
            print("20. Financial Summary")
            print("21. Daily Expense")
            print("22. Weekly Expense")
            print("23. Monthly Expense")
            print("24. Category Totals")

            print("\n25. Logout")

            choice = input("Choose an option: ")

            # ==================================================
            # GET USER
            # ==================================================

            if choice == "1":

                success, result = (
                    UserController.get_user(
                        current_user_id
                    )
                )

                if success:

                    print(
                        "\n===== USER INFORMATION ====="
                    )

                    print(
                        "ID:",
                        result.id
                    )

                    print(
                        "Username:",
                        result.username
                    )

                    print(
                        "Email:",
                        result.email
                    )

                    print(
                        "Created At:",
                        result.created_at
                    )

                else:

                    print(result)

            # ==================================================
            # UPDATE USER
            # ==================================================

            elif choice == "2":

                username = input(
                    "New username "
                    "(leave blank to keep current): "
                )

                email = input(
                    "New email "
                    "(leave blank to keep current): "
                )

                password = input(
                    "New password "
                    "(leave blank to keep current): "
                )

                username = (
                    username
                    if username
                    else None
                )

                email = (
                    email
                    if email
                    else None
                )

                password = (
                    password
                    if password
                    else None
                )

                success, message = (
                    UserController.update_user(
                        current_user_id,
                        username,
                        email,
                        password
                    )
                )

                print(message)

                if success and username is not None:

                    current_username = username

            # ==================================================
            # DELETE USER
            # ==================================================

            elif choice == "3":

                confirmation = input(
                    "Delete your account? (yes/no): "
                )

                if confirmation.lower() == "yes":

                    success, message = (
                        UserController.delete_user(
                            current_user_id
                        )
                    )

                    print(message)

                    if success:

                        logged_in = False
                        current_user_id = None
                        current_username = None

            # ==================================================
            # ADD INCOME
            # ==================================================

            elif choice == "4":

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

                success, message = (
                    IncomeController.create_income(
                        current_user_id,
                        amount,
                        source,
                        description,
                        date
                    )
                )

                print(message)

            # ==================================================
            # VIEW INCOME
            # ==================================================

            elif choice == "5":

                success, incomes = (
                    IncomeController.get_income(
                        current_user_id
                    )
                )

                if success:

                    if not incomes:

                        print(
                            "\nNo income records found."
                        )

                    else:

                        print(
                            "\n===== INCOME RECORDS ====="
                        )

                        for income in incomes:

                            print(
                                "\nID:",
                                income.id
                            )

                            print(
                                "Amount:",
                                income.amount
                            )

                            print(
                                "Source:",
                                income.source
                            )

                            print(
                                "Description:",
                                income.description
                            )

                            print(
                                "Date:",
                                income.date
                            )

                else:

                    print(incomes)

            # ==================================================
            # VIEW ONE INCOME
            # ==================================================

            elif choice == "6":

                income_id = int(
                    input("Income ID: ")
                )

                success, result = (
                    IncomeController.get_income_by_id(
                        current_user_id,
                        income_id
                    )
                )

                if success:

                    print(
                        "\n===== INCOME INFORMATION ====="
                    )

                    print(
                        "ID:",
                        result.id
                    )

                    print(
                        "Amount:",
                        result.amount
                    )

                    print(
                        "Source:",
                        result.source
                    )

                    print(
                        "Description:",
                        result.description
                    )

                    print(
                        "Date:",
                        result.date
                    )

                else:

                    print(result)

            # ==================================================
            # UPDATE INCOME
            # ==================================================

            elif choice == "7":

                income_id = int(
                    input("Income ID: ")
                )

                amount_input = input(
                    "New amount "
                    "(leave blank to keep current): "
                )

                source = input(
                    "New source "
                    "(leave blank to keep current): "
                )

                description = input(
                    "New description "
                    "(leave blank to keep current): "
                )

                date_input = input(
                    "New date YYYY-MM-DD "
                    "(leave blank to keep current): "
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

                success, message = (
                    IncomeController.update_income(
                        current_user_id,
                        income_id,
                        amount,
                        source,
                        description,
                        date
                    )
                )

                print(message)

            # ==================================================
            # DELETE INCOME
            # ==================================================

            elif choice == "8":

                income_id = int(
                    input("Income ID: ")
                )

                success, message = (
                    IncomeController.delete_income(
                        current_user_id,
                        income_id
                    )
                )

                print(message)

            # ==================================================
            # ADD EXPENSE
            # ==================================================

            elif choice == "9":

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

                success, message = (
                    ExpenseController.create_expense(
                        current_user_id,
                        amount,
                        category,
                        description,
                        date
                    )
                )

                print(message)

            # ==================================================
            # VIEW EXPENSES
            # ==================================================

            elif choice == "10":

                success, expenses = (
                    ExpenseController.get_expenses(
                        current_user_id
                    )
                )

                if success:

                    if not expenses:

                        print(
                            "\nNo expense records found."
                        )

                    else:

                        print(
                            "\n===== EXPENSE RECORDS ====="
                        )

                        for expense in expenses:

                            print(
                                "\nID:",
                                expense.id
                            )

                            print(
                                "Amount:",
                                expense.amount
                            )

                            print(
                                "Category:",
                                expense.category
                            )

                            print(
                                "Description:",
                                expense.description
                            )

                            print(
                                "Date:",
                                expense.date
                            )

                else:

                    print(expenses)

            # ==================================================
            # VIEW ONE EXPENSE
            # ==================================================

            elif choice == "11":

                expense_id = int(
                    input("Expense ID: ")
                )

                success, result = (
                    ExpenseController.get_expense(
                        current_user_id,
                        expense_id
                    )
                )

                if success:

                    print(
                        "\n===== EXPENSE INFORMATION ====="
                    )

                    print(
                        "ID:",
                        result.id
                    )

                    print(
                        "Amount:",
                        result.amount
                    )

                    print(
                        "Category:",
                        result.category
                    )

                    print(
                        "Description:",
                        result.description
                    )

                    print(
                        "Date:",
                        result.date
                    )

                else:

                    print(result)

            # ==================================================
            # UPDATE EXPENSE
            # ==================================================

            elif choice == "12":

                expense_id = int(
                    input("Expense ID: ")
                )

                amount_input = input(
                    "New amount "
                    "(leave blank to keep current): "
                )

                category = input(
                    "New category "
                    "(leave blank to keep current): "
                )

                description = input(
                    "New description "
                    "(leave blank to keep current): "
                )

                date_input = input(
                    "New date YYYY-MM-DD "
                    "(leave blank to keep current): "
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

                success, message = (
                    ExpenseController.update_expense(
                        current_user_id,
                        expense_id,
                        amount,
                        category,
                        description,
                        date
                    )
                )

                print(message)

            # ==================================================
            # DELETE EXPENSE
            # ==================================================

            elif choice == "13":

                expense_id = int(
                    input("Expense ID: ")
                )

                success, message = (
                    ExpenseController.delete_expense(
                        current_user_id,
                        expense_id
                    )
                )

                print(message)

            # ==================================================
            # EXPENSES BY DATE
            # ==================================================

            elif choice == "14":

                date_input = input(
                    "Date YYYY-MM-DD: "
                )

                date = datetime.strptime(
                    date_input,
                    "%Y-%m-%d"
                )

                success, expenses = (
                    ExpenseController.get_expenses_by_date(
                        current_user_id,
                        date
                    )
                )

                if not expenses:

                    print(
                        "\nNo expenses found."
                    )

                else:

                    print(
                        "\n===== EXPENSES ====="
                    )

                    for expense in expenses:

                        print(
                            "\nID:",
                            expense.id
                        )

                        print(
                            "Amount:",
                            expense.amount
                        )

                        print(
                            "Category:",
                            expense.category
                        )

                        print(
                            "Description:",
                            expense.description
                        )

                        print(
                            "Date:",
                            expense.date
                        )

            # ==================================================
            # EXPENSES BY CATEGORY
            # ==================================================

            elif choice == "15":

                category = input(
                    "Category: "
                )

                success, expenses = (
                    ExpenseController.get_expenses_by_category(
                        current_user_id,
                        category
                    )
                )

                if not expenses:

                    print(
                        "\nNo expenses found."
                    )

                else:

                    print(
                        "\n===== EXPENSES ====="
                    )

                    for expense in expenses:

                        print(
                            "\nID:",
                            expense.id
                        )

                        print(
                            "Amount:",
                            expense.amount
                        )

                        print(
                            "Category:",
                            expense.category
                        )

                        print(
                            "Description:",
                            expense.description
                        )

                        print(
                            "Date:",
                            expense.date
                        )

            # ==================================================
            # ADD CATEGORY
            # ==================================================

            elif choice == "16":

                name = input(
                    "Category name: "
                )

                success, message = (
                    CategoryController.create_category(
                        current_user_id,
                        name
                    )
                )

                print(message)

            # ==================================================
            # VIEW CATEGORIES
            # ==================================================

            elif choice == "17":

                success, categories = (
                    CategoryController.get_categories(
                        current_user_id
                    )
                )

                if not categories:

                    print(
                        "\nNo categories found."
                    )

                else:

                    print(
                        "\n===== CATEGORIES ====="
                    )

                    for category in categories:

                        print(
                            category.id,
                            "-",
                            category.name
                        )

            # ==================================================
            # UPDATE CATEGORY
            # ==================================================

            elif choice == "18":

                category_id = int(
                    input("Category ID: ")
                )

                name = input(
                    "New category name: "
                )

                success, message = (
                    CategoryController.update_category(
                        current_user_id,
                        category_id,
                        name
                    )
                )

                print(message)

            # ==================================================
            # DELETE CATEGORY
            # ==================================================

            elif choice == "19":

                category_id = int(
                    input("Category ID: ")
                )

                success, message = (
                    CategoryController.delete_category(
                        current_user_id,
                        category_id
                    )
                )

                print(message)

            # ==================================================
            # FINANCIAL SUMMARY
            # ==================================================

            elif choice == "20":

                _, total_income = (
                    ReportController.calculate_total_income(
                        current_user_id
                    )
                )

                _, total_expenses = (
                    ReportController.calculate_total_expenses(
                        current_user_id
                    )
                )

                _, balance = (
                    ReportController.calculate_balance(
                        current_user_id
                    )
                )

                print(
                    "\n===== FINANCIAL SUMMARY ====="
                )

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
            # DAILY EXPENSE
            # ==================================================

            elif choice == "21":

                date_input = input(
                    "Date YYYY-MM-DD: "
                )

                date = datetime.strptime(
                    date_input,
                    "%Y-%m-%d"
                )

                _, total = (
                    ReportController.calculate_daily_expenses(
                        current_user_id,
                        date
                    )
                )

                print(
                    f"\nTotal expenses for "
                    f"{date_input}: {total}"
                )

            # ==================================================
            # WEEKLY EXPENSE
            # ==================================================

            elif choice == "22":

                start_input = input(
                    "Start date YYYY-MM-DD: "
                )

                end_input = input(
                    "End date YYYY-MM-DD: "
                )

                start_date = datetime.strptime(
                    start_input,
                    "%Y-%m-%d"
                )

                end_date = datetime.strptime(
                    end_input,
                    "%Y-%m-%d"
                )

                _, total = (
                    ReportController.calculate_weekly_expenses(
                        current_user_id,
                        start_date,
                        end_date
                    )
                )

                print(
                    "\nTotal expenses:"
                    f" {total}"
                )

            # ==================================================
            # MONTHLY EXPENSE
            # ==================================================

            elif choice == "23":

                year = int(
                    input("Year: ")
                )

                month = int(
                    input("Month: ")
                )

                _, total = (
                    ReportController.calculate_monthly_expenses(
                        current_user_id,
                        year,
                        month
                    )
                )

                print(
                    "\nTotal monthly expenses:",
                    total
                )

            # ==================================================
            # CATEGORY TOTALS
            # ==================================================

            elif choice == "24":

                _, totals = (
                    ReportController.calculate_category_totals(
                        current_user_id
                    )
                )

                print(
                    "\n===== CATEGORY TOTALS ====="
                )

                if not totals:

                    print(
                        "No expense data found."
                    )

                else:

                    for item in totals:

                        print(
                            item["category"],
                            ":",
                            item["total"]
                        )

            # ==================================================
            # LOGOUT
            # ==================================================

            elif choice == "25":

                print(
                    f"Goodbye, "
                    f"{current_username}!"
                )

                logged_in = False

                current_user_id = None

                current_username = None

            else:

                print(
                    "Invalid choice. Please try again."
                )


if __name__ == "__main__":
    main()