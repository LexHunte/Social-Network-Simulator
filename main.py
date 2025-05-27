"""Author: Jaydn Hunte, 001215283. Last Updated: 22/12/2022"""

from UI_Class import UI
from File_Class import File
from SocialNetwork_Class import SocialNetwork
from User_Classes import *
import snws_Functions

repeat = True

UI.welcome()  # welcome message
while repeat:
    valid_format = False
    user_id = {}

    while not valid_format:
        user_names = {}  # allows user input to be names for User objects
        snw_users = []  # holds the users in a social network
        snw_relationships = []  # holds the list of relationships in a social network

        TextFile = File(UI.confirm_file().readlines())  # creates new instance of File

        # instantiate the social network
        for i in range(1, len(TextFile.get_contents())):  # for every line in the file except the first
            snw_users.append(TextFile.get_contents()[i].split()[0])  # Add the first name of every pair to a list
            if len(TextFile.get_contents()[i].split()) > 1:  # if the user has at least one friend
                snw_users.append(TextFile.get_contents()[i].split()[1])  # Add the second name of every pair to the list

        snw_users = snws_Functions.find_users(snw_users)
        snw_relationships = (snws_Functions.find_relationships(snw_users, TextFile.get_contents()))

        valid_format = TextFile.validate_format(snw_users)  # checks if the file is in the required format

    Network = SocialNetwork(snw_users, int(TextFile.get_contents()[0]), snw_relationships, [])  # instantiates network

    for user in range(len(Network.get_users())):  # for every user in network
        user_id.update(
            {Network.get_users()[user]: Network.get_relationships()[user]})  # add to dict as key and friends as value

    nw_keys = list(user_id.keys())  # make list of keys a variable
    nw_vals = list(user_id.values())  # make list of values a variable

    snws_Functions.create_users(Network.get_users(), nw_keys, nw_vals, SolitaryUser, SingleFriendUser, MultiFriendUser
                                )  # call function to instantiate users

    # takes user input and performs functions
    action = True
    while action:  # while the user wants to perform actions
        action = UI.action_input()  # call method to get input
        # do the follow depending on the user input
        if action == 1:
            UI.display_network(Network.get_users(), Network.get_size(), Network.get_relationships())  # display network
        elif action == 2:
            UI.display_common_friends(nw_vals, Network.get_size(), Network)
        elif action == 3:
            UI.display_recommended_friend(Network.get_users(), Network.get_relationships(),
                                          Network.calculate_common_friend_count(nw_vals), nw_keys)
        elif action == 4:
            UI.display_user_relationships(Network.get_users(), Network.get_relationships())
        elif action == 5:
            UI.display_user_friend_count(Network.get_users(), nw_keys)
        elif action == 6:
            UI.display_indirect_friends(Network.calculate_indirect_friends(nw_keys), Network.get_users())
        elif action == 7:
            UI.display_lowest_friends(nw_keys, SolitaryUser, SingleFriendUser, Network.get_relationships())
