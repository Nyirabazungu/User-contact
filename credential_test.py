# import pyperclip
    
#     def test_copy_email(self):
#         '''
#         Test to confirm that we are copying the email address from a found contact
#         '''

#         self.new_user.save_user()
#         User.copy_email("vnyanki@gmail.com")

#         self.assertEqual(self.new_user.email,pyperclip.paste())

     
#     @classmethod
#     def copy_email(cls,email):
#         user_found = User.find_by_email(email)
#         pyperclip.copy(user_found.email)   