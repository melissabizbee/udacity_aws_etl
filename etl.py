"""
ETL process for loading data into staging tables from S3 and then inserting into Redshift tables.

This module provides functionalities to connect to a PostgreSQL instance, load data into staging tables, 
and transform them into analytics tables.
"""

import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    """
    Load data into staging tables from the source data present in S3.
    
    Parameters:
    - cur : cursor
        Cursor object to execute PostgreSQL commands.
    - conn : connection
        Connection object to connect to the PostgreSQL database.
    
    Returns:
    None
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    Insert data from staging tables into the analytics tables.
    
    Parameters:
    - cur : cursor
        Cursor object to execute PostgreSQL commands.
    - conn : connection
        Connection object to connect to the PostgreSQL database.
    
    Returns:
    None
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Extract, load, and transform data.
    
    Read the configuration, establish a connection to the database,
    and load data into staging, dimension and fact tables.
    
    Return:
    None
    """
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    conn = psycopg2.connect(
        "host={} dbname={} user={} password={} port={}".format(
            *config["CLUSTER"].values()
        )
    )
    cur = conn.cursor()

    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()
