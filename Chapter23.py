def getIntegers():
    int1, int2 = '', '' # Request the user's input here for two integers
    return int1,int2

def doOr(int1, int2):
    return (int1 or int2)# print the name to the console here

if __name__ == '__main__':
    int1, int2 = getIntegers()
    print doOr(int1,int2)