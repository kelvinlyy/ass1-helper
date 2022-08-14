import unittest
from agents.admin_agent import AdminAgent


class TestAdminAgent(unittest.TestCase):
    admin_agent = AdminAgent()

    def test_get_keycloak_id(self):
        self.assertEqual(self.admin_agent.get_keycloak_id(), '9dc44da1-3fbe-4e8c-83e0-a696c41574a1')

    def test_create_keycloak_user(self):
        response = self.admin_agent.create_keycloak_user({
            "firstName": "Ryan",
            "lastName": "Chan",
            "sex": "Male",
            "email": "ryan@test.com",
            "role": "worker",
            "username": "ryan",
            "password": "password"
        })

        expected_response = {
            "kc_id": "",
            "firstName": "Ryan",
            "lastName": "Chan",
            "sex": "Male",
            "email": "ryan@test.com",
            "role": "worker"
        }

        self.assertTrue(response['kc_id'])
        self.created_kc_id = response['kc_id']
        self.assertEqual(response['firstName'], expected_response['firstName'])
        self.assertEqual(response['lastName'], expected_response['lastName'])
        self.assertEqual(response['firstName'], expected_response['firstName'])
        self.assertEqual(response['sex'], expected_response['sex'])
        self.assertEqual(response['email'], expected_response['email'])
        self.assertEqual(response['role'], expected_response['role'])

    def test_delete_keycloak_user(self):
        response = self.admin_agent.delete_keycloak_user('')

        self.assertEqual(response, 200)


if __name__ == '__main__':
    unittest.main()
