import unittest
from unittest.mock import patch

from controller.controller import controller_method


class TestController(unittest.TestCase):

    def test_controller(self):
        with patch("models.data_model.datamodel") as mock_datamodel:
            mock_datamodel.data_model_method.return_value = "mock_value"
            intended_input = "input"
            res = controller_method(intended_input)
            self.assertEqual(res, "mock_value")

    @patch("models.data_model.datamodel")
    def test_controller_2(self, mock_datamodel):
        mock_datamodel.data_model_method.return_value = "mock_value"
        intended_input = "input"
        res = controller_method(intended_input)
        self.assertEqual(res, "mock_value")


if __name__ == "__main__":
    unittest.main()
