import csv


########################################################################################################################
#                                                 NOTES
# In Main each choice should rely on a function that will return the correct info
########################################################################################################################
def open_file():
    company_db_dict = {}
    name = 'row'
    numb = 1
    with open('Company_DB - Sheet1.csv') as db:
        company_db = csv.reader(db)
        for row in company_db:
            company_db_dict.update({name + str(numb): row})
            numb += 1
    return company_db_dict


def get_age():
    dict_age = open_file()
    key_list = []
    start_age = input('Enter start age: ')
    end_age = input('Enter end age: ')
    for numb in range(int(start_age), int(end_age) + 1):
        for key in dict_age:
            key_val = dict_age.get(key)
            if key_val[3] == str(numb):
                key_list.append(key)
    for key in key_list:
        print(dict_age[key])


def get_gender():
    dict_gender = open_file()
    key_list = []
    gender = input('Enter M for male, F for female: ')
    for key in dict_gender:
        key_val = dict_gender.get(key)
        if key_val[2] == gender.upper():
            key_list.append(key)
    for key in key_list:
        print(dict_gender[key])


def get_salary():
    dict_salary = open_file()
    key_list = []
    salary_start = input('Enter salary start: ')
    salary_end = input('Enter salary end: ')
    for key in dict_salary:
        key_val = dict_salary.get(key)
        for numb in range(int(salary_start), int(salary_end), 1000):
            if key_val[5] == str(numb):
                key_list.append(key)
    for key in key_list:
        print(dict_salary[key])


def get_date():
    dict_dates = open_file()
    key_list = []
    start_date = input('Enter start date MM/DD/YYYY: ')
    end_date = input('Enter end date MM/DD/YYYY: ')
    modified_date_end = \
        int(end_date.split('/')[0]) * 32 + int(end_date.split('/')[1]) + int(end_date.split('/')[2]) * 500
    modified_date_start = \
        int(start_date.split('/')[0]) * 32 + int(start_date.split('/')[1]) + int(start_date.split('/')[2]) * 500
    for key in dict_dates:
        key_value = dict_dates.get(key)
        key_value_s = \
            int(key_value[4].split('/')[0]) * 32 + \
            int(key_value[4].split('/')[1]) + \
            int(key_value[4].split('/')[2]) * 500
        if modified_date_start <= key_value_s <= modified_date_end:
            print(modified_date_start, modified_date_end, key_value_s)
            key_list.append(key)
    for key in key_list:
        print(dict_dates[key])


def get_position():
    dict_position = open_file()
    key_list = []
    position_enter = input('Enter 1 for Sales, 2 for Software, or 3 for Management: ')
    if position_enter == '1':
        choice = 'Sales'
    elif position_enter == '2':
        choice = 'Software'
    else:
        choice = 'Management'
    for key in dict_position:
        key_val = dict_position.get(key)
        if key_val[6] == choice:
            key_list.append(key)
    for key in key_list:
        print(dict_position[key])


def main():
    run = True
    while run:
        prompt = input('What kind of information do you wish to extract :\n'
                       'To get information about employee age type:  1\n'
                       'To get information about employee gender type:  2\n'
                       'To get information about employee salary type: 3\n'
                       'To get information about employee start date type: 4\n'
                       'To get information about employee department type: 5\n'
                       'To exit the database query type: 6\n')
        if prompt == '1':
            get_age()
            run = False
        elif prompt == '2':
            get_gender()
            run = False
        elif prompt == '3':
            get_salary()
            run = False
        elif prompt == '4':
            get_date()
            run = False
        elif prompt == '5':
            get_position()
            run = False
        elif prompt == '6':
            run = False
        else:
            print('Invalid Input')


main()
