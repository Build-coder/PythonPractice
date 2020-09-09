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

def calc_mean(data):

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
        # print(animals['Attributes']['Bodyweight'])
        total_sum = animals['Attributes']['Bodyweight'] + total_sum
        counter = counter+1

    mean = total_sum/counter

    return mean

def calc_median(data):

    """
    A function to calculate the median 
    Preconditions: data must be in a SORTED list
    Postconditions: median must be returned
    :param data: the list of data
    :return: the median of the data
    """
    counter = 0

    #if len of list is an even number
    if len(data) % 2 == 0:

        while counter<len(data)/2:
            median = (data[counter] + data[counter+1])/2
            counter = counter+1

    #if len of list is an odd number
    else:

        while counter<(len(data)/2):
            median = data[counter]
            counter = counter+1

    return median


def calc_std_dev(data):
    
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
                'Attributes':{
                    'Bodyweight': line_array[1],
                    'Brainweight': line_array[2]
                }
            }

            animals.append(animal)

        count = count + 1

    return animals

if __name__ == '__main__':

    data = create_data()

    mean = calc_mean(data)
    print("The mean is: " + str(mean))

    # median = calc_median(data)
    # print("The median is: " + str(median))

    # std_dev = calc_std_dev(data)
    # print("The standard deviation is: " + str(std_dev)) 

    print()
