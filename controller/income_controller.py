import database.database as Database
import model.income_model as Income

from datetime import datetime


# ==================================================
# CREATE INCOME
# ==================================================

def create_income(
    user_id,
    amount,
    source,
    description,
    date
):

    if amount <= 0:
        return False, "Amount must be greater than zero"

    if not source.strip():
        return False, "Income source cannot be empty"

    connection = Database.get_connection()

    cursor = connection.cursor()

    # Make sure user exists
    cursor.execute("""
        SELECT id
        FROM users
        WHERE id = ?
    """, (user_id,))

    if cursor.fetchone() is None:

        connection.close()

        return False, "User not found"

    cursor.execute("""
        INSERT INTO income (
            user_id,
            amount,
            source,
            description,
            date
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        user_id,
        amount,
        source,
        description,
        date.isoformat()
    ))

    connection.commit()

    income_id = cursor.lastrowid

    connection.close()

    return True, (
        "Income added successfully.\n"
        f"Income ID: {income_id}"
    )


# ==================================================
# GET ALL INCOME
# ==================================================

def get_income(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM income
        WHERE user_id = ?
        ORDER BY date DESC
    """, (user_id,))

    rows = cursor.fetchall()

    connection.close()

    incomes = []

    for row in rows:

        income = Income.Income(
            row["id"],
            row["user_id"],
            row["amount"],
            row["source"],
            row["description"],
            datetime.fromisoformat(
                row["date"]
            )
        )

        incomes.append(income)

    return True, incomes


# ==================================================
# GET ONE INCOME
# ==================================================

def get_income_by_id(
    user_id,
    income_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM income
        WHERE id = ?
        AND user_id = ?
    """, (
        income_id,
        user_id
    ))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return False, "Income record not found"

    income = Income.Income(
        row["id"],
        row["user_id"],
        row["amount"],
        row["source"],
        row["description"],
        datetime.fromisoformat(
            row["date"]
        )
    )

    return True, income


# ==================================================
# UPDATE INCOME
# ==================================================

def update_income(
    user_id,
    income_id,
    amount=None,
    source=None,
    description=None,
    date=None
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM income
        WHERE id = ?
        AND user_id = ?
    """, (
        income_id,
        user_id
    ))

    row = cursor.fetchone()

    if row is None:

        connection.close()

        return False, "Income record not found"

    new_amount = (
        amount
        if amount is not None
        else row["amount"]
    )

    new_source = (
        source
        if source is not None
        else row["source"]
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

    if not new_source.strip():

        connection.close()

        return False, "Income source cannot be empty"

    cursor.execute("""
        UPDATE income
        SET amount = ?,
            source = ?,
            description = ?,
            date = ?
        WHERE id = ?
        AND user_id = ?
    """, (
        new_amount,
        new_source,
        new_description,
        new_date,
        income_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Income updated successfully"


# ==================================================
# DELETE INCOME
# ==================================================

def delete_income(
    user_id,
    income_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM income
        WHERE id = ?
        AND user_id = ?
    """, (
        income_id,
        user_id
    ))

    if cursor.fetchone() is None:

        connection.close()

        return False, "Income record not found"

    cursor.execute("""
        DELETE FROM income
        WHERE id = ?
        AND user_id = ?
    """, (
        income_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Income deleted successfully"