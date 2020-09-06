#!/usr/bin/env python3
#chmod +x generate_report.py


import os 
import csv 
#First, it reads a CSV file containing a list of the employees in the organization. 
# #Second, it generates a report of the number of people in each department in a plain text file.
def read_employees(csv_file_location):
    '''
    This function receives a CSV file as a parameter and returns a list of dictionaries from that file. 

    DictReader creates an object that operates like a regular reader (an object that iterates over lines
    in the given CSV file), but also maps the information it reads into a dictionary where keys are given
    by the optional fieldnames parameter. If we omit the fieldnames parameter, the values in the first row
    of the CSV file will be used as the keys. So, in this case, the first line of the CSV file has the keys
    and so there's no need to pass fieldnames as a parameter.

    We also need to pass a dialect as a parameter to this function. 
    There isn't a well-defined standard for comma-separated value files, 
    so the parser needs to be flexible. Flexibility here means that there are many parameters
    to control how csv parses or writes data.
    Rather than passing each of these parameters to the reader and writer separately, we group them together
    conveniently into a dialect object.

    Dialect classes can be registered by name so that callers of the CSV module don't need to know
    the parameter settings in advance. We will now register a dialect empDialect.
    '''
        with open(csv_file_location) as csvfile:
                csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
                employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
                employee_list = []
                for data in employee_file:
                    employee_list.append(data)
                return employee_list

def process_data(employee_list):
    '''
    Receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount.
    '''
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
        department_data = {}
    #This uses the set() method, which converts iterable elements to distinct elements.
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

def write_report(dictionary, report_file):
    '''
    his function writes a dictionary of department: amount to a file.

    The report should have the format:

    <department1>: <amount1>

    <department2>: <amount2>
    '''
    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()

employee_list = read_employees('/home/student-04-c96131948f11/data/employees.csv')
dictionary = process_data(employee_list)
write_report(dictionary, '/home/student-04-c96131948f11/data/report.txt')


