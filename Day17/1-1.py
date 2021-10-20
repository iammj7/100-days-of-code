class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'test1')
user_2 = User('002', 'test2')

user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)


# user_1 = User()
# user_1.id = '001'
# user_1.username = 'angela'
# user_1.followers = 0
# user_1.following = 0

# print(user_1.username)
# print(user_1.id)

# user_2 = User()
# user_2.id = '002'
# user_2.username = 'test'
# user_2.followers = 0
# user_2.following = 0

# print(user_2.username)
