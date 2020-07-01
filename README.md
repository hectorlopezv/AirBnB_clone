# AirBnB clone - The console

  

<p align="center">
<img src="https://camo.githubusercontent.com/8d76bb2b9f2eeeb22ba9236805e758b58eb7fdc4/68747470733a2f2f696d6775722e636f6d2f4f696c457358562e706e67">

</p>

  

## Description

-   A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
-   A website (the front-end) that shows the final product to everybody: static and dynamic
-   A database or files that store data (data = objects)
-   An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

  

## Usage
A command line interpreter to manipulate and visualize data.

Non-iterative mode:
 ```bash 
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
Iterative mode:
 ```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```



Non-interactive mode example
```bash
$ echo  "help"  | ./console.py

(hbnb)

Documented commands (type help  <topic>):

========================================

EOF all count create destroy help quit show update

```

 | Command | Example|
 | ------ | ------ |
 |show |show BaseModel 1234-1234-1234|
 |all| all BaseModel or all|
 |update| update class-name id attribute "value"|
 |create| create BaseModel|
 |class.count()|User.count()|
 |class.method|City.all() |
 |help| help or help User|
 |quit|quit or EOF|
## Models
Design for the airbnb clone v1.0
<img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/289/AirBnb_DB_diagramm.jpg" height=550 width = 1000>

 

## File storage

  

 You will convert the dictionary representation to a JSON string. JSON is a standard representation of a data structure. With this format, humans can read and all programming languages have a JSON reader and writer.

Now the flow of serialization-deserialization will be:
```bash
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump -> <class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'> -> <class 'BaseModel'>
```
Now the data will be persistent by using [__init__.py](./models/) , everytime the package engine is loaded init will be executed(init.py will be executed only one time if its imported n times)

  

## Tests
Code test with unittest module, test file are within the [test_models](./tests/test_models/)  folder
 ```bash 
ubuntu:~/AirBnB$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
ubuntu:~/AirBnB$
```

  

## Authors

  

*  **Hector lopez**  -    [<img src = "https://image.flaticon.com/icons/svg/25/25231.svg" width="30" height="30">](https://github.com/hectorlopezv)
