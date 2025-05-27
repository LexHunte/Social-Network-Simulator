"""Author: Jaydn Hunte, 001215283. Last Updated: 22/12/2022"""


class SocialNetwork:
    """Instances of this class are social network, each read in from a file"""

    def __init__(self, users, size, relationships, common_friends):
        """users is a list of names of users that make up the network and size is an integer representing the number
        of users on the network """
        self.__users = users
        self.__size = size
        self.__relationships = relationships
        self.__common_friends = common_friends

    def get_users(self):
        return self.__users

    def get_size(self):
        return self.__size

    def get_relationships(self):
        return self.__relationships

    @staticmethod
    def calculate_common_friend_count(friend_val):
        """Displays the number of common friends between every user in the network"""
        nw_common_friends = []
        for i in range(len(friend_val)):  # everything in this loop
            common_list = []
            for w in range(len(friend_val)):  # for every user in the network
                common_list.append(0)  # set each user's common friend count to 0
            for j in range(len(friend_val[i])):  # for element in users list
                for a in range(len(friend_val)):  # and for all other users lists
                    if friend_val[i][j] in friend_val[a]:  # if a users friend is in another list
                        common_list[a] += 1  # add to the common count for those two users
            nw_common_friends.append(common_list)  # add that users common list to the whole network's common count
        return nw_common_friends

    def calculate_indirect_friends(self, user_objects):
        """Displays the friends of direct friends for every user in the network"""
        indirect_network = []  # holds indirect friend lists of all network members
        for i in range(len(self.__relationships)):  # for all relationship lists
            indirect_list = []  # list of indirect friends for individual users
            for j in self.__relationships[i]:  # for each user in each friend list
                for k in range(len(user_objects)):
                    if j == user_objects[k].get_name():  # if a user is in a friend list
                        for e in user_objects[k].get_friends():
                            indirect_list.append(e)  # add each of their friends to the indirect friend list
            indirect_network.append(indirect_list)  # add each indirect friend list to the network of indirect friends

        for a in range(len(indirect_network)):  # for each indirect list
            for b in range(len(indirect_network[a])):  # and each element in each list
                if self.__users[a] in indirect_network[a]:  # if a user is in their own indirect list
                    indirect_network[a].remove(self.__users[a])  # remove them from it

        for c in self.__users:  # for each user
            for d in range(len(indirect_network)):  # and for each indirect friend list
                duplicate_count = -1  # sets duplicate count to negative
                for e in range(len(indirect_network[d])):  # for each element in each indirect friend list
                    if c == indirect_network[d][e]:  # if a user occurs in an indirect friend list
                        duplicate_count += 1  # increment duplicate count (each user should at least have one occurance)
                if duplicate_count > 0:  # if there are more than one of each user in an indirect list
                    for f in range(duplicate_count):
                        indirect_network[d].remove(c)  # remove each duplicate

        for g in range(len(self.__relationships)):  # for relationship list
            for h in self.__relationships[g]:  # and each user in each list
                if h in indirect_network[g]:  # if a direct friend is in the indirect list
                    indirect_network[g].remove(h)  # remove them for it

        return indirect_network
