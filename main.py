import pandas as pd
from pathlib import Path

# Get CSV files in the data folder
data_folder = Path("data")

# Read each CSV file
file_paths = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]
dfs = [pd.read_csv(data_folder / file) for file in file_paths]

# Step 2: Filter rows where "product" is "pink morsel"
filtered_dfs = [df[df['product'] == 'pink morsel'] for df in dfs]

# Step 3: Create a new column "sales" by multiplying "quantity" and "price"
for df in filtered_dfs:
    df['sales'] = df['quantity'] * df['price'].apply(lambda x: float(x.strip('$')))

# Step 4: List of formated dataframes
formatted_dfs = [df[['sales', 'date', 'region']] for df in filtered_dfs]

# Step 5: Concatenate the filtered and formatted data
final_df = pd.concat(formatted_dfs, ignore_index=True)

# Step 6: Save the final output to a new CSV file
final_df.to_csv("output.csv", index=False)
