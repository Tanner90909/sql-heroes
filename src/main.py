from database.db_connection import execute_query, execute_modify

# CREATE

def create_new_pirate():
    prompt = input("Welcome to the Grand Line! Would you like to make a pirate profile? Y or N: ")
    if prompt == "Y":
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
    elif prompt == "N":
        print("Guess you won't be joining my pirate crew... loser.")
        pass
    else:
        print("Invalid response. Can't be king of the pirates if you don't set sail!")

# create_new_pirate()

# READ

def view_all_pirates():
    prompt = input("Would you like to see all the pirates on the seas? Y or N: ")
    if prompt == "Y":
        query = """
            SELECT * from pirates
        """
        returned_items = execute_query(query)
        for item in returned_items:
            print(item)
        return returned_items
    elif prompt =="N":
        print("You can't set sail for the Grand Line without knowing what... or WHO lies ahead!")
    else:
        print("Invalid input. You can't set sail for the Grand Line without knowing what... or WHO lies ahead! Please select Y or N")

view_all_pirates()

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

# pirate_to_update = input("Enter pirate name to update their biography: ")
# biography_to_update = input("Enter your new biography: ")
# update_pirate_bio(pirate_to_update, biography_to_update)

# DELETE

def delete_pirate(pirate_name):
    query = """
        DELETE FROM pirates
        WHERE name = %s;
            """
    params = (pirate_name,)
    execute_modify(query, params)
    print(f"Pirate '{pirate_name}' deleted successfully")

# pirate_to_delete = input("Enter pirate name to be deleted: ")
# delete_pirate(pirate_to_delete)

