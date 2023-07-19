import pandas as pd
import numpy as np

def check_result(result_column, column_name, violation_str):
	if len(result_column):
		print(column_name + " contains " + violation_str + ": " + str(len(result_column)))
		# for entry in result_column:
		# 	print(entry)
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
        return []

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
    # return df[column_name].str.contains(r'[a-z]').all()
	return df[column_name][df[column_name].str.contains(r'[a-z]', na=False)]

# Function to check for outliers using z-scores
def check_outliers(df, column_name, threshold=4.1):
    z_scores = (df[column_name] - df[column_name].mean()) / df[column_name].std()
    outlier_indices = z_scores.abs() > threshold
    return df[column_name][outlier_indices].tolist()

def check_duplicate(df, column_name):
	return df[df.duplicated(column_name, keep=False)]

def check_categories(df, column_name):
	col_dict = {}
	for rec in df[column_name]:
		if rec not in col_dict:
			col_dict[rec] = 1
		else:
			col_dict[rec] += 1
	
	return col_dict