# Bigcorp API proyect

Sample API for retrieving BigCorp resources data.
Made with python.

## Steps to execute: 

1. Create virtual environment.
2. Install resources with `pip install -f requirements.txt`.
3. Run by setting the environment variable `FLASK_APP` to `bigcorp.py`, and then `flask run`.

## Available endpoints:

* /employees
* /employees/<id>
* /departments
* /departments/<id>
* /offices
* /offices/<id>

### Parameters

* `limit=<number>` to limit the retrieved occurrences
* `offset=<number>` to paginate the information
* `expand=<field.field...>` to expand data from id fields.
    * Available fields to expand: manager, office, department, superdepartment.

