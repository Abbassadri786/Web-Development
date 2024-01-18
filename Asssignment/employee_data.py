import pandas as pd
from datetime import datetime, timedelta

def analyze_employee_data(file_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(file_path)

    # Convert the 'Time' and 'Time Out' columns to datetime objects
    df['Time'] = pd.to_datetime(df['Time'])
    df['Time Out'] = pd.to_datetime(df['Time Out'])

    # Sort the DataFrame by 'Employee Name' and 'Time' for easier analysis
    df.sort_values(by=['Employee Name', 'Time'], inplace=True)

    # Initialize variables to store results
    employees_7_consecutive_days = set()
    employees_less_than_10_hours_between_shifts = set()
    employees_more_than_14_hours_single_shift = set()

    # Iterate through each employee's data
    for name, employee_data in df.groupby('Employee Name'):
        # Reset index for easier calculations
        employee_data.reset_index(drop=True, inplace=True)

        # Check for 7 consecutive days
        for i in range(len(employee_data) - 6):
            if (employee_data['Time'][i + 6] - employee_data['Time'][i]).days == 6:
                employees_7_consecutive_days.add(name)
                break

        # Check for less than 10 hours between shifts but greater than 1 hour
        for i in range(1, len(employee_data)):
            time_difference = employee_data['Time'][i] - employee_data['Time Out'][i - 1]
            if 1 < time_difference.total_seconds() / 3600 < 10:
                employees_less_than_10_hours_between_shifts.add(name)
                break

        # Check for more than 14 hours in a single shift
        for i in range(len(employee_data)):
            shift_duration = (employee_data['Time Out'][i] - employee_data['Time'][i]).total_seconds() / 3600
            if shift_duration > 14:
                employees_more_than_14_hours_single_shift.add(name)
                break

    # Print the results
    print("Employees who have worked for 7 consecutive days:")
    for employee in employees_7_consecutive_days:
        print(employee)

    print("\nEmployees who have less than 10 hours between shifts but greater than 1 hour:")
    for employee in employees_less_than_10_hours_between_shifts:
        print(employee)

    print("\nEmployees who have worked for more than 14 hours in a single shift:")
    for employee in employees_more_than_14_hours_single_shift:
        print(employee)

# Assuming the input file is a CSV file with the specified columns
file_path = 'path/to/your/input/file.csv'
analyze_employee_data(file_path)
