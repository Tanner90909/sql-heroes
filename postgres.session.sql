CREATE TABLE IF NOT EXISTS pirates (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(256) UNIQUE NOT NULL,
    about_me varchar(512) NOT null,
    biography varchar(2048) NOT NULL,
    image_url VARCHAR(64)
);

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Monkey D. Luffy',
        'Captain of the Straw Hat Pirates',
        'After being gifted a straw hat from his friend Shanks, Luffy decided that his destiny was to become King of the Pirates. He plans to conquer the grand line and find the One Piece.'
    );

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Roronoa Zoro',
        'First mate of the Straw Hat Pirates',
        'Determined to become the strongest swordsman in the world, Zoro was the first crew mate of the Straw Hat Pirates and set sail with Luffy to conquer the seas. He fights using a unique Three Sword Style.'
    );

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Nami',
        'Navigator of the Straw Hat Pirates',
        'Pained by her past in the East Blue, Nami initially joins the Straw Hat Pirates as an attempt to rob the crew. However, after Luffy stood up to Arlong to protect Nami and her Village, Nami became a devoted member of the crew. She regularly keeps the crewmates in line with a rather forceful approach.'
    );

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Aokiji Kuzan',
        'Admiral of the Navy Fleet',
        'Kuzan is a very laid back admiral. His understanding of justice is based almost exclusively on his own perceptions. Kuzan will not fight an enemy if he believes their purpose is for a greater good.'
    );

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Akainu Sakazuki',
        'Admiral of the Navy Fleet',
        'Strong and capable leader, but also an extremist. Believes in absolute justice and is ruthless in maintaining that justice. Stern and dead serious, expressionless at times. If you have done wrong, you will be punished.'
    );

INSERT INTO
    pirates (name, about_me, biography)
VALUES
    (
        'Kizaru Borsalino',
        'Admiral of the Navy Fleet',
        'Borsalino presents himself as calm and easy going. He is never stressed or concerned about a fight. His confidence in his abilities often lapses into absent-mindedness. Always sharply dressed.'
    );

CREATE TABLE relationship_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name varchar(64) UNIQUE NOT NULL
);

INSERT INTO
    relationship_types (name)
VALUES
    ('Crew Mate');

INSERT INTO
    relationship_types (name)
VALUES
    ('Enemy');

CREATE TABLE relationships (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pirate1_id INTEGER NOT NULL,
    FOREIGN KEY (pirate1_id) REFERENCES pirates (id) ON DELETE CASCADE,
    pirate2_id INTEGER NOT NULL,
    FOREIGN KEY (pirate2_id) REFERENCES pirates (id) ON DELETE CASCADE,
    relationship_type_id INTEGER NOT NULL,
    FOREIGN KEY (relationship_type_id) REFERENCES relationship_types (id) ON DELETE CASCADE
);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (1, 2, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (2, 1, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (1, 3, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (3, 1, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (2, 3, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (3, 2, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (4, 5, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (5, 4, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (4, 6, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (6, 4, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (5, 6, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (6, 5, 1);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (1, 4, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (4, 1, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (1, 5, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (5, 1, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (1, 6, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (6, 1, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (2, 4, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (4, 2, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (2, 5, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (5, 2, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (2, 6, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (6, 2, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (3, 4, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (4, 3, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (3, 5, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (5, 3, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (3, 6, 2);

INSERT INTO
    relationships (pirate1_id, pirate2_id, relationship_type_id)
VALUES
    (6, 3, 2);

CREATE TABLE ability_types (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(64)
);

INSERT INTO
    ability_types (name)
VALUES
    ('Rubber man');

INSERT INTO
    ability_types (name)
VALUES
    ('Best Swordsman in the World');

INSERT INTO
    ability_types (name)
VALUES
    ('Control the weather');

INSERT INTO
    ability_types (name)
VALUES
    ('Conjure and control ice');

INSERT INTO
    ability_types (name)
VALUES
    ('Conjure and control lava');

INSERT INTO
    ability_types (name)
VALUES
    ('Conjure and control Light');

INSERT INTO
    ability_types (name)
VALUES
    ('Haki');

-- SQLINES LICENSE FOR EVALUATION USE ONLY
-- CREATE SEQUENCE abilities_seq;

CREATE TABLE abilities (
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    pirate_id INTEGER NOT NULL,
    FOREIGN KEY (pirate_id) REFERENCES pirates (id) ON DELETE CASCADE,
    ability_type_id INTEGER NOT NULL,
    FOREIGN KEY (ability_type_id) REFERENCES ability_types (id) ON DELETE CASCADE
);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (1, 1);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (1, 7);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (2, 2);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (2, 7);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (3, 3);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (4, 4);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (4, 7);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (5, 5);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (5, 7);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (6, 6);

INSERT INTO
    abilities (pirate_id, ability_type_id)
VALUES
    (6, 7);