"""
File: assignment1.py
Author: Phil Wood
Date: 08/25/2020
Section: 01
Email: pwood3@umbc.edu
Description: This program reads in a filename supplied at the command line
             and returns the mean, median, and standard deviation
"""

import math

def calc_mean(data, weight):

    """
    A function to calculate the mean
    Preconditions: data must be in a list
    Postconditions: mean must be returned
    :param data: the list of data
    :return: the mean of the data
    """

    total_sum = 0.0
    counter = 0

    for animals in data:
        total_sum = animals[weight] + total_sum
        counter = counter+1

    mean = total_sum/counter

    return mean

def calc_median(data, weight):

    """
    A function to calculate the median 
    Preconditions: data must be in a SORTED list
    Postconditions: median must be returned
    :param data: the list of data
    :return: the median of the data
    """
    counter = 0

    #if len of list is an even number
    if len(sorted(data)) % 2 == 0:

        while counter<len(data)/2:
            median = (data[counter][weight] + data[counter+1][weight])/2
            counter = counter+1

    #if len of list is an odd number
    else:

        while counter<(len(data)/2):
            median = data[counter][weight]
            counter = counter+1

    return median


def calc_std_dev(data, weight):
    
    """
    A function to calculate the standard deviation
    of the values in the csv file
    Preconditions: mean must be calculated 
    Postconditions: returns standard deviation 
    :param data: the list of data
    :return: the standard deviation of the data 
    """

    #to compute the std_dev, you calc the difference between each value
    #and the mean(the variance), and square it. then you find the mean
    #of all of these squared variances and take the sqr root of it

    variances = []
    mean = calc_mean(data)

    for values in data:
        variances.append((values-mean)**2)
        
    mean_variances = calc_mean(variances)

    std_dev = math.sqrt(mean_variances)

    return std_dev


def create_data():

    """
    A function to create a sorted list of values from
    an csv file
    Preconditions: user must enter a csv file 
    Postconditions: returns a list of sorted intergers 
    :param data: None
    :return: a list of sorted ints
    """

    #list to hold values of csv file
    data = []
   
    file_name = input("Please enter the name of the csv file \n")

    f = open(file_name + ".csv")

    #  list to store animals
    animals = []

    count = 0

    # print(f.read())
    for line in f.readlines():
        
        # skip the first line of file
        if count > 0:
            # delete \n characters
            line = line.replace('\n', '')

            # turn each line into an array
            line_array = line.split(',')

            # convert all values from strings to floats
            line_array[1] = float(line_array[1])
            line_array[2] = float(line_array[2])

            # info for each animal is stored in a dict
            animal = {
                'Species': line_array[0],
                'Bodyweight': line_array[1],
                'Brainweight': line_array[2]
            }

            animals.append(animal)

        count = count + 1

    return animals

def sort_data(data):

    """
    A function to sort data values
    Preconditions: data list must be created
    Postconditions: returns a list of sorted values 
    :param data: data
    :return: a list of sorted floats
    """

    




if __name__ == '__main__':

    data = create_data()

    mean_bodyweight = calc_mean(data, 'Bodyweight')
    print("The mean is: " + str(mean_bodyweight))

    # median_bodyweight = calc_median(data, 'Bodyweight')
    # print("The median is: " + str(median_bodyweight))

    # std_dev_bodyweight = calc_std_dev(data, 'Bodyweight')
    # print("The standard deviation is: " + str(std_dev_bodyweight)) 

    mean_brainweight = calc_mean(data, 'Brainweight')
    print("The mean is: " + str(mean_brainweight))

    # median_brainweight = calc_median(data, 'Brainweight')
    # print("The median is: " + str(median_brainweight))

    # std_dev_brainweight = calc_std_dev(data, 'Brainweight')
    # print("The standard deviation is: " + str(std_dev_brainweight)) 

    print()
