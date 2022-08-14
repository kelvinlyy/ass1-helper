import json
from agents.job_agent import JobAgent


def create_jobs():
    with open('../data/create_job.json', 'rb') as f:
        create_job_requests = json.load(f)

    job_agent = JobAgent()
    manager_list = ['Joe', 'Joe', 'Joe', 'Zoe', 'Kelvin', 'Kelvin', 'Zoe']

    assert(len(create_job_requests) == len(manager_list))
    for i in range(len(create_job_requests)):
        job_agent.create_job(manager_list[i], 'password', create_job_requests[i])


if __name__ == "__main__":
    create_jobs()
