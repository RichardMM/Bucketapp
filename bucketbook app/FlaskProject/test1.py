import unittest

import unittest
from FlaskProject import app
from FlaskProject.templates import *

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

        # sends HTTP GET request to the application

        # on the specified path

        result = self.app.get('/') 
        # assert the response data

        self.assertEqual(result.data, createaccount)

    def test_mybucket(self):
        #assert response
        result = self.app.get('/bucketlist/samplebucket')
        self.assertEqual(result.data, samplebucketlist1)

if __name__ == '__main__':
    unittest.main()
