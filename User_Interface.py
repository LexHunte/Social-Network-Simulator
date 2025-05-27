"""Author: Jaydn Hunte, 001215283. Last Updated: 12/12/2022"""

import time
import File_Class
import SocialNetwork_Class
from User_Classes import *

input_validity = False
nw_num = 0
run = 'y'  # allows the program to start
choice = ''

file_names = {}  # allows user input to be names for objects
snw_names = {}  # allows user input to be names for objects
usernames = {}  # allows user input to be names for objects

print("Welcome to the Social Network Simulator!\n")  # welcome message
time.sleep(0.5)

while run == 'y':  # user can interact with console until they choose to exit with 'n'
    file_to_open = input("Please enter the filename of the file that you would like to simulate: ")

    snw_contents = []  # uniquely identifies contents of every file (mimics autonumber)
    user_list = []  # holds the list of users in the file
    friend_list = []  # holds the list of friends for each user

    current_file = open(file_to_open, "r")  # allows the file's contents to be accessed
    file_names[file_to_open] = File_Class.File(current_file,
                                               current_file.readlines())  # filename used to create new object

    if not file_names[file_to_open].validate_format():  # checks file is compatible with the program
        continue

    snw_contents.append(file_names[file_to_open].get_contents())  # adds contents of file into list

    # takes contents of file, extracts each name, stores it in user_list
    for item in range(2, int(snw_contents[nw_num][0]) + 2):
        user_list.append(snw_contents[nw_num][item].split()[0])
    time.sleep(1)

    name = input("What would you like to name your social network?: ")

    #  gets a value for the relationships attribute
    for item in range(2, int(snw_contents[nw_num][0]) + 2):
        friend_list.append(snw_contents[nw_num][item].split())

    snw_names[name] = SocialNetwork_Class.SocialNetwork(user_list, int(snw_contents[nw_num][0]),
                                                        friend_list, {})  # creates instance of SocialNetwork

    nw_num += 1  # prepares for the next potential file

    # this section instantiates every user, categorising them as Solitary, SingleFriend or MultiFriend
    for i in range(len(snw_names[name].get_relationships())):  # for every user in the network
        if len(snw_names[name].get_relationships()[i]) > 1:  # if a user has at least one friend
            friend_index = snw_names[name].get_relationships()[i][1].split(',')  # puts their friends into a list
            if len(friend_index) > 1:  # if they have >1 friends
                usernames[i] = MultiFriendUser(snw_names[name].get_relationships()[i][1], '')
            elif len(friend_index) == 1:  # if they have 1 friend
                usernames[i] = SingleFriendUser(snw_names[name].get_relationships()[i][1], '')
        else:  # if they have 0 friends
            usernames[i] = SolitaryUser()

    print()  # tests to see how to call the object method

    while choice != 'n':  # loops if the input is invalid
        choice = input("\nWhat would you like to do?\n\n"
                       "1: Display a social network\n"
                       "2: Display common friend count\n"
                       "3: Find a recommendation\n"
                       "4: Display the number of friends for a user\n"
                       "5: Display the users with the least friends\n"
                       "6: Display the relationships of a user\n"
                       "7: Display indirect friends\n"
                       "Enter a number to confirm your choice or enter n to quit: ")
        print("\n")

        if choice == '1':
            snw_names[name].display_social_network()
        elif choice == '2':
            snw_names[name].display_common_friend_count()
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        elif choice == '5':
            pass
        elif choice == '6':
            pass
        elif choice == '7':
            pass
        elif choice == 'n':
            run = 'n'
        else:
            print("Invalid Input. Please Try again")
