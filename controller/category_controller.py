import database.database as Database
import model.category_model as Category


# ==================================================
# CREATE CATEGORY
# ==================================================

def create_category(
    user_id,
    name
):

    if not name.strip():
        return False, "Category name cannot be empty"

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
        SELECT id
        FROM categories
        WHERE user_id = ?
        AND LOWER(name) = LOWER(?)
    """, (
        user_id,
        name
    ))

    if cursor.fetchone() is not None:

        connection.close()

        return False, "Category already exists"

    cursor.execute("""
        INSERT INTO categories (
            name,
            user_id
        )
        VALUES (?, ?)
    """, (
        name,
        user_id
    ))

    connection.commit()

    category_id = cursor.lastrowid

    connection.close()

    return True, (
        "Category created successfully.\n"
        f"Category ID: {category_id}"
    )


# ==================================================
# GET CATEGORIES
# ==================================================

def get_categories(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM categories
        WHERE user_id = ?
        ORDER BY name
    """, (user_id,))

    rows = cursor.fetchall()

    connection.close()

    categories = []

    for row in rows:

        category = Category.Category(
            row["id"],
            row["name"],
            row["user_id"]
        )

        categories.append(category)

    return True, categories


# ==================================================
# UPDATE CATEGORY
# ==================================================

def update_category(
    user_id,
    category_id,
    name
):

    if not name.strip():
        return False, "Category name cannot be empty"

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM categories
        WHERE id = ?
        AND user_id = ?
    """, (
        category_id,
        user_id
    ))

    if cursor.fetchone() is None:

        connection.close()

        return False, "Category not found"

    cursor.execute("""
        SELECT id
        FROM categories
        WHERE user_id = ?
        AND LOWER(name) = LOWER(?)
        AND id != ?
    """, (
        user_id,
        name,
        category_id
    ))

    if cursor.fetchone() is not None:

        connection.close()

        return False, "Category already exists"

    cursor.execute("""
        UPDATE categories
        SET name = ?
        WHERE id = ?
        AND user_id = ?
    """, (
        name,
        category_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Category updated successfully"


# ==================================================
# DELETE CATEGORY
# ==================================================

def delete_category(
    user_id,
    category_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM categories
        WHERE id = ?
        AND user_id = ?
    """, (
        category_id,
        user_id
    ))

    if cursor.fetchone() is None:

        connection.close()

        return False, "Category not found"

    cursor.execute("""
        DELETE FROM categories
        WHERE id = ?
        AND user_id = ?
    """, (
        category_id,
        user_id
    ))

    connection.commit()

    connection.close()

    return True, "Category deleted successfully"