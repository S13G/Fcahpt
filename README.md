# FCAHPT
A Car Rental Website

### Installation

To run this project on your machine. Make sure you have __python3__ installed on your machine.
Create a virtual environment on your code editor using the command

```virtualenv <name of environment>```

### Example

```virtualenv env```

If virtualenv is not installed on your machine. Install it or use this alternative to create a virtual environment

```python -m venv <name of environment>```

After virtual environment has been created. Activate the environment.

### Linux

```source <name_of_environment>/bin/activate```

### Windows
```<name_of_environment>/Scripts/bin/activate```

Install all packages listed in the requirements.txt file using the command below:

```pip install -r requirements.txt```

All packages should install without errors.

Create a ```.env``` file in the product directory

Follow the example in the ```.env.example``` and populate the ```.env``` file with the values

Input ```SECRET_KEY=<secret key copied from terminal>``` if required


## NOTE:
**If all above has been met, skip to the command below**

Then run the python server with the command

### Make migrations
```python3 manage.py makemigrations```

### Migrate to the database
```python3 manage.py migrate```

### Run the server
```python3 manage.py runserver```
