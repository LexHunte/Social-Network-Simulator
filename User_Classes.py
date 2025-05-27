"""Author: Jaydn Hunte, 001215283. Last Updated: 22/12/2022"""


class User:
    """Abstract super class for  SolitaryUser, SingleFriendUser and MultiFriendUser"""

    def __init__(self, name, friends, recommended_friend):
        """Constructor method for user class."""
        self._instances.append(self)
        self.__username = name
        self.__friends = friends
        self.__recommended_friend = recommended_friend

    def get_friends(self):
        """Different implementation for each subclass"""
        raise NotImplementedError("Cannot call abstract method without implementation")

    def get_friend_count(self):
        """Different implementation for each subclass"""
        raise NotImplementedError("Cannot call abstract method without implementation")

    def get_recommendation(self):
        """Different implementation for each subclass"""
        raise NotImplementedError("Cannot call abstract method without implementation")

    def get_instances(self):
        return self._instances

    def get_name(self):
        return self.__name


class SolitaryUser(User):
    """Child class for User class, instances are users with no friends"""
    _instances = []

    def __init__(self, name):
        """Doesn't have friends or recommended_friend attributes"""
        self._instances.append(self)
        self.__name = name

    def get_friends(self):
        """All instances of SolitaryUser will never have friends"""
        return 'This user has no friends.'

    def get_friend_count(self):
        """All instances of SolitaryUser will never have friends"""
        return 0

    def get_recommendation(self, a, b, c, d):
        """Cannot recommend a friend for a user with no friends"""
        pass

    def get_name(self):
        return self.__name


class SingleFriendUser(User):
    """Child class for User class, instances only have one friend"""
    _instances = []

    def __init__(self, name, friends, recommended_friend):
        self._instances.append(self)
        super().__init__(name, friends, recommended_friend)
        self.__name = name
        self.__friends = friends
        self.__recommended_friend = recommended_friend

    def get_friends(self):
        return self.__friends

    def get_friend_count(self):
        return 1

    def get_recommendation(self, position, users, friend_lists, common_friends):
        """Recommends a friend for a user based on the number of friends they have in common"""
        common_check_zero = 0  # checks how many zeros are in a users common friend count list
        for n in range(len(common_friends[position])):  # for the length of that list
            if common_friends[position][n] == 0:  # if there is a zero in the current position
                common_check_zero += 1  # add to a counter

        if common_check_zero == len(common_friends[position]) - 1:  # if all positions but one are zero, they
            # don't have a recommended friend
            return None

        highest_count = 0  # highest number of common friends between specified user and other users
        for i in range(len(common_friends[position])):  # for common friend counts of this user
            if common_friends[position][i] > highest_count and position != i:  # if greater count found but only if
                # the count isn't their own
                highest_count = common_friends[position][i]  # update highest_count to the greater value

        for j in range(len(common_friends[position])):  # for each common counter
            if highest_count == common_friends[position][j] and j != position and users[j] not in \
                    friend_lists[position]:  # find the highest count in the list
                # again
                return j  # return its position

    def get_name(self):
        return self.__name


class MultiFriendUser(User):
    """Child class for User class, instances have more than 1 friend"""
    _instances = []

    def __init__(self, name, friends, recommended_friend):
        self._instances.append(self)
        super().__init__(name, friends, recommended_friend)
        self.__name = name
        self.__friends = friends
        self.__recommended_friend = recommended_friend

    def get_friends(self):
        return self.__friends

    def get_friend_count(self):
        return len(self.__friends)

    def get_recommendation(self, position, users, friend_lists, common_friends):
        """Returns the index of the highest common friend count in a user's list"""
        highest_count = 0  # highest number of common friends between specified user and other users
        for i in range(len(common_friends[position])):  # for common friend counts of this user
            if common_friends[position][i] > highest_count and position != i:  # if greater count found but only if
                # the count isn't their own
                highest_count = common_friends[position][i]  # update highest_count to the greater value

        for j in range(len(common_friends[position])):  # for each common counter
            if highest_count == common_friends[position][j] and j != position and users[j] not in \
                    friend_lists[position]:  # find the highest count in the list
                # again
                return j  # return its position

    def get_name(self):
        return self.__name
