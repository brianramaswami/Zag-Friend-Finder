import csv
import random

FilePath = 'data.csv';


##LocalFilePath = './data.csv';

#################
# USEFUL FUNCTIONAL FUNCTIONS (pun intended)
def append(lst, elem):
    return lst + [elem]


def extend(lst1, lst2):
    return lst1 + lst2


#################

def readData():
    data = [];

    with open(FilePath, 'r') as f:
        r = csv.reader(f, delimiter=',');
        row1 = next(r);

        for row in r:
            tempList = row;
            data.append(tempList);
        ##            tempList[0] = User(tempList[0],tempList[1],tempList[2],tempList[3],tempList[4],tempList[5],
        ##                               tempList[6],tempList[7],tempList[8],tempList[9],tempList[10],tempList[11]);
        #      print('.....DONE');
        return data;


def writeData(list, data):
    with open(FilePath, 'a') as f:
        w = csv.writer(f, delimiter=',');
        w.writerow(list);

        # UPDATES DATA LIST RE-READS CSV NOT APPENDING LIST
        data = readData();


def createData(Data, count):
    with open(FilePath, 'r') as f:
        r = csv.reader(f, delimiter=',');
        Questions = next(r);
        print('Entering New User Data')
        # print(Questions);
        # print(len(Questions))
        tempList = [count];
        for question in Questions:
            question = (question + ": ")
            A = random.randint(1,10)
            tempList.append(A);
        algorithm(tempList)
        print(tempList);
        writeData(tempList, Data);

def algorithm(tempList):
    temp = []
    value = 0
    x = 2
    while (x<25):
        mult = int(tempList[x])
        sum = int(tempList[x+1]) + int(tempList[x+2]) + int(tempList[x+3])
        total = mult*sum
        temp.append(total)
        x = x+4
    for i in range (0,5):
        value = value + temp[i]
    tempList.append(value)



def analyzeData(Data):
    count = (len(Data)) - 1
    print(count)
    showData(Data)
    rowNum = input("\nSelect your line: ")
    rowNum = int(rowNum)-1
    person = Data[rowNum][1]
    friend = 'Friend'
    close = 10000000
    while (count>=0):
        temp = abs(int(Data[rowNum][26])-int(Data[count][26]))
        if(temp < close and rowNum != count):
            close = abs(int(Data[rowNum][26])-int(Data[count][26]))
            friend = Data[count][1]
        count = count -1
    print(person + " - The person you're most compatiable with is: " + friend)


def showData(Data):
    print('\nDISPLAYING CURRENT DATA: \n')
    print('-------------------------------------');
    print('');
    for row in Data:
        print(row);
        print('');
    print('-------------------------------------');

