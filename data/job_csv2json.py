import pandas as pd


if __name__ == '__main__':
    df = pd.read_csv('job_data.csv', header=0, names=['code', 'title', 'description', 'workerID'])

    # export to array of jsons
    df.to_json('create_job_requests.json', orient='records')
