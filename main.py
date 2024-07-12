import pandas as pd

data = {
    'col1': [2, 3, 4, 5],
    'col3': [6, 7, 8, 9],
    'col4': [10, 11, 12, 13],
    'col5': [14, 15, 16, 17]
}
numbers = [2, 3, 4, 5]

numbers[0]
data['col1']

df = pd.DataFrame(data)

# df.groupby('col1').count()
