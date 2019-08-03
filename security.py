users = [
    {
        'id': 1,
        'username': 'patrick',
        'password': 'asdf'
    }
]

username_mapping = {'patrick': {'id': 1,
                                'username': 'patrick',
                                'password': 'asdf'}}

userid_mapping = {1:  {'id': 1,
                       'username': 'patrick',
                       'password': 'asdf'}}


def authenticate(username, password):
    user = username_mapping.get(username, None)

    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id)
