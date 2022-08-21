from agents.job_agent import JobAgent
import pandas as pd
import json


def create_jobs():
    # load job data from csv
    job_df = pd.read_csv('../data/job_data.csv', header=0)

    # identify the job manager and the job dto
    job_managers = job_df.loc[:, 'manager']
    create_job_dto = json.loads(job_df.loc[:, ['code', 'title', 'description', 'workerID']].to_json(orient='records'))

    # login as the manager
    # create job using the job dto
    for manager, job_request in zip(job_managers, create_job_dto):
        job_agent = JobAgent(username=manager.lower(), password='password')
        job_agent.create_job(job_request)


if __name__ == "__main__":
    create_jobs()
