"""Author: Jaydn Hunte, 001215283. Last Updated: 15/12/2022"""


def find_users(user_list):
    """Finds every unique name in the file and stores it in a list"""
    user_set = {''}
    for item in range(len(user_list)):  # for every name in the first column of each line
        user_set.add(user_list[item])  # add the unique names to a set

    user_list = []

    for i in user_set:  # for each user in the network
        user_list.append(i)

    user_list.remove('')
    return user_list


def find_relationships(user_list, file_contents):
    """Find all relationships in the network and stores them in a 2d array"""
    network_relationships = []
    for user in range(len(user_list)):  # for every user
        user_relationships = []

        for line in range(1, len(file_contents)):  # and for every line in the network
            if len(file_contents[line].split()) > 1:  # if the user has at east one friend
                if user_list[user] == file_contents[line].split()[0]:
                    user_relationships.append(
                        file_contents[line].split()[1])  # add their friends to a list
                elif user_list[user] == file_contents[line].split()[1]:
                    user_relationships.append(
                        file_contents[line].split()[0])  # add their friends to a list
            else:
                if len(file_contents[line].split()) > 1:
                    user_relationships.append('')

        network_relationships.append(user_relationships)  # add individual user relationship list to social network list
    return network_relationships


def create_users(user_list, name_list, friend_list, User1, User2, User3):
    """Uses lists created in main to instantiate users as objects in User_Classes"""
    for user in range(len(user_list)):  # for every user in network
        if len(friend_list[user]) == 0:  # if they have no friends
            name_list[user] = User1(user_list[user])  # instantiate them as SolitaryUser
        elif len(friend_list[user]) == 1:  # or if they have one friend
            name_list[user] = User2(user_list[user], friend_list[user], '')  # instantiate them as SingleFriendUser
        elif len(friend_list[user]) > 1:  # or if they have multiple friends
            name_list[user] = User3(user_list[user], friend_list[user], '')  # instantiate them as MultiFriendUser
