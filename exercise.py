# Without Pandas or third party libraries, pure Python or standard lib only

# 1 - Load the data from the nat2021 file you have downloaded
# 2 - Create a function to count the number of firstnames used by less than 100 persons from 1900 to this date
# 3 - Create a function to count the number of persons for a specified firstname since 1900 and for a specific year
# 4 - Create a function to list the X most popular firstname for year Y (X and Y being argument of the function)
# 5 - Create a function to count the number of unique firstnanes per year from 1900 and for the whole period
# 6 - Compute the ratio of girls over boys per year from 1900
# 7 - Find the list of firstnames that have remained among the 200 most popular in the whole period
# 8 - Which firstname with at least 50 births per year that had the strongest compound annual growth rate in the last 10 years


import csv


#2 function to count the number of firstnames used by less than 100 persons from 1900 to this date
def count_firstname_less_than_100_from_1900(csv_data):
    name_quantity = {}
    for line in csv_data:
        # print(type(line))
        gender, name, year, quantity = line
        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0

        if name in name_quantity:
            name_quantity[name] += quantity
        else:
            name_quantity[name] = quantity

    names_with_total_quantity_less_than_100 = [name for name, total_quantity in name_quantity.items() if total_quantity < 100]
    return len(names_with_total_quantity_less_than_100)



#3 function to count the number of persons for a specified firstname since 1900 and for a specific year
def count_person_specified_name_specified_year_since_1900(specified_name, specified_year, csv_data):
    specified_name_counter = 0
    specified_name_in_specified_year = 0
    for line in csv_data:
        # print(line)
        gender, name, year, quantity = line
        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0

        if name == specified_name:
            specified_name_counter += quantity
        if name == specified_name and year == specified_year:
            specified_name_in_specified_year += quantity
    return (specified_name_counter, specified_name_in_specified_year)


# 4 - Create a function to list the X most popular firstname for year Y (X and Y being argument of the function)
def list_x_most_popular_name_for_year_y(x, year_y, csv_data):
    names_for_year_y = {}
    for line in csv_data:
        # print(type(line))
        gender, name, year, quantity = line
        quantity = int(quantity)
        if year !='XXXX':
            year = int(year)
        else:
            year = 0
        if year == year_y:
            if name not in names_for_year_y:
                names_for_year_y[name] = quantity
            else:
                names_for_year_y[name] += quantity
    sort_names_by_quantity = sorted(names_for_year_y.items(), key = lambda item: item[1])
    return sort_names_by_quantity[-x:]


#5 function to count the number of unique firstnanes per year from 1900 and for the whole period
def count_unique_name_per_year_from_1900_and_whole(csv_data):
    unique_name_year = {}
    unique_name_whole = set()
    for line in csv_data:
        # print(line)
        gender, name, year, quantity = line

        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0

        if year !='XXXX':
            year = int(year)
        else:
            year = 0

        if year >= 1900:
            if year not in unique_name_year:
                unique_name_year[year] = {name}
            else: 
                unique_name_year[year].add(name)

    for name in unique_name_year.values():
        unique_name_whole.update(name)
    return (unique_name_year, len(unique_name_whole))

#6 Compute the ratio of girls over boys per year from 1900
def compute_ratio_girls_over_boys(csv_data):
    # asume gender 1 is girl and 2 is boy 
    girl_num = 0
    boy_num = 0

    for line in csv_data:
        # print(line)
        gender, name, year, quantity = line
        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0
        if gender == '2':
            girl_num += quantity
        else:
            boy_num += quantity
    return( girl_num/boy_num)

#7 Find the list of firstnames that have remained among the 200 most popular in the whole period
def find_most_popular_name_among_200(csv_data):
    name_quantity = {}
    for line in csv_data:
        # print(type(line))
        gender, name, year, quantity = line
        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0

        if name in name_quantity:
            name_quantity[name] += quantity
        else:
            name_quantity[name] = quantity
    sorted_names_quantity = sorted(name_quantity.items(), key= lambda item: item[1])
    return sorted_names_quantity[-200:]

#8 Which firstname with at least 50 births per year that had the strongest compound annual growth rate in the last 10 years
def determine_strongest_compound_annual_growth_rate_last_10_year(csv_data):
    delta_year = 10
    name_quantity_2012 = {}
    name_quantity_2022 = {}
    for line in csv_data:
        # print(type(line))
        gender, name, year, quantity = line

        if int(quantity):
            quantity = int(quantity)
        else:
            quantity = 0

        if year == "2012":
            if name in name_quantity_2012:
                name_quantity_2012[name] += quantity
            else:
                name_quantity_2012[name] = quantity

        if year == "2022":
            if name in name_quantity_2012:
                name_quantity_2022[name] += quantity
            else:
                name_quantity_2022[name] = quantity
        
    return name_quantity



#1 load the file 

with open("./nat2022.csv", encoding="utf8") as file:
    csv_reader = csv.reader(file, delimiter=';')
    # remove header 
    next(csv_reader, None)
    csv_reader = list(csv_reader)
    print(determine_strongest_compound_annual_growth_rate_last_10_year(csv_reader))


 

