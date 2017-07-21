import unittest
from FlaskProject import app

class FlaskBookshelfTests(unittest.TestCase): 

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        self.app.testing = True 


    def test_home(self):

        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 
        # assert the status code of the response
        self.assertEqual(result.status_code, 200) 

    #------should look at how to make this test work_____
    #def test_home_data(self):
    #    # sends HTTP GET request to the application

    #    # on the specified path

    #    result = self.app.get('/') 
    #    # assert the response data
    #    self.assertEqual(result.data, createaccount)


if __name__ == '__main__':
    unittest.main()
