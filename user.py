class User:
    """
    Class that generates new instances of contacts.
    """
    user_list=[]#Empty contact list
    def _init_(self,user_name,password):
       # docstring removed for simplicity
        self.user_name = user_name
        self.password = password
        
       