
# we can store test data in this module like users

users = [{'name': 'invalid_user', 'email': 'invalidUser@test.com', 'password': 'qwert1235'},
          {'name': 'valid_user', 'email': 'tetra-support@strikersoft.com', 'password': '12345+'}
          ]

def get_user(name):
    return (user for user in users if user['name'] == name).__next__()