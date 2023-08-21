"""
This module handles the creation and dropping of tables in a Redshift database.

The module sets up logging to help resolve issues related to SQL Queries and security.
It establishes a connection to a Redshift cluster, drops tables if they exist, 
and creates new tables according to predefined SQL queries.
"""

import configparser
import psycopg2
import logging
from sql_queries import create_table_queries, drop_table_queries

# Setting up logging to help resolve issues with SQL Queries and security
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def drop_tables(cur, conn):
    """
    Drop tables defined in `drop_table_queries`.
    
    Parameters:
    - cur : cursor
        Cursor object to execute PostgreSQL commands.
    - conn : connection
        Connection object connected to the PostgreSQL database.
    
    Returns:
    None
    """
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            logging.error(f"Error executing query: {query}\nError message: {e}")
            conn.rollback()
            raise

def create_tables(cur, conn):
    """
    Create tables defined in `create_table_queries`.
    
    Parameters:
    - cur : cursor
        Cursor object to execute PostgreSQL commands.
    - conn : connection
        Connection object connected to the PostgreSQL database.
    
    Returns:
    None
    """
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            logging.error(f"Error executing query: {query}\nError message: {e}")
            conn.rollback()
            raise

def main():
    """
    Connect to the Redshift cluster, drop existing tables and create new ones.
    
    This function reads the configurations, establishes a connection, and then 
    orchestrates the table drop and create operations.
    
    Returns:
    None
    """
    config = configparser.ConfigParser()
    config.read("dwh.cfg")

    try:
        conn = psycopg2.connect(
            "host={} dbname={} user={} password={} port={}".format(
                *config['CLUSTER'].values()
            )
        )
        cur = conn.cursor()

        drop_tables(cur, conn)
        create_tables(cur, conn)

    except Exception as e:
        logging.error(f"Error connecting to Redshift cluster: {e}")

    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
