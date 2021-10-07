import csv


########################################################################################################################
#                                                 NOTES
# In Main each choice should rely on a function that will return the correct info
########################################################################################################################
def open_file():
    with open('Company_DB - Sheet1.csv') as db:
        company_db = csv.reader(db)
        company_db2 = []
        for row in company_db:
            company_db2.append(row)
        return company_db2


def get_age():
    dict_age = {}
    with open('Company_DB - Sheet1.csv') as db:
        company_db = csv.reader(db)
        for row in company_db:
            dict_age.update({row[3]: row})
    print(dict_age)
    start_age = input('Enter start age: ')
    end_age = input('Enter end age: ')
    for numb in range(int(start_age), int(end_age)+1):
        pass



def main():
    file = open_file()
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
            pass
        elif prompt == '3':
            pass
        elif prompt == '4':
            pass
        elif prompt == '5':
            pass
        elif prompt == '6':
            run = False
        else:
            print('Invalid Input')


main()
