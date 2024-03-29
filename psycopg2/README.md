# LearningPython
This workspace uses the same machine in the previous workspace, so any databases you previously created are preserved here as databases you can connect to using psql.

### Practice using psycopg2

#### Exercise 1

* Create a database in your Postgres server (using `createdb`)
* In psycopg2, create a table and insert some records using methods for SQL string composition. Make sure to establish a connection, and close it at the end of interacting with your database.
* Inspect your table schema and data in psql. (hint: use `SELECT *`, `\dt`, and `\d`)

#### Exercise 2

* Now modify your script to use string composition, throughout. Use both `%s` and `%(named_var)s` methods.
* Run the script, and then connect to the database using psql to inspect that the records were properly inserted into the tables in our database.

#### Exercise 3

* Fetch results from your first created record to create a new record, slightly modified.
* Fetch all of the rows from the table, and print each item line-by-line using a loop.