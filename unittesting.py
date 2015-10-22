import unittest
import auth

class TestLoginMethods(unittest.TestCase):

    def test_auth_true(self):
        s = auth.kcheck()
        self.assertEquals(s, 0)

    def test_auth_false(self):
        s = auth.kcheck()
        self.assertNotEqual(s, 1)

if __name__ == '__main__':
    unittest.main()
