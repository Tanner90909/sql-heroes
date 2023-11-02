from database.db_connection import execute_query, execute_modify

# CREATE

def create_new_pirate():
    pirate_name = input("Enter pirates name: ")
    pirate_about_me = input("Enter pirates about me: ")
    pirate_biography = input("Enter pirates biography: ")
    query = """
        INSERT INTO
            pirates (name, about_me, biography)
        VALUES
            (%s, %s, %s);
            """
    params = (pirate_name, pirate_about_me, pirate_biography)
    execute_modify(query, params)
    print("New pirate entry successfully created.")

create_new_pirate()

# READ

def view_all_pirates():
    query = """
        SELECT * from pirates
    """
    returned_items = execute_query(query)
    for item in returned_items:
        print(item)
    return returned_items

# view_all_pirates()

# UPDATE

def update_pirate_bio(pirate_name, new_biography):
    query = """
        UPDATE pirates
        SET biography = %s
        WHERE name = %s;
            """
    params = (new_biography, pirate_name)
    execute_modify(query, params)
    print(f"Pirate '{pirate_name}' bio has been updated")

pirate_to_update = input("Enter pirate name to update their biography: ")
biography_to_update = input("Enter your new biography: ")
update_pirate_bio(pirate_to_update, biography_to_update)

# DELETE

def delete_pirate(pirate_name):
    query = """
        DELETE FROM pirates
        WHERE name = %s;
            """
    params = (pirate_name,)
    execute_modify(query, params)
    print(f"Pirate '{pirate_name}' deleted successfully")

pirate_to_delete = input("Enter pirate name to be deleted: ")
delete_pirate(pirate_to_delete)

