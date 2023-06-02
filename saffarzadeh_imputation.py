# Define the mappings for each variable
age_mapping = {1: range(0, 11), 2: range(11, 21), 3: range(21, 31)}
sex_mapping = {1: 'female', 2: 'male'}
working_mapping = {1: 'no', 2: 'yes'}
disabled_mapping = {1: 'no', 2: 'yes'}
jobType_mapping = {1: 'full time', 2: 'part time'}

# Define the input dataset
input_data = [
    {'age': 1, 'sex': 2, 'working': 2, 'disabled': 1, 'jobType': 1, 'totalWorkHrs': 40},
    {'age': 3, 'sex': 1, 'working': 1, 'disabled': 2, 'jobType': 2, 'totalWorkHrs': 25},
    {'age': 2, 'sex': 2, 'working': 1, 'disabled': 2, 'jobType': 1, 'totalWorkHrs': 63},
    {'age': 1, 'sex': 2, 'working': 2, 'disabled': 1, 'jobType': 1, 'totalWorkHrs': 0},
    {'age': 3, 'sex': 1, 'working': 1, 'disabled': 2, 'jobType': 2, 'totalWorkHrs': 0}, 
    {'age': 2, 'sex': 2, 'working': 1, 'disabled': 2, 'jobType': 1, 'totalWorkHrs': 0}
]


# Perform the hot deck imputation
for data_point in input_data:
    if data_point['totalWorkHrs'] > 0:
        data_point['imputed'] = False
    else:
        # Retrieve the values for the corresponding categories
        age_range = age_mapping[data_point['age']]
        sex_value = sex_mapping[data_point['sex']]
        working_value = working_mapping[data_point['working']]
        disabled_value = disabled_mapping[data_point['disabled']]
        job_type_value = jobType_mapping[data_point['jobType']]
        
        # Find the matching data points with non-zero totalWorkHrs
        matched_data = []
        for previous_data in input_data:
            if (previous_data['age'] in age_range and
                sex_mapping[previous_data['sex']] == sex_value and
                working_mapping[previous_data['working']] == working_value and
                disabled_mapping[previous_data['disabled']] == disabled_value and
                jobType_mapping[previous_data['jobType']] == job_type_value and
                previous_data['totalWorkHrs'] > 0):
                    matched_data.append(previous_data)
                
        if matched_data:
            data_point['totalWorkHrs'] = matched_data[0]['totalWorkHrs']
            data_point['imputed'] = True
        else:
            data_point['imputed'] = False

# Print the imputed dataset
print('input_data')
for data_point in input_data:
    print(data_point)
print('matched_data')
for matched_point in matched_data:
    print(matched_point)
