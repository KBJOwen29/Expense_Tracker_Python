from typing import List, Optional, Dict, Tuple
from model.user_model import User

# In-memory store for users (simple, non-persistent)
_users: List[User] = []
_next_id = 1

def _get_next_id() -> int:
	global _next_id
	nid = _next_id
	_next_id += 1
	return nid

def _user_to_dict(user: User) -> Dict:
	return {"id": user.id, "username": user.username, "email": user.email}

def register_user(username: str, email: str, password: str) -> Tuple[bool, str, Optional[Dict]]:
	"""Register a new user.

	Returns (success, message, user_dict).
	"""
	# simple uniqueness checks (case-insensitive)
	for u in _users:
		if u.username.lower() == username.lower():
			return False, "Username already exists", None
		if u.email.lower() == email.lower():
			return False, "Email already registered", None

	user = User(_get_next_id(), username, email, password)
	_users.append(user)
	return True, "User registered", _user_to_dict(user)

def login_user(typed_username_or_email: str, password: str) -> Tuple[bool, str, Optional[Dict]]:
	"""Authenticate a user by username or email and password.

	Returns (success, message, user_dict).
	"""
	for u in _users:
		ok, msg = u.authenticate(typed_username_or_email, password)
		if ok:
			return True, "Login successful", _user_to_dict(u)

	return False, "Invalid credentials", None

def get_user(user_id: Optional[int] = None, username: Optional[str] = None, email: Optional[str] = None):
	"""Retrieve a user by id, username, or email. If none provided, returns all users."""
	if user_id is None and username is None and email is None:
		return [_user_to_dict(u) for u in _users]

	for u in _users:
		if user_id is not None and u.id == user_id:
			return _user_to_dict(u)
		if username is not None and u.username.lower() == username.lower():
			return _user_to_dict(u)
		if email is not None and u.email.lower() == email.lower():
			return _user_to_dict(u)

	return None

def update_user(user_id: int, username: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None) -> Tuple[bool, str, Optional[Dict]]:
	"""Update fields of a user. Returns (success, message, user_dict)."""
	for u in _users:
		if u.id == user_id:
			# check uniqueness for username/email
			if username and any(x.username.lower() == username.lower() and x.id != user_id for x in _users):
				return False, "Username already taken", None
			if email and any(x.email.lower() == email.lower() and x.id != user_id for x in _users):
				return False, "Email already in use", None

			if username:
				u.username = username
			if email:
				u.email = email
			if password:
				u.password = password

			return True, "User updated", _user_to_dict(u)

	return False, "User not found", None

def delete_user(user_id: int) -> Tuple[bool, str]:
	"""Delete a user by id. Returns (success, message)."""
	global _users
	for i, u in enumerate(_users):
		if u.id == user_id:
			_users.pop(i)
			return True, "User deleted"

	return False, "User not found"

__all__ = [
	"register_user",
	"login_user",
	"get_user",
	"update_user",
	"delete_user",
]

