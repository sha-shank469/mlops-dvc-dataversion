import pandas as pd
import os

data = {
    'Name':['Alice','Bob','Charlie'],
    'Age': [25,30,40],
    'city':['NewYork','Los Angles','chicago']
}

df = pd.DataFrame(data)

# Adding new row to df for V2
new_row_loc = {'Name':'Shashank', 'Age':20, 'city':'Delhi'}
df.loc[len(df.index)] = new_row_loc

new_row_loc = {'Name':'Reddy', 'Age':19, 'city':'Andhra'}
df.loc[len(df.index)] = new_row_loc

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=False)

print(f"Csv file save to {file_path}")