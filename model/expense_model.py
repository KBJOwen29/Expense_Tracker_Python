class Expense:
    
    def __init__(
        self,
        id,
        user_id,
        amount,
        category,
        description,
        date
    ):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date