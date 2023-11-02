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

create_new_pirate()

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

def update_pirate_bio():
    prompt = input("Would you like to update your biography? Y or N: ")
    if prompt == "Y":
        pirate_to_update = input("Enter pirate name to update their biography: ")
        biography_to_update = input("Enter your new biography: ")
        query = """
            UPDATE pirates
            SET biography = %s
            WHERE name = %s;
                """
        params = (biography_to_update, pirate_to_update)
        execute_modify(query, params)
        print(f"Pirate '{pirate_to_update}' bio has been updated")
    elif prompt == "N":
        print("That's okay, I think what you have now will work!")
    else:
        print("Invalid input. Please try again and select Y or N.")

update_pirate_bio()

def add_crew_mate():
    prompt = input("Would you like to add a crew mate? Y or N: ")
    user_name = input("What is your name?: ")
    if prompt == "Y":
            query = """
            SELECT * from pirates
                    """
            returned_items = execute_query(query)
            for item in returned_items:
                print(item[0], item[1])
    elif prompt == "N":
        pass
    else:
        print("Invalid input. Please try again and select Y or N.")
    prompt2 = input("Do you see your crew mate? Y or N: ")
    if prompt2 == "Y":
        pick_crew_mate = input("What is their number?: ")
        query = """
            INSERT INTO relationships(pirate1_id, pirate2_id, relationship_type_id)
            VALUES (%s, %s, %s)
                """
        pirate1_id_query = f"""
            SELECT id FROM pirates
            WHERE name = '{user_name}'
            """
        pirate1_id_vairable = execute_query(pirate1_id_query)
        pirate1_id = pirate1_id_vairable[0]
        pirate2_id = pick_crew_mate
        relationship_type_id = 1
        params = (pirate1_id, pirate2_id, relationship_type_id)
        execute_modify(query, params)
        print("You successfully added a member to your pirate crew!")
    elif prompt2 == "N":
        print("They must not have created a pirate profile yet. Check back soon!")
    else:
        print("Invalid input. Please try again and select Y or N.")

add_crew_mate()

def add_enemy():
    prompt = input("Would you like to add an enemy? Y or N: ")
    user_name = input("What is your name?: ")
    if prompt == "Y":
            query = """
            SELECT * from pirates
                    """
            returned_items = execute_query(query)
            for item in returned_items:
                print(item[0], item[1])
    elif prompt == "N":
        pass
    else:
        print("Invalid input. Please try again and select Y or N.")
    prompt2 = input("Do you see your enemy? Y or N: ")
    if prompt2 == "Y":
        pick_crew_mate = input("What is their number?: ")
        query = """
            INSERT INTO relationships(pirate1_id, pirate2_id, relationship_type_id)
            VALUES (%s, %s, %s)
                """
        pirate1_id_query = f"""
            SELECT id FROM pirates
            WHERE name = '{user_name}'
            """
        pirate1_id_vairable = execute_query(pirate1_id_query)
        pirate1_id = pirate1_id_vairable[0]
        pirate2_id = pick_crew_mate
        relationship_type_id = 2
        params = (pirate1_id, pirate2_id, relationship_type_id)
        execute_modify(query, params)
        print("You successfully added an enemy to vanquish!")
    elif prompt2 == "N":
        print("They must not have created a pirate profile yet. Check back soon!")
    else:
        print("Invalid input. Please try again and select Y or N.")

add_enemy()

# DELETE

def delete_pirate():
    prompt = input("Do you want to delete any pirates from the seas? Y or N: ")
    if prompt == "Y":
        pirate_to_delete = input("Enter pirate name to be deleted: ")
        query = """
            DELETE FROM pirates
            WHERE name = %s;
                """
        params = (pirate_to_delete,)
        execute_modify(query, params)
        print(f"Pirate '{pirate_to_delete}' deleted successfully")
    elif prompt == "N":
        print("The other pirates can exist... for now.")
    else:
        print("Invalid input. Please try again and select Y or N")

delete_pirate()

