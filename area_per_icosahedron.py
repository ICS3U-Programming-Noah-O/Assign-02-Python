#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Dec. 2, 2021
# This program calculates the volume and surface area of an icosahedron

import math
import time
import colorama
from colorama import Fore, Back, Style


def main():
    # This function asks for units and side length and then calculates the
    # volume and surface area
    print(Fore.WHITE + "This program calculates the volume "
          + "and surface area of an icosahedron!")
    print(" ")
    time.sleep(2)

    # Input

    units = str(input(Fore.CYAN + "Enter the units that you're using: "))
    edge_length = int(input("Enter the edge length: "))

    # process

    volume_icosahedron = ((5 * (3 + math.sqrt(5))) / 12) * (edge_length ** 3)
    surface_area_icosahedron = (5 * math.sqrt(3)) * (edge_length ** 2)
    time.sleep(2)

    # This function displays the surface area
    def surface():
        print(" ")
        print(Fore.WHITE + "The surface area of your "
              + "icosahedron is: {:,.2f}".format(surface_area_icosahedron)
              + " {}^2".format(units))
        print(" ")

    # This function displays the volume
    def volume():
        print(" ")
        print(Fore.WHITE + "The volume of your "
              "icosahedron is: {:,.2f}".format(volume_icosahedron)
              + " {}^3".format(units))
        print(" ")

    # This function allows the user to choose either volume or surface area
    def choice():

        if(user_choice == "volume"):

            volume()
        elif(user_choice == "surface area"):

            surface()

        else:
            print("You must enter either volume or surface area")

    # Calls choice function
    print(Fore.MAGENTA + "Would you like to try to calculate "
          + "volume or surface area?")
    user_choice = str(input(" "))
    choice()

    # Ask user if they want to calculate again
    time.sleep(2)
    print(Fore.BLUE + "Would you like to try with a different edge length?")
    user_answer = str(input("Y or N:"))

    if(user_answer == "Y"):

        main()
    if(user_answer == "y"):

        main()
    else:
        print(Fore.YELLOW + "Thank you for using this program")


if __name__ == "__main__":
    main()
