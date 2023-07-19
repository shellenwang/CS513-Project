import pandas as pd
import numpy as np
import checker.quality as qual

def remove_duplicate(df, column_name):
    df.drop_duplicates(subset=[column_name], keep='first', inplace=True)
    return df

def remove_stardardize_format(df, column_name):
	col_dict = {}
	count = 0
	for i in range(len(df[column_name])):
		if df.at[i, column_name] not in col_dict:
			count += 1
			col_dict[df.at[i, column_name]] = count
			df.at[i, column_name] = col_dict[df.at[i, column_name]]
		else:
			df.at[i, column_name] = col_dict[df.at[i, column_name]]
	
	return col_dict

csv_file = "./data/Food_Inspections_after_openrefine.csv"
df = pd.read_csv(csv_file)

remove_duplicate(df, 'Inspection ID')
result_dict_results = remove_stardardize_format(df, 'Results')
print(result_dict_results)
result_dict_risk = remove_stardardize_format(df, 'Risk')
print(result_dict_risk)

df.to_csv("./data/Food_Inspections_after_openrefine_after_python_cleaning.csv", index=False)