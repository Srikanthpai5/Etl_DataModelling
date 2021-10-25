# import etl_scripts
from etl_scripts import *

# enter database details
user = 'root'  # please write your user name
password = 'password'  # please write your password
host = 'localhost'  # please write your host address
port = 3306 # not necessary for MySQL.
database = 'store_schema'


if __name__ == '__main__':

    # specifying the zip file name and zip file extract path
    zip_name = './Data.zip'

    extract_path = './store_project/'

    # Extract the data from zip file
    extract_zip(zip_name, extract_path)

    # Establish connection with SQL
    engine = establish_connection(user, password, host, database)

    # Write table name exists in SQL DB
    '''
    In the list, write those table name first, which has no foreign key associated.
    E.g. Check the store_db.sql file. products table has no foreign key associated, 
    hence it is added first in the list. orders table has associated foregin key, 
    hence added back in the table.
    '''

    # store_schema
    sql_table = ["products", "shippers", "customers", "order_statuses",
                 "orders", "order_items"]

    
    # transform_table -> sql_table_column + insert_data_sql

    for table in sql_table:
        # path, where extracted data from zip is located
        
        path = 'store_project/Data/'
        data = transform_table(table, path, engine)
        print(data.shape)

        # insert data to sql
        insert_data_sql(data, table, engine)