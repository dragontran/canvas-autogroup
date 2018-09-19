import json


class FormatHelper:

    def open_json_file(self, file_path):
        json_object = []
        with open(file_path) as json_file:
            json_object = json.load(json_file)
        return json_object

    def remove_non_student_groups(self, groups_list):
        new_groups_list = []
        for group in groups_list:
            if(group['role'] == "student_organized"):
                new_groups_list.append(group)
        return new_groups_list

    def parse_group_info(self, groups_list):
        group_info_tuple_list = []
        for group in groups_list:
            group_info_tuple_list.append((group["id"], group["name"]))
        return group_info_tuple_list

    def parse_group_members(self, member_list):
        output_member_list = []
        for member in member_list:
            output_member_list.append(member['id'])
        return output_member_list

    def format_group_member_string(self, group_member_list):
        output_string = str(group_member_list).strip('[]')
        return output_string
