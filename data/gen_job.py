import pandas as pd

code_list = ['C05', 'J3', 'L2', 'DF1', 'U3', 'A1', 'DF4']
title_list = ['Apple', 'Make', 'Operate', 'Horse', 'Watch', 'Construct', 'Plan']
description_list = ['Slice', 'Horse', 'Pop', 'Face', 'Break', 'House', 'Itch']
worker_id_list = [1, 3, 1, 5, 2, 3, 1]
manager_list = [1, 1, 1, 2, 3, 4, 2]

if __name__ == '__main__':
    df = pd.DataFrame(
        {
            "code": code_list,
            "title": title_list,
            "description": description_list,
            "workerID": worker_id_list
        }
    )

    # export to array of jsons
    df.to_json('create_job.json', orient='records')
