import pandas as pd

# create a sample DataFrame with the serial date numbers
df = pd.DataFrame({'Date': [731777, 731778, 731779, 731780, 731781, 731782, 731783, 731784, 731785, 731786, 731787]})
df['Date'] = df['Date'].astype(str)
df['Date'] = df['Date'].str.extract('(\d{4}-\d{2}-\d{2})').astype('datetime64[ns]')

# convert the 'Date' column to datetime objects
df['Date'] = pd.to_datetime(df['Date'], origin='1899-12-30')

print(df)




