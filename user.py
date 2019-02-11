class User:
    """
    Class that generates new instances of contacts.
    """
    user_list=[]#Empty user list
    # Init method up here
    def __init__(self,first_name,last_name,contact,user_name,email,password):

        self.first_name = first_name
        self.last_name = last_name  
        self.contact= contact
        self.user_name = user_name
        self.email = email
        self.password = password
        
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

    

    @classmethod
    def find_by_email(cls,email): 
     
        '''
        Method that takes in a email and returns a useer that matches that email.

        '''

        for user in cls.user_list:
            if user.email == email:
                return user   
    
    @classmethod
    def user_exist(cls,email):
        '''
        Method that checks if a user exists from the user list.
        Args:
            email:email to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.email== email:
                    return True

        return False    
        
       

#  class Credintial:
#     """
#     Class that generates new instances of credintial .
#     """
#     credintial_list=[]#Empty credintial list
#     # Init method up here
#     def __init__(user_name,email,password):

#         self.user_name = user_name
#         self.email = email
#         self.password = password
        
#     def save_credintial(self):

#         '''
#         save_credintial method saves credintial objects into credintial_list
#         '''

#        Credintial.credintial_list.append(self)

#     def delete_credintial(self):

#         '''
#         delete_credintial method deletes a saved credintial from the credintial_list
#         '''

#         Credintial.credintial_list.remove(self) 

    

#     @classmethod
#     def find_by_email(cls,email): 
     
#         '''
#         Method that takes in a email and returns a credintial that matches that email.

#         '''

#         for credintial in cls.credintial_list:
#             if credintial.email == email:
#                 return credintial   
    
#     @classmethod
#     def credintial_exist(cls,email):
#         '''
#         Method that checks if a credintial exists from the credintial list.
#         Args:
#             email:email to search if it exists
#         Returns :
#             Boolean: True or false depending if the credintial exists
#         '''
#         for credintial in cls.credintial_list:
#             if credintial.email== email:
#                     return True

#         return False    
        
             