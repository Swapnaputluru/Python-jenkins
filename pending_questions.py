# 3. Write a Python program that removes and prints every third number from a list of numbers until the list is empty.

list1= [10,20,30,40,50,60,70,80,90]

import emoji
# print("Smiling face with heart eyes: ","\U0001F60D")
# print("Unamused face: \U0001F612")
# print("Beaming face with smiling eyes: \U0001F604")
# print("Grinning face with sweat: \U0001F605")
# print("Face with tears of joy unicode: \U0001F602")
# print("Slightly smiling face : \U0001F642")
# print("Smiling face with halo: \U0001F607")
# print("Zipper mouth face: \U0001F910")
# print("Grinning face: \U0001F600")
# print("Rolling on the floor laughter: \U0001F923")
#
#
# a=24
# b=
#
# for i in range(max(list1)):
#     if a%i==0 and b%i==0:







#
# 130. Write a Python program to check whether a given month and year contains a Monday 13th.
# Month No.: 11 Year: 2022
# Check whether the said month and year contains a Monday 13th.: False
# Month No.: 6 Year: 2022
# Check whether the said month and year contains a Monday 13th.: True

import datetime
def check_13_ismonday(month,year):
    date = 13
    d = datetime.date(year,month,date)
    print(f"For month {month} and year {year} :")
    print("Day for given date:", d.weekday())
    if d.weekday()==0:
        print("Yes, it's Monday: ",True)
    else:print("No, it's not Monday:",False)

check_13_ismonday(6,2022)




# 58. When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.
# Write a Python program to restore the original string by entering the compressed string with this rule. However, the # character does not appear in the restored character string.
# Input:
# The restored character string for each character on one line.
# Original text: XY#6Z1#4023
# XYZZZZZZ1000023
# Original text: #39+1=1#30
# 999+1=1000

text = "XY#6Z1#4023"
text = "#39+1=1#30"
def restored_character(text):
    new_text = ""
    i=0
    while i <(len(text)):
        if text[i]=="#":
            new_text+=text[i+2]*int(text[i+1])
            i+=3
        else:
            new_text+=text[i]
            i+=1
    print(f"Restored text is: {new_text}")

restored_character("#39+1=1#30")
restored_character("XY#6Z1#4023")


# 46. Write a Python program that reads a date (from 2016/1/1 to 2016/12/31) and prints the day of the date. Jan. 1, 2016, is Friday. Note that 2016 is a leap year.
# Input:
# Two integers m and d separated by a single space in a line, m ,d represent the month and the day.
# Input month and date (separated by a single space):
# 5 15
# Name of the date: Sunday

import datetime
def find_day(date,month,year=2016):
    days = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    d = datetime.date(year,month,date)
    day = d.weekday()
    print(f"The day is:  {days[day]}")

# find_day(15,5)
# find_day(29,2)
# find_day(10,8,2023)

# 17. Write a Python program to get all strobogrammatic numbers that are of length n.
# A strobogrammatic number is a number whose numeral is rotationally symmetric, so that it appears the same when rotated 180 degrees. In other words, the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']

# 47. Write a Python program that reads text (only alphabetical characters and spaces) and prints two words. The first word is the one that appears most often in the text. The second one is the word with the most letters.
# Note: A word is a sequence of letters which is separated by the spaces.
# Input:
# A text is given in a line with following condition:
# a. The number of letters in the text is less than or equal to 1000.
# b. The number of letters in a word is less than or equal to 32.
# c. There is only one word which is arise most frequently in given text.
# d. There is only one word which has the maximum number of letters in given text.
# Input text: Thank you for your comment and your participation.
# Output: your participation.
def max_count_length(text):
    dict1 ={}
    words = text.split()
    if len(text)<=1000 and len(words)<=32:
        for i in words:
            keys = dict1.keys()
            if i in keys:
                dict1[i]+=1
            else:
                dict1[i] =1
        else:
            print("Maximim frequency of word: ", max(dict1.keys()))
            print("Maximun length of word: ", max(words, key=len))
    else:
        print("Text length is out of range")

# max_count_length("Thank you for your comment and your participation.")
#
#
# max_count_length("What is the SimpleText? SimpleText is a text editor made for the classic Mac OS operating system."
#                  " It replaced simpler text editor programs made in the age of the command-line interface.")
#





X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
A= [20,60,70,80]

lists =[X,Y,Z,A]

print("Hello Swapna", lists)


print("Uday")





















