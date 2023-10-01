import pandas as pd


# Load the first CSV file into a pandas DataFrame
df1 = pd.read_csv('Upload CSV file1')
print(df1.head())

# Load the second CSV file into another pandas DataFrame
df2 = pd.read_csv('Upload CSV file2')
print(df2.head())

# Perform a full outer join on a common column (e.g., 'common_column')
merged_df = pd.merge(df2, df1, on='month', how='outer')

# Removal of null values
Invest_Dis_Date1.isnull().sum()
dfresult = merge_df.dropna(axis=1)
print(dfresult)

# Save the merged DataFrame to a new CSV file
merged_df.to_csv('Stamp_Transport.csv', index=False)