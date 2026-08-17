import database.database as Database


# ==================================================
# TOTAL INCOME
# ==================================================

def calculate_total_income(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM income
        WHERE user_id = ?
    """, (user_id,))

    total = cursor.fetchone()[0]

    connection.close()

    return True, total


# ==================================================
# TOTAL EXPENSES
# ==================================================

def calculate_total_expenses(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
    """, (user_id,))

    total = cursor.fetchone()[0]

    connection.close()

    return True, total


# ==================================================
# BALANCE
# ==================================================

def calculate_balance(
    user_id
):

    _, total_income = calculate_total_income(
        user_id
    )

    _, total_expenses = calculate_total_expenses(
        user_id
    )

    balance = total_income - total_expenses

    return True, balance


# ==================================================
# DAILY EXPENSES
# ==================================================

def calculate_daily_expenses(
    user_id,
    date
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    date_string = date.strftime("%Y-%m-%d")

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        AND date LIKE ?
    """, (
        user_id,
        date_string + "%"
    ))

    total = cursor.fetchone()[0]

    connection.close()

    return True, total


# ==================================================
# WEEKLY EXPENSES
# ==================================================

def calculate_weekly_expenses(
    user_id,
    start_date,
    end_date
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        AND date >= ?
        AND date <= ?
    """, (
        user_id,
        start_date.isoformat(),
        end_date.isoformat()
    ))

    total = cursor.fetchone()[0]

    connection.close()

    return True, total


# ==================================================
# MONTHLY EXPENSES
# ==================================================

def calculate_monthly_expenses(
    user_id,
    year,
    month
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    month_string = f"{year:04d}-{month:02d}"

    cursor.execute("""
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        WHERE user_id = ?
        AND date LIKE ?
    """, (
        user_id,
        month_string + "%"
    ))

    total = cursor.fetchone()[0]

    connection.close()

    return True, total


# ==================================================
# CATEGORY TOTALS
# ==================================================

def calculate_category_totals(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            category,
            SUM(amount) AS total
        FROM expenses
        WHERE user_id = ?
        GROUP BY category
        ORDER BY total DESC
    """, (user_id,))

    rows = cursor.fetchall()

    connection.close()

    category_totals = []

    for row in rows:

        category_totals.append({
            "category": row["category"],
            "total": row["total"]
        })

    return True, category_totals