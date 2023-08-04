class UserNotFoundError(Exception):

    def __str__(self):
        return 'User not found'

users = {
    "alice": {"name": "Alice Smith", "email": "alice@example.com"},
    "bob": {"name": "Bob Johnson", "email": "bob@example.com"},
    "jack": {"name": "Jack Wild", "email": "jack_wild@example.com"}
}


def get_user(username):
    if username in users:
        return users[username]["name"]
    else:
        raise UserNotFoundError


try:
    username = get_user(input())
except UserNotFoundError as e:
    print(e)
else:
    print(username)

