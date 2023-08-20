import configparser
import psycopg2
import logging
from sql_queries import create_table_queries, drop_table_queries


# logging added due to help resolve issues with SQL Queries and Security

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# add schema and set search dist ## 3.1 Create tables (with a distribution strategy) in the `dist` schema

def drop_tables(cur, conn):
    for query in drop_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            logging.error(f"Error executing query: {query}\nError message: {e}")
            conn.rollback()
            raise

def create_tables(cur, conn):
    for query in create_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except psycopg2.Error as e:
            logging.error(f"Error executing query: {query}\nError message: {e}")
            conn.rollback()
            raise

def main():
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
