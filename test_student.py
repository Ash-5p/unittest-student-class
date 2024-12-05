import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    def setUp(self):
        '''
        setUp creates a class instance that can be used by each test function,
        so that the class instance properties don't need to be defined in each
        function.
        '''
        print("setUp")
        self.student = Student("John", "Doe")

    def tearDown(self):
        '''
        tearDown is used to remove the class instance set up by the setUp method.
        Not needed for this example (added as placeholder)
        '''
        print("tearDown")


    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")


    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")


    def test_apply_extension(self):
        print("test_apply_extension")
        old_end_date = self.student.end_date
        self.student.apply_extension(5)
        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

    
    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)


if __name__ == "__main__":
    unittest.main()
