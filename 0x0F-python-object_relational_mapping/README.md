#### 0x0F. Python - Object-relational mapping

#### Learning Objectives

* Why Python programming is awesome

* How to connect to a MySQL database from a Python script

* How to SELECT rows in a MySQL table from a Python script

* How to INSERT rows in a MySQL table from a Python script

* What ORM means

* How to map a Python Class to a MySQL table

* How to create a Python Virtual Environment



#### Install and activate venv

* To create a Python Virtual Environment, allowing you to install specific dependencies for this python project, 
we will install venv:

```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```


#### Install MySQLdb module version 2.0.x

* For installing MySQLdb, you need to have MySQL installed: How to install MySQL 8.0 in Ubuntu 20.04

```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

#### Install SQLAlchemy module version 1.4.x

```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

#### AUTHOR

* UDUAK-OBONG UWAH
