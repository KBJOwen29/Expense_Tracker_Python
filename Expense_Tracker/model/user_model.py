class User:
    def __init__(self, id, username, email, password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
    
    def authenticate(self, typed_username_or_email, typed_password):
        input_login = typed_username_or_email.lower()
        stored_user = self.username.lower()
        stored_email = self.email.lower()
        stored_password = self.password
        
        if (stored_user == input_login and stored_password == typed_password) or (stored_email == input_login and stored_password == typed_password):
            return True, "Access Granted"
        else:
            return False, "Access Denied"

        