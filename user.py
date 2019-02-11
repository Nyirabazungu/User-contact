class User:
    """
    Class that generates new instances of contacts.
    """
    user_list=[]#Empty contact list
    def _init_(self,user_name,password):
        '''
        __init__ method that helps us define properties for our objects.

        Args:
            user_name: New user user name.
            password : New user password.
        '''    
        self.user_name = user_name
        self.password = password
        
       