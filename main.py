import pandas as pd
import os

# Step 1: Get CSV files in the data folder
DATA_DIRECTORY = "./data"
dfs = [pd.read_csv(f"{DATA_DIRECTORY}/{file_name}") for file_name in os.listdir(DATA_DIRECTORY)]

# Step 2: Filter rows where "product" is "pink morsel"
filtered_dfs = [df[df['product'] == 'pink morsel'] for df in dfs]

# Step 3: Create a new column "sales" by multiplying "quantity" and "price"
for df in filtered_dfs:
    df['sales'] = df['quantity'] * df['price'].apply(lambda x: float(x.strip('$')))

# Step 4: Create a list of dataframes with 'sales', 'date', 'region' columns only
formatted_dfs = [df[['sales', 'date', 'region']] for df in filtered_dfs]

# Step 5: Concatenate the filtered and formatted dataframes
final_df = pd.concat(formatted_dfs, ignore_index=True)

# Step 6: Save the final output to a new CSV file
final_df.to_csv("output.csv", index=False)