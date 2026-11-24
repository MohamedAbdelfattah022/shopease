from repositories.repository_factory import RepositoryFactory


class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get_all():
        repo = RepositoryFactory.get_repository("user")
        rows = repo.get_all()
        users = []

        for row in rows:
            user = User(
                row["id"],
                row["name"],
                row["email"]
            )

            users.append(user)

        return users

    @staticmethod
    def get_by_id(id):
        repo = RepositoryFactory.get_repository("user")
        row = repo.get_by_id(id)

        if row:
            user = User(
                row["id"],
                row["name"],
                row["email"]
            )

            return user

        return None