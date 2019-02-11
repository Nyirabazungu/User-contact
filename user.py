class User:
    """
    Class that generates new instances of contacts.
    """
    user_list=[]#Empty contact list
    # Init method up here
    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 

    def __init__(self,first_name,last_name,contact,user_name,email,password):

        @classmethod
    def find_by_email(cls,email): 
     
        '''
        Method that takes in a email and returns a useer that matches that email.

        '''

        for user in cls.user_list:
            if user.email== email:
                return user   
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            first_name:New user first name.
            last_name:New user last name.
            contact:New user contact.
            user_name: New user user name.
            user_name: New user email.
            password : New user password.

        ''' 
        self.first_name = first_name
        self.last_name = last_name  
        self.contact= contact
        self.user_name = user_name
        self.email = email
        self.password = password
        
       