"""Author: Jaydn Hunte, 001215283. Last Updated: 15/12/2022"""
import time


class File:
    """Every instance contains the information read into files"""

    def __init__(self, contents):
        """Only has one attribute"""
        self.__contents = contents

    def get_contents(self):
        return self.__contents

    def validate_format(self, users):
        """ensures the file is a valid social network"""
        checksum = 0  # counts how many validity checks are passed
        # validity check 1
        try:
            int(self.__contents[0])  # try to turn the first line of the file into an integer
        except IndexError:  # if an IndexError is raised
            time.sleep(0.2)
            print("Invalid File Format. Please try a different file.")
            return False  # the format is invalid
        except ValueError:  # if a ValueError is raised
            time.sleep(0.2)
            print("Invalid File Format. Please try a different file.")
            return False  # the format is invalid
        else:
            checksum += 1

        if int(self.__contents[0]) == len(users):  # if the number in the first line equals the number of users
            checksum += 1  # add to checksum
        else:
            time.sleep(0.2)
            print("Invalid File Format. Please try a different file.")
            return False  # the format is invalid

        length_check = 0
        for line in range(len(self.__contents)):
            if len(self.__contents[line].split()) > 2:
                length_check += 1

        if length_check > 0:  # if any line in the file has more than two names
            time.sleep(0.2)
            print("Invalid File Format. Please try a different file.")
            return False  # the format is invalid
        else:
            checksum += 1

        if checksum == 3:  # if all requirements met
            return True  # format valid
