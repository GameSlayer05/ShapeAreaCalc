import unittest
from main import calculator

# Unit test class
class TestCircleArea(unittest.TestCase):
    
    def test_area_valid_radius(self):
        # Test with a known radius (e.g., r=2, area=4*pi)
        self.assertAlmostEqual(calculator(2), 12.566370614359172)
        
    def test_area_zero_radius(self):
        # Test that radius 0 returns 0 area
        self.assertEqual(calculator(0), 0)
        
    def test_area_float_radius(self):
        # Test with a floating point radius
        self.assertAlmostEqual(calculator(2.5), 19.634954084936208)
        
    def test_negative_radius(self):
        # Test that negative radius raises a ValueError
        with self.assertRaises(ValueError):
            calculator(-1)

if __name__ == '__main__':
    unittest.main()
