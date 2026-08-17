import database.database as Database
import model.user_model as User

from datetime import datetime


# ==================================================
# REGISTER USER
# ==================================================

def register_user(
    username,
    email,
    password,
    created_at
):

    if not username.strip():
        return False, "Username cannot be empty"

    if not email.strip():
        return False, "Email cannot be empty"

    if not password:
        return False, "Password cannot be empty"

    connection = Database.get_connection()

    cursor = connection.cursor()

    try:

        cursor.execute("""
            INSERT INTO users (
                username,
                email,
                password,
                created_at
            )
            VALUES (?, ?, ?, ?)
        """, (
            username,
            email,
            password,
            created_at.isoformat()
        ))

        connection.commit()

        user_id = cursor.lastrowid

        return True, (
            "User registered successfully.\n"
            f"Your User ID is: {user_id}"
        )

    except Exception as error:

        connection.rollback()

        error_message = str(error).lower()

        if "username" in error_message:
            return False, "Username already exists"

        if "email" in error_message:
            return False, "Email already exists"

        return False, "Registration failed"

    finally:

        connection.close()


# ==================================================
# LOGIN USER
# ==================================================

def login_user(
    username_or_email,
    password
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE LOWER(username) = LOWER(?)
        OR LOWER(email) = LOWER(?)
    """, (
        username_or_email,
        username_or_email
    ))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return False, "Access Denied"

    if row["password"] != password:
        return False, "Access Denied"

    return True, "Access Granted"


# ==================================================
# GET USER BY LOGIN
# ==================================================

def get_user_by_login(
    username_or_email
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE LOWER(username) = LOWER(?)
        OR LOWER(email) = LOWER(?)
    """, (
        username_or_email,
        username_or_email
    ))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return False, "User not found"

    user = User.User(
        row["id"],
        row["username"],
        row["email"],
        row["password"],
        datetime.fromisoformat(
            row["created_at"]
        )
    )

    return True, user


# ==================================================
# GET USER
# ==================================================

def get_user(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return False, "User not found"

    user = User.User(
        row["id"],
        row["username"],
        row["email"],
        row["password"],
        datetime.fromisoformat(
            row["created_at"]
        )
    )

    return True, user


# ==================================================
# UPDATE USER
# ==================================================

def update_user(
    user_id,
    username=None,
    email=None,
    password=None
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM users
        WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()

    if row is None:

        connection.close()

        return False, "User not found"

    new_username = (
        username
        if username is not None
        else row["username"]
    )

    new_email = (
        email
        if email is not None
        else row["email"]
    )

    new_password = (
        password
        if password is not None
        else row["password"]
    )

    try:

        cursor.execute("""
            UPDATE users
            SET username = ?,
                email = ?,
                password = ?
            WHERE id = ?
        """, (
            new_username,
            new_email,
            new_password,
            user_id
        ))

        connection.commit()

        return True, "User updated successfully"

    except Exception as error:

        connection.rollback()

        error_message = str(error).lower()

        if "username" in error_message:
            return False, "Username already exists"

        if "email" in error_message:
            return False, "Email already exists"

        return False, "Failed to update user"

    finally:

        connection.close()


# ==================================================
# DELETE USER
# ==================================================

def delete_user(
    user_id
):

    connection = Database.get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM users
        WHERE id = ?
    """, (user_id,))

    row = cursor.fetchone()

    if row is None:

        connection.close()

        return False, "User not found"

    try:

        cursor.execute("""
            DELETE FROM users
            WHERE id = ?
        """, (user_id,))

        connection.commit()

        return True, "User deleted successfully"

    except Exception:

        connection.rollback()

        return False, "Failed to delete user"

    finally:

        connection.close()