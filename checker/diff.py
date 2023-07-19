import pandas as pd
import numpy as np
from quality import *

csv_file_raw = "./data/Food_Inspections_RAW.csv"
df_raw = pd.read_csv(csv_file_raw)
csv_file_cleaned = "./data/Food_Inspections_after_openrefine_after_python_cleaning.csv"
df_cleaned = pd.read_csv(csv_file_cleaned)

print("CSV Raw data Head:")
print(df_raw.head())

print("\n\nBefore and After Comparison:\n")

for col in ['Address', 'Violations']:
	print("raw CSV without cleaning:")
	result_column1 = check_leading_trailing_whitespace(df_raw, col)
	check_result(result_column1, col, "leading/trailing whitespace")
	print("CSV after cleaning:")
	result_column2 = check_leading_trailing_whitespace(df_cleaned, col)
	check_result(result_column2, col, "leading/trailing whitespace")
        
for col in ['Inspection ID', 'License #', 'Zip', 'Latitude', 'Longitude']:
	print("raw CSV without cleaning:")
	result_column1 = check_numeric_column(df_raw, col)
	check_result(result_column1, col, "non-numeric type")
	print("CSV after cleaning:")
	result_column2 = check_numeric_column(df_cleaned, col)
	check_result(result_column2, col, "non-numeric type")
	print('\n')

for col in ['DBA Name', 'AKA Name', 'Address', 'City', 'Violations']:
	print("raw CSV without cleaning:")
	result_column1 = check_any_lowercase(df_raw, col)
	check_result(result_column1, col, "lowercase characters")
	print("CSV after cleaning:")
	result_column2 = check_any_lowercase(df_cleaned, col)
	check_result(result_column2, col, "lowercase characters")
	print('\n')

for col in ['Latitude','Longitude']:
	print("raw CSV without cleaning:")
	result_column1 = check_outliers(df_raw, col)
	check_result(result_column1, col, "Outliers")
	print("CSV after cleaning:")
	result_column2 = check_outliers(df_cleaned, col)
	check_result(result_column2, col, "Outliers")
	print('\n')

for col in ['Inspection ID']:
	print("raw CSV without cleaning:")
	result_column1 = check_duplicate(df_raw, col)
	check_result(result_column1, col, "Inspection ID")
	print("CSV after cleaning:")
	result_column2 = check_duplicate(df_cleaned, col)
	check_result(result_column2, col, "Inspection ID")
	print('\n')

for col in ['Results', 'Risk']:
	print("raw CSV without cleaning:")
	result_dict1 = check_categories(df_raw, col)
	print(result_dict1)
	print("CSV after cleaning:")
	result_dict2 = check_categories(df_cleaned, col)
	print(result_dict2)
	print('\n')