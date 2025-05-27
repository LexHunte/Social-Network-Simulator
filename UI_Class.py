"""Author: Jaydn Hunte, 001215283. Last Updated: 22/12/2022"""

import time


class UI:

    @staticmethod
    def welcome():
        """Outputs welcome message"""
        print("Welcome to the Social Network Simulator!")  # welcome message
        time.sleep(0.3)

    @staticmethod
    def file_input():
        """Gets input for filename or exit"""
        time.sleep(0.2)
        file_id = input("\nPlease enter the filename to continue or enter 'n' to exit: ")
        if file_id == 'n':
            return False
        else:
            return file_id

    @staticmethod
    def confirm_file():
        """Calls file_input and checks if name exists, if not, outputs appropriate message"""
        filename_valid = False
        while not filename_valid:  # keeps requesting a filename that can be found
            try:
                file_id = UI.file_input()  # takes filename as input
                opened_file = open(file_id, "r")  # opens file in read mode
                if not file_id:  # if the user chooses to exit the program
                    opened_file.close()  # closes the file
                    quit()  # exits the program
            except FileNotFoundError:  # if the filename is not found
                print('.', end=''), time.sleep(0.5), print('.', end=''), time.sleep(0.5), print('.'), time.sleep(0.5)
                time.sleep(0.5), print("Cannot find this file, try a different one."), time.sleep(0.2)  # error msg
            else:
                filename_valid = True
        return opened_file  # only returns a found filename to the main program

    @staticmethod
    def action_input():
        """Presents options to user and returns their input"""
        print("\nWhat would you like to do?")
        time.sleep(0.1)
        print("1: Display the Social Network")
        print("2: Display a Common Friend Count")
        print("3: Get a Friend Recommendation")
        print("4: Display a User's Friends")
        print("5: Get a User's Friend Count")
        print("6: Display All Indirect Friends")
        print("7: Display the Users with the Least Friends")
        print("\n")
        time.sleep(0.2)

        choice_invalid = True

        while choice_invalid:
            choice = input("Please enter a corresponding number to select an option or type 'c' to change file: ")
            if choice == '1':
                choice_invalid = False
                print('\n')
                return 1
            elif choice == '2':
                choice_invalid = False
                print('\n')
                return 2
            elif choice == '3':
                choice_invalid = False
                print('\n')
                return 3
            elif choice == '4':
                choice_invalid = False
                print('\n')
                return 4
            elif choice == '5':
                choice_invalid = False
                print('\n')
                return 5
            elif choice == '6':
                choice_invalid = False
                print('\n')
                return 6
            elif choice == '7':
                choice_invalid = False
                print('\n')
                return 7
            elif choice == 'c':
                choice_invalid = False
                return False
            else:
                print("\nInvalid Input\n")

    @staticmethod
    def display_network(names, repetitions, friends):
        """Pretty Prints the social network"""
        max_name_length = 0  # will hold the length of the longest name in the list
        for r in range(repetitions):  # for each name
            if len(names[r]) > max_name_length:  # if the length of the current name if larger than max_name_length
                max_name_length = len(names[r])  # replace max_name_length with new max length

        # pretty print every name and friend list
        print("---")
        for r in range(repetitions):  # for every name
            space_num = (max_name_length + 1) - len(names[r])  # number of spaces required on each line for neat print
            print(names[r], (' ' * space_num), '-> ', str(friends[r]).replace('[', '').replace(']', '').replace("'", ''))
        print("---")
        time.sleep(0.3)

    @staticmethod
    def display_common_friends(values, repetitions, net_class):
        """Pretty prints the common friend count between every user"""
        max_name_length = 0  # will hold the length of the longest name in the list
        for r in range(repetitions):  # for each name
            if len(net_class.get_users()[r]) > max_name_length:  # if the length of the current name if larger than
                # max_name_length
                max_name_length = len(net_class.get_users()[r])  # replace max_name_length with new max length

        # pretty print every name and friend list
        print("---")
        for r in range(repetitions):  # for every name
            space_num = (max_name_length + 1) - len(net_class.get_users()[r])  # number of spaces required on each
            # line for neat print
            print(net_class.get_users()[r], (' ' * space_num), '-> ', net_class.calculate_common_friend_count(values)[r]
                  )
        print("---")
        time.sleep(0.3)

    @staticmethod
    def display_recommended_friend(users, friend_list, common_friends, name_list):
        """Prints a specified user's recommended friend"""
        selected_user = input("For which user would you like to get a recommended friend?: ")
        for i in range(len(name_list)):  # for every user object
            if selected_user == name_list[i].get_name():  # find selected user's object
                recommended_friend = (name_list[i].get_recommendation(i, users, friend_list,
                                                                      common_friends))  # method call
                if recommended_friend is not None:
                    print("\nThe recommended friend for", selected_user, "is", users[recommended_friend])
                    # output
                else:
                    print("\nThis user does not have a recommended friend.")
            elif selected_user not in users:
                return print("This user doesnt exist in this network.")

    @staticmethod
    def display_user_relationships(user_list, relationships):
        """Prints the friends of one specified user"""
        user = input("For which user would you like to see the relationships?: ")  # ask user to enter name

        if user not in user_list:  # if entered name isn't a member of the network
            return print("This user does not exist in this network.")  # print message

        for i in range(len(user_list)):  # for every user
            if user == user_list[i]:  # if a match is found
                return print(user, '->', str(relationships[i]).replace('[', '').replace(']', '').replace("'", ""))
                # print message
        time.sleep(0.2)

    @staticmethod
    def display_user_friend_count(user_list, object_names):
        """Pretty prints the number of friends of one specified user"""
        user = input("For which user could you like to see the friend count?: ")  # takes input name
        for i in range(len(user_list)):  # for each user
            if user == user_list[i]:  # compare entered name
                index = i  # if they match, assign index to a variable
            elif user not in user_list:
                return print("This user does not exist in this network.")
        return print("\nThis user has", object_names[index].get_friend_count(), "friends.")

    @staticmethod
    def display_indirect_friends(indirect_lists, user_list):
        """Pretty prints the lists of indirect friends for each user"""
        max_name_length = 0  # will hold the length of the longest name in the list
        for j in range(len(user_list)):  # for each name
            if len(user_list[j]) > max_name_length:  # if the length of the current name if larger than
                # max_name_length
                max_name_length = len(user_list[j])  # replace max_name_length with new max length

        print("---")
        for i in range(len(user_list)):  # for each list
            space_num = (max_name_length + 1) - len(user_list[i])
            print(user_list[i], (' ' * space_num), "->", str(indirect_lists[i]).replace('[', '').replace(']', '').replace("'", ''))
            # print it in this format
        print("---")

    @staticmethod
    def display_lowest_friends(object_names, no_friends, one_friend, friend_lists):
        """Pretty prints the users with either one or zero friends and how many they have"""
        max_name_length = 0  # will hold the length of the longest name in the list
        for j in range(len(object_names)):  # for each name
            if len(object_names[j].get_name()) > max_name_length:  # if the length of the current name if larger than
                # max_name_length
                max_name_length = len(object_names[j].get_name())  # replace max_name_length with new max length

        print("---")
        for i in range(len(object_names)):  # for every user object
            space_num = (max_name_length + 1) - len(object_names[i].get_name())  # calculate space for pretty print
            if isinstance(object_names[i], no_friends) or isinstance(object_names[i], one_friend):  # if object is an
                # instance of SolitaryUser or SingleFriendUser
                print(object_names[i].get_name(),(' ' * space_num), "->", len(friend_lists[i]))  # pretty print this
        print("---")
