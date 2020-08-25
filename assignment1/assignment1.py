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

    total_sum = 0
    counter = 0

    for values in data:
        total_sum = values+total_sum
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

    #large string of entire contents of file
    file_string = f.read()

    #replace all commas in csv file with blank space
    file_no_commas = file_string.replace(',','')

    #create a list of string values
    file_csv = file_no_commas.split()

    #create a list of int values
    for value in file_csv:
        data.append(int(value))

    #sort data in order from lowest to highest value
    sorted_data = sorted(data)

    return sorted_data


if __name__ == '__main__':

    data = create_data()
    print("The data is: " + str(data))

    mean = calc_mean(data)
    print("The mean is: " + str(mean))

    median = calc_median(data)
    print("The median is: " + str(median))

    std_dev = calc_std_dev(data)
    print("The standard deviation is: " + str(std_dev)) 
