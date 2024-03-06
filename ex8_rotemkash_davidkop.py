"""
======================================================================
ex8
======================================================================
Writen by: Rotem kashani, ID = 209073352,   login = rotemkash
	       David Koplev, ID = 208870279 ,    login = davidkop
This program run in an infinite loop until the user insert his choice,
if the user inserts choice number 1 the program shows the largest cities,
in addition to the names the program shows each city's postal code.
if the user inserts choice number 2 the program creates file, in the file there are
the names and the numbers of the files that their run has ended.
if the user inserts choice number 3 the program will end.
input: choice between 1-3
"""

import re


# shows the largest cities and their postal code
def Largest_City():
    # open files
    try:
        cities_file = open("2022_largest_cities.txt", "r")
        postal_code_file = open("us_postal_codes.csv", "r")
    except IOError:
        print("Can't open file in Largest_City.")

    l_cities = cities_file.readlines()  # holder for cities_file data
    p_codes = postal_code_file.readlines()  # holder for postal_code_file data
    cities_csv = dict()
    cities = []

    for line in range(1, len(l_cities)):
        cities.append(re.search(r'[a-zA-Z]+[\s]{0,1}[a-zA-Z]*[A-Z]', l_cities[line]).group()[0:-1])
    for line in range(1, len(p_codes)):
        information = re.search(r'([0-9]*),([a-zA-Z ]+)', p_codes[line])
        if information:
            cities_csv[information.group(2)] = information.group(1)

    for data in cities:
        if data in cities_csv.keys():
            print(data, cities_csv[data])


# function creates a file with the names and run time of all files it ran on
def runlog():
    # open files
    try:
        input_log = open("atoms2.log", "r")
        output_log = open("logfile.txt", "w")
    except IOError:
        print("Can't open file in runlog.")

    data = input_log.readlines()

    for line in range(0, len(data)):
        res = re.search(r"COMPLETED", data[line])

        if res:
            pid = re.search(r"[\d]+", data[line]).group() + " "
            name = re.search(r" ([a-zA-z]+.dat). \d{1,2}.\d{1,2}", data[line])
            if name:
                output_log.write(pid + " " + name.group(1) + "\n")


while True:
    choice = int(input('\nPlease enter your choice:\n'
                       '1 - To view largest cities\n'
                       '2 - To run on log file\n'
                       '3 - To exit the program\n'))
    if choice == 1:
        Largest_City()
    elif choice == 2:
        runlog()
    elif choice == 3:
        print("GoodBye")
        break
