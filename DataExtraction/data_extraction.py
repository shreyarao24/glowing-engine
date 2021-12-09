
# This file contains the data extraction code for 3 different PDF formats.

# Code 1

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import pandas
import re

f = pandas.read_csv('C:/Users/Shreya/Desktop/file1.csv')

# creating a new dataframe to store all extracted data
final = pandas.DataFrame(columns=['Sr No.', 'Name', 'Student ID', 'Gender', 'Grade'])

# looping through each row in the dataframe
for row in f.itertuples():
    # splitting the information, which was stored as a string, into a list
    r = row[1].split(' ')

    # removing any empty strings in the list
    while r.count('') > 0:
        r.remove('')

    # extracting required information
    sr_no = r[0]
    sid = '*' + r[1] + r[2] + r[3]
    grade = r[4]

    if len(re.sub('[^a-zA-Z]+', '', r[5])) <= 2:
        name = re.sub('[^a-zA-Z]+', '', r[5]) + ' ' + re.sub('[^a-zA-Z]+', '', r[6])
    else:
        name = re.sub('[^a-zA-Z]+', '', r[5])

    if 'BOY' in r:
        gender = 'BOY'
    else:
        gender = 'GIRL'

    l = [sr_no, name, sid, gender, grade]
    # adding the final data to our new dataframe
    final.loc[len(final)] = l

# converting our pandas dataframe to a .csv file
final.to_csv('C:/Users/Shreya/Desktop/ctd files/file-name.csv')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Code 2

f = pandas.read_csv('C:/Users/Shreya/Desktop/file-name.csv', header=None)

# dropping duplicate rows - since headers were repeated on every new page of the pdf
f.drop_duplicates(keep='first', inplace=True)

# creating a new dataframe
final = pandas.DataFrame(columns=['Sr No.', 'Name', 'Student ID', 'Gender'])

for row in f.itertuples():
    r = str(row[1]).split(' ')

    while r.count('') > 0:
        r.remove('')

    if r[0].isnumeric() and len(r) > 1:
        sr_no = r[0]

        for i in range(0, len(r)):
            if len(r[i]) == 3 and r[i].isnumeric() and len(r[i + 1]) == 3 and r[i + 1].isnumeric():
                sid = '*' + r[i] + r[i + 1] + r[i + 2]
                break

        name = r[1]
        if r[2].isalpha():
            name = name + ' ' + r[2]

        if 'BOY' in r:
            gender = 'BOY'
        else:
            gender = 'GIRL'

        l = [sr_no, name, sid, gender]
        final.loc[len(final)] = l

final.to_csv('C:/Users/Shreya/Desktop/files/file-name.csv')

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Code 3

f = pandas.read_csv('C:/Users/Shreya/Desktop/file-name.csv', header=None)

final = pandas.DataFrame(columns=['Sr No.', 'Name', 'Student ID', 'Gender', 'Grade'])

for i in range(0, len(f), 2):
    r1 = f.iat[i, 0].split(' ')
    while r1.count('') > 0:
        r1.remove('')

    r2 = f.iat[i + 1, 0].split(' ')
    while r2.count('') > 0:
        r2.remove('')

    r = r1 + r2

    sr_no = r[0]

    if r[9].isnumeric():
        sid = '*' + r[1] + r[2] + r[9]
    else:
        sid = '*' + r[1] + r[2] + r[10]

    name = r[3] + ' ' + r[4]

    if 'BOY' in r:
        gender = 'BOY'
    else:
        gender = 'GIRL'

    if r[7].isnumeric():
        grade = r[7]
    else:
        grade = r[8]

    l = [sr_no, name, sid, gender, grade]
    final.loc[len(final)] = l

final.to_csv('C:/Users/Shreya/Desktop/files/file-name.csv')