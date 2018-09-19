import unittest
import json
import pprint
from autogroup import *
# from network import Network
from helper import FormatHelper




class TestFormatHelper(unittest.TestCase):

    def test_open_json_file(self):
        file_path = './sample_payloads/sample_members.json'
        format_helper = FormatHelper()
        test_json_object = format_helper.open_json_file(file_path)
        test_value = test_json_object[0]['name']
        test_result = 'Dragon Tran'
        self.assertEqual(test_value, test_result)

    def test_remove_non_student_groups(self):
        file_path = './sample_payloads/test_groups.json'
        format_helper = FormatHelper()
        groups_list = format_helper.open_json_file(file_path)
        filtered_group_list = format_helper.remove_non_student_groups(groups_list)
        self.assertEqual(len(filtered_group_list), 1)

    def test_parse_group_info(self):
        file_path = './sample_payloads/test_groups.json'
        format_helper = FormatHelper()
        groups_list = format_helper.open_json_file(file_path)
        group_info_list = format_helper.parse_group_info(groups_list)
        test_value = [(0, 'test group 1'), (0, 'test group 2')]
        self.assertEqual(group_info_list, test_value)

    def test_parse_group_members(self):
        file_path = './sample_payloads/sample_members.json'
        format_helper = FormatHelper()
        test_json_object = format_helper.open_json_file(file_path)
        test_group_info = format_helper.parse_group_members(test_json_object)
        test_value = [1, 2]
        self.assertEqual(test_group_info, test_value)

    def test_format_group_member_string(self):
        sample_group_list = [1, 2]
        format_helper = FormatHelper()
        test_output = format_helper.format_group_member_string(sample_group_list)
        test_value = '1, 2'
        self.assertEqual(test_output, test_value)

    # def test_get_network_call(self):
    #     network = Network()
    #     sample_endpoint = 'https://jsonplaceholder.typicode.com/todos/1'
    #     response = network.get_network_call(sample_endpoint)
    #     self.assertIsNotNone(response)



if __name__ == '__main__':
    unittest.main()
