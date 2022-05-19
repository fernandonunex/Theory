import users as usr


if __name__ == '__main__':
    me = usr.Admin('Fer', 'nunx')

    me.describe_user()
    me.greet_user()
    me.privileges.show_privileges()