from database.db_connection import execute_query, execute_modify

# CREATE

def create_new_pirate():
    prompt = input("Would you like to make a pirate profile? Y or N: ")
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


def add_new_ability():
    prompt = input("Would you like to add a new ability? Y or N: ")
    if prompt == "Y":
        ability_name_question = input("What is your name?: ")
        ability_question = input("What ability do you have?: ")
        query1 = f"""
        INSERT INTO
            ability_types (name)
        VALUES
            ('{ability_question}');
            """
        query2 = f"""
        SELECT id FROM pirates
        WHERE name = '{ability_name_question}';
                """
        query3 = f"""
        SELECT id FROM ability_types
        WHERE name = '{ability_question}';
        """
        query4 = """
        INSERT INTO 
            abilities (pirate_id, ability_type_id)
        VALUES
            (%s, %s);
            """
        execute_modify(query1)
        pirate_id_to_add_ability_unformatted = execute_query(query2)
        ability_id_to_add_unformatted = execute_query(query3)
        pirate_id_to_add_ability = pirate_id_to_add_ability_unformatted[0]
        ability_id_to_add = ability_id_to_add_unformatted[0]
        params = (pirate_id_to_add_ability, ability_id_to_add)
        execute_modify(query4, params)
        print(f"You successfully added {ability_question} to your abilities!")
    elif prompt == "N":
        print("You're probably strong enough. I've heard you might have eaten a Devil Fruit ;)")
    else:
        print("Invalid input. Please try again and select Y or N.")


def view_pirate_abilities():
    prompt = input("Would you like to view a pirates abilities? Y or N: ")
    if prompt == "Y":
        pirate_name_to_view = input("Whose abilities would you like to see?: ")
        query1 = f"""
        SELECT id FROM pirates
        WHERE name = '{pirate_name_to_view}'
                """
        pirate_id_to_view_unformatted = execute_query(query1)
        pirate_id_to_view = pirate_id_to_view_unformatted[0]
        pirate_id_to_view_correct = pirate_id_to_view[0]
        query2 = f"""
        SELECT ability_type_id FROM abilities
        WHERE pirate_id = '{pirate_id_to_view_correct}'
        """
        ability_type_id_to_view_unformatted = execute_query(query2)
        ability_type_id_to_view1 = ability_type_id_to_view_unformatted[0]
        ability_type_id_to_view_correct1 = ability_type_id_to_view1[0]
        query3 = f"""
        SELECT name FROM ability_types
        WHERE id = '{ability_type_id_to_view_correct1}'
                """
        abilities_to_view = execute_query(query3)
        print(f"'{pirate_name_to_view} has the following abilities: '{abilities_to_view}'")
    elif prompt == "N":
        print("You're so strong you don't need to know what you're up against to win.")
    else:
        print("Invalid input. Please try again and select Y or N.")



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





intro = input("Welcome to the Grand Line matey! Have you heard about our pirate database? Y or N: ")
if intro == "Y":
    print("Awesome! What would you like to do?")
    question = input("""1 Create a new pirate profile
2 View all the pirates on the seas
3 Update my biography
4 Add a crewmate
5 Add an enemy
6 Add an ability
7 View a pirates abilities
8 Delete pirate from the seas
""")
    if question == "1":
        create_new_pirate()
    elif question == "2":
        view_all_pirates()
    elif question == "3":
        update_pirate_bio()
    elif question == "4":
        add_crew_mate()
    elif question == "5":
        add_enemy()
    elif question == "6":
        add_new_ability()
    elif question == "7":
        view_pirate_abilities()
    elif question == "8":
        delete_pirate()
    else:
        print("Invalid input. Please try again and select a number 1-8")
elif intro == "N":
    question2 = input("""Well, let me tell ya bout it! This is the Grand Line Network! Where all pirates can make profiles, connect with other users, and share their abilities! What would you like to do?
1 Create a new pirate profile
2 View all the pirates on the seas
3 Update my biography
4 Add a crewmate
5 Add an enemy
6 Add an ability
7 View a pirates abilities
8 Delete pirate from the seas                      
: """)
    if question2 == "1":
        create_new_pirate()
    elif question2 == "2":
        view_all_pirates()
    elif question2 == "3":
        update_pirate_bio()
    elif question2 == "4":
        add_crew_mate()
    elif question2 == "5":
        add_enemy()
    elif question2 == "6":
        add_new_ability()
    elif question2 == "7":
        view_pirate_abilities()
    elif question2 == "8":
        delete_pirate()
    else:
        print("Invalid input. Please try again and select a number 1-8")
else:
    print("Invalid input. Please try again and select Y or N")