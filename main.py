from classes import ParseData
import csv
import sys


def Main():
    count = 0
    while (exit != True):

        UserAnswer = input(
            "\nWould you like to? :  \n(1): Display Current Data.\n(2): Create New User \n(3): Analyze Data \n(4): Exit. \n")
        Data = ParseData.readData();

        if (UserAnswer == "1"):

            # READS IN DATA FROM CSV INTO NESTED ARRAY/LIST
            # print('');
            # print('READS IN DATA FROM CSV INTO NESTED ARRAY/LIST');
            Data = ParseData.readData();

            # DISPLAYS NESTED LIST
            # print('');
            # print('DISPLAYS NESTED LIST');
            ParseData.showData(Data);
        elif (UserAnswer == "2"):
            count = len(Data) + 1;
            #count = count + 1
            createData = ParseData.createData(Data, count);

        elif (UserAnswer == "3"):
            ParseData.analyzeData(Data);

        elif (UserAnswer == "4"):
            sys.exit();

        else:
            print("TRY AGAIN .. DUMMY \n");


Main();
