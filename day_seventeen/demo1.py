class User:
    pass


user_1 = User()
user_1.id = '001'
user_1.username = 'Zapryan'

print(user_1.username)

user_2 = User()
user_2.id = '002'
user_2.username = 'jack'


# to make things simpler we can use constructor

class AnotherUser:

    def __init__(self):
        print('new user being created...')

another_user = AnotherUser()