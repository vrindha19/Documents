# write a python program to print the following string in a specific format.
# sample String:"Twinkle,twinkle,title star,How I wonder what you are!Up above the world so high,Like a diamond in the sky.Twinkle,twinkle,litle star,How i wonder what you are"

# Twinkile,twinkle,Title star,
# How i wonder what you are!
# up above the world so high
# Like a diamond in the sky.
# Twinkle,twinkle,litle star,
# How I wonder what you are 

# ANS:

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")



# 2. write a python program to find out what version of python you are using.

# ANS:

# import sys
# print("User Current Version:-", sys.version)



# 3. write a python program to display the current date and time.

# sample output:
# current date and time:
# 2014-07-05 14:34:14

# ANS:

# import datetime
 
# current_time = datetime.datetime.now()
 
# print("current date and time:", current_time)



# 4. write a python program that calculates the area of a circle based on the radius entered by the user:
# sample ouput
# r=1.1
# Area=3.80132711084336504def area_of_circle(r):


# def area_of_circle(r):
#     pi=3.2
#     area= pi*r*r
#     return area

# radius=float(input("Enter Radius: "))
# print("Area: ",area_of_circle(radius))


#  5. Write a program to display the first and last colors from the following list.
# color_list=["red","Green","White","Black"]


# color_list = ["Red","Green","White" ,"Black"]
# print( "%s %s"%(color_list[0],color_list[-1]))



#  6. write a python program that takes a sequence 
# of number and determines whether all the numbers are different from each other 


# def test_distinct(data):
#   if len(data) == len(set(data)):
#     return True
#   else:
#     return False;
# print(test_distinct([1,5,7,9]))
# print(test_distinct([2,4,5,5,7,9]))




# 7. write a python program that creates all possible strings using the letters 'a','e','i','0',and'I'
# Ensure that each character is used only once.


# import random
# char_list = ['a','e','i','o','u']
# random.shuffle(char_list)
# print(''.join(char_list))




# 8. write a python program that removes and prints every third number 
# from a list of numbers until the list is empty


# def removeThirdNumber(int_list):
     
#     # list starts with
#     # 0 index
#     pos = 3 - 1
#     index = 0
#     len_list = (len(int_list))
     
#     # breaks out once the
#     # list becomes empty
#     while len_list > 0: 
     
#         index = (pos + index) % len_list
         
#         # removes and prints the required
#         # element
#         print(int_list.pop(index)) 
#         len_list -= 1
 
# # Driver code
# nums = [1, 2, 3, 4,5,6,7,8,9,10,11,12] 
# removeThirdNumber(nums)



# 9. write a python program to identify unique triples whose 
# three elements sum to zero from an arry of n integers.








# 10. write a python program to make combinations of 3 digits.





# 11. write a python program to create a class representing a circle.
# include methods to calcalute its area and perimeter.

