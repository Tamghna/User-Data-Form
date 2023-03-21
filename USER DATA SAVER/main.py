#feel free to modify this code !!!!!!!
#use it in your own projects
#no copyright


#imports
import os


def delete():
    del_nm = input("Enter Name to Delete :----->")
    os.remove(del_nm + ".txt")
    print("[DELETED SUCESSFULLY]")













def add_data_base():
    name = input("Enter Name :")
    age = input("Enter Age : ")
    ph_num = input("Enter PHONE NUMBER :")
    address = input("Enter Address : ")
    email = input("Enter Email Address :")
    id = input("Enter ID :")

    with open( name + ".txt" , 'a')as a:
        a.write("Name : " + name + "\n")
        a.write("Age : " + age + "\n")
        a.write("Phone Number : " + ph_num + "\n")
        a.write("Address : " + address + "\n")
        a.write("email : " + email+ "\n")
        a.write("id : " + id + "\n")

    print("[SUCESSFULLY ADDED]")







def read():
    nm = input("Enter Name : ")
    val = open(nm + ".txt" , 'r').read()
    print(val)


def show_list():
    
# import OS module

 
# Get the list of all files and directories
    path = ""
    dir_list = os.listdir()
    dir_list.remove("main.py")
    print(" List of All Data . :----> :")

    print("\n")
    
    # prints all files
    print(dir_list)







while True:
    print("\n")
    cmd = input("Enter Command | [add] to add user to data base | [read] to read data  |  [list] to show list of data |  [del] to delete a name | ----->")
    if cmd == "add":
        add_data_base()


    if cmd == "read":
        print("\n")
        read()

    if cmd == "list":
        show_list()

    if cmd == "del":
        delete()
