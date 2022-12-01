# HTMLTableMaster
A python package to manipulate HTML tables easily

## Installting The Package
--------------------
` pip install HTMLTableMaster`


## Getting Started
---------------------
You need the following two modules into your project. Please note that the cleaning funciton is optional.

`from HTMLTableMaster.HTMLTable import HTMLTable`


## Regular Use Logic
---------------------
> - The Package is designed to be used with a single line code , But you can use it in the regular manner
> - First Step would be to create an object from HTMLTable class

```
file = open("data.html" , "r")
htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True))
```      

> - First parameter specifies the the html table in string format.
> - Second parameter specifies the column that shoud be used to identify the rows to be murged (Refer Note 1).
> - Third parameter specifies weather the table has a heading or not in bool 
> - After creation of the objects you can call these methods 

```
htmlTable = htmlTable.murgeRows([0 ,1, 2 ])

htmlTable =htmlTable.removeColumn([-1])

print(htmlTable..getString())

```

> - murgeRows() method accepts a list with column indeces to be murged by the HTMLTableMaster.
> - removeColumn() method can be used to remove entire columns from the existing HTMLTableMaster.



## Single Line Use Logic
---------------------
- > HTMLTableMaster can be used with just one line to quickly manipulate HTML tables.

#### Senario 1
`htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).murgeRows([0 ,1, 2 ]).removeColumn([-1]).getString()`

#### Senario 2
`htmlTable = HTMLTable(file.read() , -1 , hasHeading=(True)).removeColumn([-1]).getString()`



### Note 1
---------------------
> - This is the second parameter that is passed to the HTMLTable constrtor.
> - You can use regular python indexing format to specify this number Ex: 0 , 1  , 2 or -1 , -2 , -3.
> - HTMLTableMaster will murge the rows based on the values given in this column






