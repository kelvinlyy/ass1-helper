import unittest
from agents.job_agent import JobAgent


class TestJobAgent(unittest.TestCase):
    job_agent = JobAgent()

    def test_create_job(self):
        create_job_request = {
            "code": "test_code",
            "title": "test_title",
            "description": "test_description",
            "workerID": 1
        }

        expected_job_response = {
            "id": 0,
            "code": "test_code",
            "title": "test_title",
            "description": "test_description",
            "status": "PROGRESS",
            "worker": {
                "id": 1,
                "kcId": "",
                "createdDate": "",
                "updatedDate": ""
            }
        }

        response = self.job_agent.create_job('kelvin', 'password', create_job_request)

        self.assertEqual(response['code'], expected_job_response['code'])
        self.assertEqual(response['title'], expected_job_response['title'])
        self.assertEqual(response['description'], expected_job_response['description'])
        self.assertEqual(response['code'], expected_job_response['code'])
        self.assertEqual(response['worker']['id'], expected_job_response['worker']['id'])

if __name__ == '__main__':
    unittest.main()
