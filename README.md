# <p align="center"> Data Modeling with MySQL</p>

<img height="300" src="https://prod-discovery.edx-cdn.org/media/course/image/f33be2a5-322f-4b9c-9ac5-a89b43080427-50e7d5598dac.small.jpeg"/>

## Overview
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. We will create a database schema and ETL pipeline for this analysis.

## Project Description
We define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into tables in MySQL.

## Dataset
The insights for the data are derived from: [dataset](docs/reports/dataset.md)

## How to run
1. Create ```.env``` file based on [env_example](./.env_example) file.
2. Install MySQL and dependencies
```
pip3 install -r requirements.txt
```
1. Set the PYTHONPATH environment variable to the current directory.
- In Windows:
```
SET PYTHONPATH=.
```
- In Linux, MacOS:
```
export PYTHONPATH=.:$PYTHONPATH
```
1. Run python script
```python
python3 src/main.py
```



## Tests
To check if the program is working properly, please run these scripts in order:
```python
pip3 install pytest
python3 -m pytest tests/
```

Expected result:
```
===================================== test session starts =====================================
platform win32 -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: D:\Github\data-modelling
plugins: mock-3.6.1
collected 5 items

tests\test_select.py .....                                                               [100%]

====================================== 5 passed in 0.18s ======================================
```


## Documents
Some documents about data modeling: [docs](docs/)

## References
- https://github.com/alanchn31/Data-Engineering-Projects.
- https://github.com/san089/Udacity-Data-Engineering-Projects.