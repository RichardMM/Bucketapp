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

    def test_home_data(self):
        # check create account page is rendered in home route
        result = self.app.get('/') 
        # assert the response data
        self.assertIn(b"Create account to start tracking your dreams", result.data)

    def test_creataccount(self):
        #test that creating an account works
        account_data = {"firstname": "firstname",
                        "surname": "surname", 
                        "phone": "phone", 
                        "emailaddress": "emailaddress", 
                        "password": "password", 
                        "pswrepeat": "password"}
        result = self.app.post("/", data=account_data, follow_redirects=True)
        self.assertIn(b"email", result.data)
        
    
    def test_storage(self):


if __name__ == '__main__':
    unittest.main()
