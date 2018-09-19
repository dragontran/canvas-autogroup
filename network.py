import requests
import config


class Network:

    API_LINK = 'https://canvas.ou.edu/api/v1/'
    GROUP_PAGE_ID = config.GROUP_PAGE_ID
    GROUP_CATEGORY = config.GROUP_CATEGORY
    HEADER = {'Authorization' : 'Bearer ' + config.API_KEY }

    def get_groups(self):
        endpoint = 'courses/%s/groups?per_page=35' % self.GROUP_PAGE_ID
        response = self.get_network_call(endpoint)
        return response

    def get_students_from_group_id(self, group_id):
        endpoint = 'groups/%s/users' % group_id
        response = self.get_network_call(endpoint)
        return response

    def make_group(self, group_name):
        endpoint = 'group_categories/%s/groups' % self.GROUP_CATEGORY
        body = { 'name': group_name }
        response = self.post_network_call(endpoint, body)
        return response["id"]

    def add_members_to_group(self, member_string, group_id):
        endpoint = 'groups/%s' % group_id
        body = { 'members' : member_string }
        response = self.put_network_call(endpoint, body)
        return response

    def post_network_call(self, endpoint, body):
        response = requests.post(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()

    def get_network_call(self, endpoint):
        response = requests.get(self.API_LINK + endpoint, headers = self.HEADER)
        return response.json()

    def put_network_call(self, endpoint, body):
        response = requests.put(self.API_LINK + endpoint, headers = self.HEADER, data=body)
        return response.json()