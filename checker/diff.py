import pandas as pd
import numpy as np
from quality import *

csv_file_raw = "./data/Food_Inspections_RAW.csv"
df_raw = pd.read_csv(csv_file_raw)
csv_file_cleaned = "./data/Food_Inspections_after_openrefine_after_python_cleaning.csv"
df_cleaned = pd.read_csv(csv_file_cleaned)

print(df_raw.head())

for col in ['Address', 'Violations']:
	result_column1 = check_leading_trailing_whitespace(df_raw, col)
	check_result(result_column1, col, "leading/trailing whitespace")
	result_column2 = check_leading_trailing_whitespace(df_cleaned, col)
	check_result(result_column2, col, "leading/trailing whitespace")
        
for col in ['Inspection ID', 'License #', 'Zip', 'Latitude', 'Longitude']:
	result_column1 = check_numeric_column(df_raw, col)
	check_result(result_column1, col, "non-numeric type")
	result_column2 = check_numeric_column(df_cleaned, col)
	check_result(result_column2, col, "non-numeric type")

for col in ['DBA Name', 'AKA Name', 'Address', 'City', 'Violations']:
	result_column1 = check_any_lowercase(df_raw, col)
	check_result(result_column1, col, "lowercase characters")
	result_column2 = check_any_lowercase(df_cleaned, col)
	check_result(result_column2, col, "lowercase characters")

for col in ['Latitude','Longitude']:
	result_column1 = check_outliers(df_raw, col)
	check_result(result_column1, col, "Outliers")
	result_column2 = check_outliers(df_cleaned, col)
	check_result(result_column2, col, "Outliers")

for col in ['Inspection ID']:
	result_column1 = check_duplicate(df_raw, col)
	check_result(result_column1, col, "Inspection ID")
	result_column2 = check_duplicate(df_cleaned, col)
	check_result(result_column2, col, "Inspection ID")

for col in ['Results', 'Risk']:
	result_dict1 = check_categories(df_raw, col)
	print(result_dict1)
	result_dict2 = check_categories(df_cleaned, col)
	print(result_dict2)