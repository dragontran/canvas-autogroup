import requests
import config


class Network:

    API_LINK = 'https://canvas.ou.edu/api/v1/'
    COURSE_ID = config.COURSE_ID
    GROUP_CATEGORY_ID = config.GROUP_CATEGORY_ID
    HEADER = {'Authorization' : 'Bearer ' + config.API_KEY }

    def get_groups(self):
        endpoint = 'courses/%s/groups?per_page=100' % self.COURSE_ID
        response = self.get_network_call(endpoint)
        return response

    def get_students_from_group_id(self, group_id):
        endpoint = 'groups/%s/users' % group_id
        response = self.get_network_call(endpoint)
        return response

    def make_group(self, group_name):
        endpoint = 'group_categories/%s/groups' % self.GROUP_CATEGORY_ID
        body = { 'name': group_name }
        response = self.post_network_call(endpoint, body)
        return response["id"]

    def add_members_to_group(self, member_string, group_id):
        endpoint = 'groups/%s' % group_id
        body = { 'members' : member_string }
        response = self.put_network_call(endpoint, body)
        return response

    def delete_student_made_group(self, group_id):
        endpoint = 'groups/%s' % group_id
        response = self.delete_network_call(endpoint)
        return response

    def delete_network_call(self, endpoint):
        response = requests.delete(self.API_LINK + endpoint, headers = self.HEADER)
        return response.json()

    def post_network_call(self, endpoint, body):
        response = requests.post(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()

    def get_network_call(self, endpoint):
        response = requests.get(self.API_LINK + endpoint, headers = self.HEADER)
        return response.json()

    def put_network_call(self, endpoint, body):
        response = requests.put(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()
