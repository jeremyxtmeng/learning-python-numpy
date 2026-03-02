
# Lesson 23. Capstone project: analyze your friends
import os
current_directory = os.getcwd()
file1= current_directory+ "\\public\\ana_bell_book_cap2_phone_book.txt"

with open(file1.replace('\\', '/'), 'r') as file: book = file.read()

#Write a program that reads input from a file in a specific
#format, regarding all your friends’ names and phone
#numbers. Your program should store that information
#and analyze it in some way. For example, you can show
#the user where their friends live based on the area code
#of the phone numbers, and the number of states where
#they live.

# identify location of \n
name=()
phone=()
# before name
phonebook=book
count=1

def clean_phone_number(content):
    content1=content.replace("(","")
    content2=content1.replace(")","")
    content3=content2.replace("-","")
    return content3

while len(phonebook)>0:
    contents=phonebook[0:phonebook.find("\n")]
    phonebook=phonebook.replace(contents+"\n","")
    if count%2!=0:
      name=name+(contents,)
    else:
      phone=phone+(clean_phone_number(contents),)
    count+=1

name=name[0:len(name)-1] # remove empty
