import pandas as pd

# Load the CSV 
df_raw = pd.read_csv("/Users/sa3/Portfolio-Project/incidents.csv", header=None)

# Print first 15 rows to inspect structure
print(df_raw.head(15))

# Assign column names manually, ensuring Row 8 is named "Date_Occurred"
df_raw.columns = ["col_" + str(i) for i in range(len(df_raw.columns))] 

# Rename the specific column
df_raw.rename(columns={"col_8": "Date_Occurred", "col_12": "Incident_Type", "col_13": "Incident_Count", "col_11": "Wday_Wnd","col_9": "Division","col_10": "TrainLine"} , inplace=True)

columns_to_drop = ["col_0", "col_1","col_2","col_3","col_4","col_5","col_6","col_7"]  
df_raw.drop(columns=columns_to_drop, inplace=True)

# Display column names to confirm
print(df_raw.columns)

# Save the cleaned CSV
df_raw.to_csv("/Users/sa3/Portfolio-Project/incidents_clean.csv", index=False)

print("File saved successfully!") 

print(df_raw.columns)
df_raw.head()