import unittest

class Test_test_1(unittest.TestCase):
    def test_A(self):
        print('THE TEST IS RUNNING')
        ran = True
        self.assertTrue(ran)

if __name__ == '__main__':
    unittest.main()
