#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: DEC. 2, 2021
# This program calculates the volume and surface area of an icosahedron

import math
import time


def main():
    # This function asks for the radius and then calculates the area and perimeter.
  print(" ")
  print("This program calculates the area and perimeter of an icosahedron!")
    # Input
  units = str(input("Enter the units that you're using: "))
  edge_length = int(input("Enter the edge length: "))
  volume_icosahedron = ((5 * (3 + math.sqrt(5))) / 12) * (edge_length ** 3)
  surface_area_icosahedron = (5 * math.sqrt(3)) * (edge_length ** 2)
  
  def surface():
    print(" ")
    print("The surface area of your icosahedron is: {}".format (surface_area_icosahedron) + " {}".format(units))
    print(" ")
    
  def volume():
    print(" ")
    print("The volume of your icosahedron is: {}".format (volume_icosahedron) + " {}^2".format(units))
    print(" ")
    
   
    
  def choice():
      
      if(user_choice == "volume"):
    
        volume()
      elif(user_choice == "surface area"):
      
          surface()


  print("Would you like to try to calculate volume, surface area, of total edge length?")
  user_choice = str(input(" "))
  choice()

  
  
  
    

  

  # Ask user if they want to calculate again
  print("Would you like to try with a different edge length?")
  user_answer = str(input("Y or N:"))

  if(user_answer == "Y" or "y"):
    
    main()

    

if __name__ == "__main__":
    main()
