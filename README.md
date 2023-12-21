# LAB: Class 28


## Project: Working Forms


## Author: Jacob Bassett


## Description: 

This is our first project developing with forms with Django.


## Installation


Run the following in the terminal while in project's root directory. For macOS.


```bash

git clone "...url"

cd django-snacks

python3.? -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver

```


Open browser and proceed to "http://127.0.0.1:8000/home" or "http://127.0.0.1:8000/about".


## Requirements.txt

asgiref==3.7.2

Django==5.0

django-appconf==1.0.6

django-compressor==4.4

rcssmin==1.1.1

rjsmin==1.2.1

sqlparse==0.4.4


## Tests


Run the following in the terminal while in project's root directory and the virtual environment is active. For macOS.


```bash
(.venv) ➜  django-snacks3 git:(main) ✗ python3.11 manage.py test
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 0.799s

OK
Destroying test database for alias 'default'...
```