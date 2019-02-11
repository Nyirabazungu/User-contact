import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Nya","Vava","0725296112","Nyanki","vnyanki@gmail.com","Kigali") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properl
        '''
        self.assertEqual(self.new_user.first_name,"Nya")
        self.assertEqual(self.new_user.last_name,"Vava")
        self.assertEqual(self.new_user.contact,"0725296112")
        self.assertEqual(self.new_user.user_name,"Nyanki")
        self.assertEqual(self.new_user.email,"vnyanki@gmail.com")
        self.assertEqual(self.new_user.password,"Kigali")
        
    
    def test_save_user(self):
        '''
        test_save_contact test case to test if the user object is saved into
        the user list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)

        
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

# other test cases here
    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Nya","vava","0725296112","Nyanki","vnyanki@gmail.com","Kigali") # new user
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Nya","vava","0725296112","Nyanki","vnyanki@gmail.com","Kigali") # new contact
        test_user.save_user()

        self.new_user.delete_user()# Deleting a user object
        self.assertEqual(len(User.user_list),1)   

    def test_find_user_by_email(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

        self.new_user.save_user()
        test_user = User("Nya","vava","0725296112","Nyanki","vnyanki@gmail.com","Kigali") # new contact
        test_user.save_user()

        found_user = User.find_by_email("vnyanki@gmail.com")

        self.assertEqual(found_user.user_name,test_user.user_name)    
 

if __name__ == '__main__':
    unittest.main()        