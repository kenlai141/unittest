import sys
sys.path.insert(0, r"C:\Users\ken_x1c\Documents\Python Scripts\unittest_app\app")

import unittest
from unittest.mock import patch, MagicMock

from controller import controller_method

class TestController(unittest.TestCase):
    
    @patch("models.data_model.datamodel", return_value="mocked")
    def test_controller(self, mock_datamodel_method):
        intended_input = "input"
        controller_method(intended_input)
        


if __name__ == "__main__":
    unittest.main()