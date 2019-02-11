# import unittest # Importing the unittest module
# from credintial import Credintial # Importing the credintial class

# class TestCredintial(unittest.TestCase):

#     '''
#     Test class that defines test cases for the credintial class behaviours.

#     Args:
#         unittest.TestCase: TestCase class that helps in creating test cases
#     '''
#     def setUp(self):
#         '''
#         Set up method to run before each test cases.
#         '''
#         self.new_credintial = Credintial("Nyanki","vnyanki@gmail.com","Kigali") # create user object


#     def test_init(self):
#         '''
#         test_init test case to test if the object is initialized properl
#         '''
#         self.assertEqual(self.new_credintial.user_name,"Nyanki")
#         self.assertEqual(self.new_credintial.email,"vnyanki@gmail.com")
#         self.assertEqual(self.new_credintial.password,"Kigali")
        
    
#     def test_save_credintial(self):
#         '''
#         test_save_contact test case to test if the credintial object is saved into
#         the credintial list
#         '''
#         self.new_credintial.save_credintial() # saving the new credintial
#         self.assertEqual(len(Credintial.credintial_list),1)

        
#     def tearDown(self):
#         '''
#         tearDown method that does clean up after each test case has run.
#         '''
#         Credintial.credintial_list = []

#         # other test cases here
#     def test_save_multiple_credintial(self):
#         '''
#         test_save_multiple_credintial to check if we can save multiple credintial
#         objects to our credintial_list
#         '''
#         self.new_credintial.save_credintial()
#         test_credintial = Credintial("Nyanki","vnyanki@gmail.com","Kigali") # new credintial
#         test_credintial.save_credintial()
#         self.assertEqual(len(Credintial.credintial_list),2)

#     def test_delete_credintial(self):
#         '''
#         test_delete_credintial to test if we can remove acredintial from our credintial list
#         '''
#         self.new_credintial.save_credintial()
#         test_credintial = Credintial("Nyanki","vnyanki@gmail.com","Kigali") # new contact
#         test_credintial.save_credintial()

#         self.new_credintial.delete_credintial()# Deleting a credintial object
#         self.assertEqual(len(Credintial.credintial_list),1)   

#     def test_find_credintial_by_email(self):
#         '''
#         test to check if we can find a concredintial by email and display information
#         '''

#         self.new_credintial.save_credintial()
#         test_credintial = Credintial("Nyanki","vnyanki@gmail.com","Kigali") # new contact
#         test_credintial.save_credintial()

#         found_credintial = Credintial.find_by_email("vnyanki@gmail.com")

#         self.assertEqual(found_credintial.user_name,test_credintial.user_name)    
    
#     def test_credintial_exists(self):
#         '''
#         test to check if we can return a Boolean  if we cannot find the credintial.
#         '''

#         self.new_credintial.save_credintial()
#         test_credintial = Credintial("Nyanki","vnyanki@gmail.com","Kigali") # new contact
#         test_credintial.save_credintial()

#         credintial_exists = Credintial.credintial_exist("vnyanki@gmail.com")

#         self.assertTrue(credintial_exists)

# if __name__ == '__main__':
#     unittest.main()        