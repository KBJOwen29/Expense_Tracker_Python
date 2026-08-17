import database.database as Database
import model.expense_model as Expense

from datetime import datetime


# ==================================================
# CREATE EXPENSE
# ==================================================

def create_expense(
    user_id,
    amount,
    category,
    description,
    date
):

    if amount <= 0:
        return False, "Amount must be greater than zero"

    if not category.strip():
        return False, "Category cannot be empty"

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE id = ?
    """, (user_id,))

    if cursor.fetchone() is None:

        connection.close()

        return False, "User not found"

    cursor.execute("""
        INSERT INTO expenses (
            user_id,
            amount,
            category,
            description,
            date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        amount,
        category,
        description,
        date.isoformat()
    ))

    connection.commit()

    expense_id = cursor.lastrowid

    connection.close()

    return True, (
        "Expense added successfully.\n"
        f"Expense ID: {expense_id}"
    )


# ==================================================
# GET EXPENSES
# ==================================================

def get_expenses(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,))

    rows = cursor.fetchall()

    connection.close()

    expenses = []

    for row in rows:

        expense = Expense.Expense(
            row["id"],
            row["user_id"],
            row["amount"],
            row["category"],
            row["description"],
            datetime.fromisoformat(
                row["date"]
            )
        )

        expenses.append(expense)

    return True, expenses


# ==================================================
# GET ONE EXPENSE
# ==================================================

def get_expense(
    user_id,
    expense_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE id = ?
        AND user_id = ?
    """, (
        expense_id,
        user_id
    ))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return False, "Expense record not found"

    expense = Expense.Expense(
        row["id"],
        row["user_id"],
        row["amount"],
        row["category"],
        row["description"],
        datetime.fromisoformat(
            row["date"]
        )
    )

    return True, expense


# ==================================================
# UPDATE EXPENSE
# ==================================================

def update_expense(
    user_id,
    expense_id,
    amount=None,
    category=None,
    description=None,
    date=None
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE id = ?
        AND user_id = ?
    """, (
        expense_id,
        user_id
    ))

    row = cursor.fetchone()

    if row is None:

        connection.close()

        return False, "Expense record not found"

    new_amount = (
        amount
        if amount is not None
        else row["amount"]
    )

    new_category = (
        category
        if category is not None
        else row["category"]
    )

    new_description = (
        description
        if description is not None
        else row["description"]
    )

    new_date = (
        date.isoformat()
        if date is not None
        else row["date"]
    )

    if new_amount <= 0:

        connection.close()

        return False, "Amount must be greater than zero"

    if not new_category.strip():

        connection.close()

        return False, "Category cannot be empty"

    cursor.execute("""
        UPDATE expenses
        SET amount = ?,
            category = ?,
            description = ?,
            date = ?
        WHERE id = ?
        AND user_id = ?
    """, (
        new_amount,
        new_category,
        new_description,
        new_date,
        expense_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Expense updated successfully"


# ==================================================
# DELETE EXPENSE
# ==================================================

def delete_expense(
    user_id,
    expense_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM expenses
        WHERE id = ?
        AND user_id = ?
    """, (
        expense_id,
        user_id
    ))

    if cursor.fetchone() is None:

        connection.close()

        return False, "Expense record not found"

    cursor.execute("""
        DELETE FROM expenses
        WHERE id = ?
        AND user_id = ?
    """, (
        expense_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Expense deleted successfully"


# ==================================================
# GET EXPENSES BY DATE
# ==================================================

def get_expenses_by_date(
    user_id,
    date
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    date_string = date.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE user_id = ?
        AND date LIKE ?
        ORDER BY date DESC
    """, (
        user_id,
        date_string + "%"
    ))

    rows = cursor.fetchall()

    connection.close()

    expenses = []

    for row in rows:

        expense = Expense.Expense(
            row["id"],
            row["user_id"],
            row["amount"],
            row["category"],
            row["description"],
            datetime.fromisoformat(
                row["date"]
            )
        )

        expenses.append(expense)

    return True, expenses


# ==================================================
# GET EXPENSES BY CATEGORY
# ==================================================

def get_expenses_by_category(
    user_id,
    category
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM expenses
        WHERE user_id = ?
        AND LOWER(category) = LOWER(?)
        ORDER BY date DESC
    """, (
        user_id,
        category
    ))

    rows = cursor.fetchall()

    connection.close()

    expenses = []

    for row in rows:

        expense = Expense.Expense(
            row["id"],
            row["user_id"],
            row["amount"],
            row["category"],
            row["description"],
            datetime.fromisoformat(
                row["date"]
            )
        )

        expenses.append(expense)

    return True, expenses