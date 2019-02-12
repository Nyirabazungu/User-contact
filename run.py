#!/usr/bin/env python3.6

def create_user(first_name,last_name,contact,user_name,email,password):
    '''
    Function to create a new user
    '''
    new_user = User(first_name,last_name,contact,user_name,email,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user() 

def find_user(email):
    '''
    Function that finds a user by email and returns the user
    '''
    return User.find_by_email(email) 

 
def check_existing_users(email):
    '''
    Function that check if a user exists with that email and return a Boolean
    '''
    return User.user_exist(email)  

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()         




def main():
     print("Hello Welcome to your user list. What is your name?")
     user_name = input()

     print("Hello Welcome to your credential list. What is your password?")
     user_name = input()

     print(f"Hello {user_name}. what would you like to do?")
     print('\n')

     while True:
                    print("Use these short codes : cu - create a new user, du - display users, fu -find a user, dl - delete users,ex -exit the user list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New User")
                            print("-"*10)

                            print ("First name ....")
                            first_name = input()

                            print("Last name ...")
                            last_name = input()

                            print("contact ...")
                            contact = input()

                            print("User name ...")
                            user_name = input()

                            print("email ...")
                            email = input()

                            print("Password ...")
                            password = input( )

                      


                            save_users(create_user(first_name,last_name,contact,user_name,email,password)) # create and save new contact.
                            print ('\n')
                            print(f"New User {first_name} {lname_name} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your users")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.first_name} {user.last_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any users saved yet")
                                    print('\n')

                    elif short_code == 'fu':

                            print("Enter the email you want to search for")

                            search_email = input()
                            if check_existing_users(search_email):
                                    search_user = find_user(search_email)
                                    print(f"{search_user.first_name} {search_user.last_name}")
                                    print('-' * 20)

                                    print(f"email address.......{search_user.email}")
                                    print(f"contact.......{search_user.contact}")
                            else:
                                    print("That user does not exist")

                   
                            
                #     elif del_user=='dl' ():  

                #                     print("Enter the something you want to delete")
                                    
                #                     delete_user = input()
                                   
                #                     user=(del_user [first_name,last_name,contact,user_name,email,password])
                #                     del user[first_name,last_name,contact,user_name,email,password]
                                    
                              


                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes") 
if __name__ == '__main__':

    main()
