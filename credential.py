# class Credintial:
# import pyperclip
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
    
   
#         # for credintial in cls.credintial_list:
#         #     if credintial.email== email:
#         #             return True

#         return False    
        
             