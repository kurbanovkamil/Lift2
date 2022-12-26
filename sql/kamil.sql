CREATE TABLE IF NOT EXISTS equipments(
    id INTEGER PRIMARY KEY,
    equipment VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS resources(
    id INTEGER PRIMARY KEY,
    resource VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS post(
    id INTEGER PRIMARY KEY,
    position VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS firms(
    id INTEGER PRIMARY KEY,
    equipment_id INTEGER NOT NULL,
    resource_id INTEGER NOT NULL,
    title_firm VARCHAR(100) UNIQUE NOT NULL ,
    phone INTEGER UNIQUE NOT NULL,
    city VARCHAR(50) NOT NULL,
    FOREIGN KEY(equipment_id)
        REFERENCES equipments(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY (resource_id)
        REFERENCES resources(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
);

CREATE TABLE staff(
    id INTEGER PRIMARY KEY,
    firm_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    patronymic VARCHAR(100),
    date_of_birth VARCHAR(100) NOT NULL,
    FOREIGN KEY(firm_id)
        REFERENCES firms(id)
        ON DELETE SET NULL ON UPDATE NO ACTION,
    FOREIGN KEY(post_id)
        REFERENCES positions(id)
        ON DELETE SET NULL ON UPDATE NO ACTION
)