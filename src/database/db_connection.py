from psycopg2 import connect, OperationalError

def create_connection(db_name, db_user, db_password, db_host = "localhost", db_port = "5432"):
    connection = None
    try:
        connection = connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        print("Query executed successfully")
        return cursor.fetchall()
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")
        return []
    finally:
        connection.close()

def execute_modify(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("Query executed successfully")
    except OSError as e:
        print(f"The error '{e}' occurred or the hero name is already taken")
    finally:
        connection.close()
        
# """
# To use the execute_query function you will need to:
# (1) Import it into your python file. 
# (2) use it as execute_query(query_string, tuple_with_matching_args)
# (3) attach a .fetchone(), .fetchall() to it
# Documentation on this can be found at https://www.psycopg.org/psycopg3/docs/basic/usage.html
# Examples:
# def select_all_patients():
#     query = """
#         SELECT * from patients
#     """
#     returned_items = execute_query(query)
#     for item in returned_items:
#         print(item[1])
#     return returned_items
   
# To use the execute_modify function you will need to:
# (1) Import it into your python file. 
# (2) use it as execute_modify(query_string, tuple_with_matching_args)
# (3) this creates the new record if you use 'insert'
# (4) this function can be used to edit and delete records
#  def create_new_patient(name, bio):
#     query = """
#         INSERT INTO patients (name, bio)
#         VALUES (%s, %s)
#         """
#     execute_modify(query, (name, bio))
    
# NOTE: Tuples () with only one argument need to have a trailing comma. 
# NOTE2: You may remove the print statements in create_connection() and execute_query() to keep from muddying up your project.
    
# """