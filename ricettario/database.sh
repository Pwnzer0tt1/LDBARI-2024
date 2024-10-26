#!/bin/bash 
ADMIN_PASSWORD=$(openssl rand -base64 12)

sqlite3 database.db <<EOF
-- Create recipes table
CREATE TABLE recipes (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);

-- Insert sample recipes
INSERT INTO recipes (name, ingredients, instructions) VALUES
('Spaghetti Carbonara', 'Spaghetti, Eggs, Parmesan, Pancetta, Black Pepper', 'Boil pasta, cook pancetta, mix with egg and cheese, combine.'),
('Tomato Soup', 'Tomatoes, Onion, Garlic, Basil, Vegetable Broth', 'Cook vegetables, blend, simmer with broth.'),
('Pancakes', 'Flour, Milk, Eggs, Sugar, Baking Powder', 'Mix ingredients, fry on skillet.');

-- Create users table 
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES
('user', 'tomato-soup'),
('admin', '$ADMIN_PASSWORD');
EOF
