import pandas as pd
import numpy as np

csv_file = "./data/Food_Inspections_after_openrefine.csv"
df = pd.read_csv(csv_file)

print(df.head())

def check_result(result_column, column_name, violation_str):
	if result_column:
		print(column_name + " contains " + violation_str + ":")
		for entry in result_column:
			print(entry)
	else:
		print('No ' + violation_str + ' on column ' + column_name)

# Function to check if each entry has leading/trailing whitespace characters
def check_leading_trailing_whitespace(df, column_name):
    column = df[column_name]
    has_whitespace = column.str.startswith(' ') | column.str.endswith(' ')
    if has_whitespace.any():
        entries_with_whitespace = column[has_whitespace]
        return entries_with_whitespace.tolist()
    else:
        return False

# Function to check if each entry is a number (int or float) in the column
def check_numeric_column(df, column_name):
    column = df[column_name]
    numeric_entries = []
    for entry in column:
        if not pd.api.types.is_numeric_dtype(np.array([entry])):
            numeric_entries.append(entry)

    return numeric_entries

# Function to check if each entry has at least one lowercase character in the column
def check_any_lowercase(df, column_name):
    return df[column_name].str.contains(r'[a-z]').all()

for col in ['Address', 'Violations']:
	result_column = check_leading_trailing_whitespace(df, col)
	check_result(result_column, col, "leading/trailing whitespace")
        
for col in ['Inspection ID', 'License #', 'Zip', 'Latitude', 'Longitude']:
	result_column = check_numeric_column(df, col)
	check_result(result_column, col, "non-numeric type")

for col in ['DBA Name', 'AKA Name', 'Address', 'City', 'Violations']:
	result_column = check_any_lowercase(df, col)
	check_result(result_column, col, "lowercase characters")