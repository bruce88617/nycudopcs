import pandas as pd
import numpy as np


def pickStudent(num=3, path="1111-515401.csv"):
    df = pd.read_csv(path)

    nameList1 = list(df['Unnamed: 2'])[4:35]
    nameList2 = list(df['Unnamed: 3'])[4:35]
    nameList = np.array([nameList1, nameList2])

    presenters = []
    count = 0

    while len(presenters) < num:
        pickIndex = int(np.round((np.size(nameList, axis = 1) - 1) * np.random.uniform(size = 1)))
        ID = str(nameList[0, pickIndex])
        if ID not in presenters:
            presenters.append(ID)
            print('The', count + 1, 'presenter is', nameList[0, pickIndex], nameList[1, pickIndex])
            count += 1

