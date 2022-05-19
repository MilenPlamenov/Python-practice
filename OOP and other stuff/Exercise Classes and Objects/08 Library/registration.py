class Registration:
    @staticmethod
    def add_user(user, library):
        if user not in library.user_records:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    @staticmethod
    def remove_user(user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            return "We could not find such user to remove!"

    @staticmethod
    def change_username(user_id, new_username, library):
        user = [u for u in library.user_records if u.user_id == user_id]

        if not user:
            return f"There is no user with id = {user_id}!"
        elif user[0].username == new_username:
            return "Please check again the provided username - it should be different than the username used so far!"
        user[0].username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"
