from network import Network
from helper import FormatHelper


def main():
    network_helper = Network()
    helper = FormatHelper()
    group_json = network_helper.get_groups()
    filtered_group_json = helper.remove_non_student_groups(group_json)
    group_id_name_list =  helper.parse_group_info(filtered_group_json)

    for group in group_id_name_list:
        group_id, group_name  = group[0], group[1]
        members_json = network_helper.get_students_from_group_id(group_id)
        members_id_list =  helper.parse_group_members(members_json)
        members_list_string =  helper.format_group_member_string(members_id_list)
        new_group_id = network_helper.make_group(group_name)
        network_helper.add_members_to_group(members_list_string, new_group_id)
        network_helper.delete_student_made_group(group_id)


if __name__ == "__main__":
    main()
