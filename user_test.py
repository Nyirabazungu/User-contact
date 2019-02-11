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
        self.new_user = User("Nya","Vava","Nyanki","vnyanki@gmail.com") # create user object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properl
        '''
        self.assertEqual(self.new_user.first_name,"Nya")
        self.assertEqual(self.new_user.last_name,"Vava")
        self.assertEqual(self.new_user.user_name,"Nyanki")
        self.assertEqual(self.new_user.password,"vnyanki@gmail.com")

if __name__ == '__main__':
    unittest.main()        