from method_2 import convert_json_table
import unittest

class Convert_JSON_To_Table_TestCase(unittest.TestCase):
    def test_return_message(self):
        message = convert_json_table()
        self.assertEqual(message, "HTML table generated")


if __name__ == '__main__':
    unittest.main()

