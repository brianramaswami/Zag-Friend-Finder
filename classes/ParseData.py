import csv

FilePath = './data/data.csv';
##LocalFilePath = './data.csv';

'''
#CREATING A CLASS USER FOR EVERY ENTRY

class User:
    def _init_(self,full_name,first_name, last_name, A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11):
        self.full_name = full_name;
        self.first_name = first_name;
        self.last_name = last_name;
        self.A1 = A1;
        self.A2 = A2;
        self.A3 = A3;
        self.A4 = A4;
        self.A5 = A5;
        self.A6 = A6;
        self.A7 = A7;
        self.A8 = A8;
        self.A9 = A9;
        self.A10 = A10;
        self.A11 = A11;

    def displayUser(self):
        print(self.full_name, '', self.first_name, '', self.last_name, '', self.A1, '', self.A2, '', self.A3, ''
              , self.A4, '', self.A5, '', self.A6, '', self.A7, '', self.A8, '', self.A9, '', self.A10,
              '', self.A11);
        
'''        




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
        print('.....DONE');
        return data;



def writeData(list, data):
    with open(FilePath, 'a') as f:
        w = csv.writer(f, delimiter=',');
        w.writerow(list);

        #UPDATES DATA LIST RE-READS CSV NOT APPENDING LIST
        data = readData();
    return data;



##def editData():




def analyzeData(Data):
    if(Data[1][4] <  Data[1][5]):
        print('True');


def showData(Data):
    print('-------------------------------------');  
    print('');
    for row in Data:
        print(row);
        print('');
    print('-------------------------------------');    




##def Main():
##    Data = readData();
##    showData(Data);
##    ##newEntry = ["Spikes long lost girlfriend The Poodle","Spikes long lost girlfriend", "The Poodle", "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "A10", "A11"];
##    ##writeData(newEntry);
####    analyzeData(Data);
##
##
##
##
##Main();
