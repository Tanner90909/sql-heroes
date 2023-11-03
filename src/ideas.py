from database.db_connection import execute_query

# CREATE

def create_new_pirate():
    query = """
        INSERT INTO
            pirates (name, about_me, biography)
        VALUES
            (
                'God Usopp',
                'Crew mate of the Straw Hat Pirates',
                'Once a liar-liar pants on fire, after Luffy came to Usopps village and rescued Kaya from the infamous Black Cat Pirates, Usopp became the fourth member of the Straw Hat Pirates. He specializes in long range fighting and disguises.'
            );

        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 1, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 2, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 3, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 4, 2);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 5, 2);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (7, 6, 2);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (1, 7, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (2, 7, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (3, 7, 1);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (4, 7, 2);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (5, 7, 2);
        INSERT INTO
            relationships (pirate1_id, pirate2_id, relationship_type_id)
        VALUES
            (6, 7, 2);

        INSERT INTO
            ability_types (name)
        VALUES
            ('Sniper King');

        INSERT INTO
            abilities (pirate_id, ability_type_id)
        VALUES
            (7, 8)
            """
    execute_query(query)
    print("New pirate entry successfully created.")

# READ

def select_all_pirates():
    query = """
        SELECT * from pirates
    """
    returned_items = execute_query(query)
    for item in returned_items:
        print(item)
    return returned_items

# UPDATE

def modify_pirate():
    query = """
        SELECT 
            """