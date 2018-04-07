from classes import ParseData
import csv


def Main():
    #READS IN DATA FROM CSV INTO NESTED ARRAY/LIST
    print('');
    print('READS IN DATA FROM CSV INTO NESTED ARRAY/LIST');
    Data = ParseData.readData();

    #DISPLAYS NESTED LIST
    print('');
    print('DISPLAYS NESTED LIST');
    ParseData.showData(Data);

    #SAMPLE NEW DATA
    print('');
    print('SAMPLE NEW DATA : ');
    newEntry = ["Spikes long lost girlfriend The Poodle","Spikes lfong lost girlfriend", "The Poodle", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A10", "A11"];
    print(newEntry);
    
    #ADD NEW DATA TO CSV
    print('');
    print('ADD NEW DATA TO CSV');
    ParseData.writeData(newEntry, Data);
    Data = ParseData.readData();

    print('NEW DATA SHOULD BE : ');
    print(Data);

    #DISPLAYS NESTED LIST
    print('');
    print('DISPLAYS NESTED LIST');
    ParseData.showData(Data);

    #TEST ANALYZE DATA
    print('');
    print('TEST ANALYZE DATA');
    ParseData.analyzeData(Data);







Main();
