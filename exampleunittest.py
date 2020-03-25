import unittest
import example
import array as arr

class UnitTests(unittest.TestCase):
    def test_add(self):
        self.assertEquals(4,example.add(2,2))
        self.assertEquals(4,example.add(2,2))

    def test_divide(self):
        self.assertEquals(2,example.divide(4,2))
        self.assertTrue(example.divide(40,20) == 2)
        self.assertFalse(example.divide(33,54) == 7)
        # self.assertFalse(example.divide(5,0) == 7)
    
    def test_Arrays(self):
        a = arr.array('i', [1,2,3])
        self.assertEquals(a,example.getArray())
        self.assertIn(2,example.getArray())
        self.assertNotIn(4,example.getArray())

if __name__ == '__main__':
    unittest.main()
