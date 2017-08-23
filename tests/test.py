"""
tests for whole app
"""
from flaskProject import app
import unittest


class FlaskBookshelfTests(unittest.TestCase): 

    def setUp(self):
        # creates a test client
        app.config['WTF_CSRF_ENABLED'] = False
        app.secret_key = "lkjhg646"
        self.app = app.test_client()
        self.app.testing = True
        self.account_data = {"firstname": "firstname",
                        "surname": "surname", 
                        "phone": "phone", 
                        "emailaddress": "emailaddress", 
                        "password": "password", 
                        "pswrepeat": "password"}
        self.login_data = {"email": "emailaddress",
                           "password": "password", }

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
        result = self.app.post("/", data=self.account_data, follow_redirects=True)
        self.assertIn(b"Login to start tracking your dreams", result.data)

    def test_login(self):
        # test that login works from create account
        with self.app as sess:
            self.app.post("/", data=self.account_data, follow_redirects=True)
            result = self.app.post("/login", data=self.login_data, follow_redirects=True)
            self.assertIn(b"My Profile", result.data)
            self.assertIn(b"Sample", result.data)
            self.assertIn(b"Add", result.data)


    def test_buckets_storage(self):
        # test whether a newly created bucket is saved and rendered
        with self.app as p:
            self.app.post("/", data=self.account_data, follow_redirects=True)
            self.app.post("/login", data=self.login_data, follow_redirects=True)
            response = self.app.post("/mybuckets/{}".format(self.account_data["firstname"]),
                          data={"newbucket": "test_bucket"}, follow_redirects=True)
            # test that input was stored in session variable
            with p.session_transaction() as sess:
                self.assertEqual(sess["newbucket"], "test_bucket")
            #test that the new bucket is displayed on screen
            self.assertIn(b"test_bucket", response.data)


    def test_list_storage(self):
        # test that items can be added to a bucket
        with self.app as p:
            self.app.post("/", data=self.account_data, follow_redirects=True)
            self.app.post("/login", data=self.login_data, follow_redirects=True)
            self.app.post("/mybuckets/{}".format(self.account_data["firstname"]),
                          data={"newbucket": "test_bucket"}, follow_redirects=True)
            response = self.app.post("/{}/test_bucket".format(self.account_data["firstname"]),
                          data={"newlist": "test_list"}, follow_redirects=True)
            # test that input was stored in session variable
            with p.session_transaction() as sess:
                self.assertEqual(sess["bucketitems"]["test_bucket"][0], "test_list")
            #test that the new list is displayed on screen
            self.assertIn(b"test_list", response.data)


if __name__ == '__main__':
    unittest.main()
