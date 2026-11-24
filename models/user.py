class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get_all():
        return [
            User(1, "Ahmed Mohamed", "john@example.com"),
            User(2, "Nabil Sherif", "jane@example.com"),
        ]

    @staticmethod
    def get_by_id(id):
        for user in User.get_all():
            if user.id == id:
                return user
        return None
