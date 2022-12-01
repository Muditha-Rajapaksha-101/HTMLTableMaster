from HTMLTableMaster.HTMLTable import HTMLTable

if __name__ == "__main__":    
    file = open("data.html" , "r")
    htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).murgeRows([0 ,1, 2 ]).removeColumn([-1]).getString()
    #htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).removeColumn([-1]).getString()
    print(htmlTable)
    
    fileNew = open("output.html" , "w")
    fileNew.write(htmlTable)
    fileNew.close()
   