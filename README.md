The README file includes a summary of the project, how to run the Python scripts, and an explanation of the files in the repository. Comments are used effectively and each function has a docstring.

# Project Summary

dwg.cfg
create_cluster.py
sql_queries.py
create_tables.py
etl.py
data_check.py

## CONFIGURE AWS USER AND CLUSTER VIA THE AWS CONSOLE

1. create and AWS account and add the IAM and EC2 Service
2. create an S3 Bucket and add the external data source to your bucket (optional?)
3. create a IAM User with AdministratorAccess, this user does not need access to the console. They're Access Keys are used to commincate to the AWS CLI. You need to create the user BEFORE creating Access Keys.
4. create the access keys and save them somewhere safe. You will need to add them to the 'dwh.cfg' file in this project.

## CREATE THE PYTHON ENVIRONMENT ON YOUR MACHINE

1. Clone this repo to your local computer or download the zip files.
2. Create a virtual environment in the same folder as the scripts.

NOTE ensure you create a gitignore file and add 'dwh.cfg' before you commit to a public git / remove your credentials

## RUN THE PYTHON SCRIPTS (SEE CODE FOR MORE DETAIL ON WHAT EACH SCRIPT DOES)

1. create or replace the tables in Redshift with create_tables.py
2. copy and insert data from external S3 bucket into the recently created Redshift tables etl.py
3. test the etl. Does the destination has the same number of unique records as the source for song and log data? data_check.py

---

Add data quality checks

- ROW COUNTS

Create a dashboard for analytic queries on your new database

- USE MATLAB WITH A BAR CHART SHOWING ROW COUNT FOR EACH TABLE
