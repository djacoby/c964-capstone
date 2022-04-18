import csv
from sqlalchemy import create_engine

# Create db engine and connect to db
engine = create_engine('postgresql://postgres@localhost:5432/capstone')
connection = engine.connect()


# Read csv files
stores = open('../raw-data/stores.csv', 'r')
transactions = open('../raw-data/transactions.csv', 'r')

# Convert stores csv to list of dictionaries
stores_list = []

for row in csv.DictReader(stores):
    stores_list.append(row)

cleaned_stores = []

# State lookup dictionary to map dataset states to midwestern states
state_dict = {
    "Pichincha": "IL",
    "Santo Domingo de los Tsachilas": "IN",
    "Manabi": "IN",
    "Tungurahua": "IN",
    "Esmeraldas": "IN",
    "Tungurahua": "IN",
    "Guayas": "OH",
    "Cotopaxi": "MI",
    "Manabi": "MI",
    "Chimborazo": "IA",
    "Imbabura": "IA",
    "Bolivar": "IA",
    "Pastaza": "IA",
    "Santa Elena": "IA",
    "Los Rios": "IA",
    "Azuay": "IA",
    "El Oro": "IA",
    "Loja": "IA",
}

# City lookup dictionary to map dataset cities to midwestern cities
city_dict = {
    "Quito": "Chicago",
    "Guayaquil": "Cleveland",
    "Santo Domingo": "Indianapolis",
    "Cayambe": "Springfield",
    "Latacunga": "Dearborn",
    "Riobamba": "Davenport",
    "Ibarra": "Sioux City",
    "Guaranda": "Council Bluffs",
    "Puyo": "Mason City",
    "Ambato": "Fort Wayne",
    "Salinas": "Dubuque",
    "Daule": "Akron",
    "Babahoyo": "Ames",
    "Quevedo": "Ottumwa",
    "Playas": "Lorain",
    "Libertad": "Canton",
    "Cuenca": "Des Moines",
    "Loja": "Cedar Rapids",
    "Machala": "Iowa City",
    "Esmeraldas": "Bloomington",
    "Manta": "Evansville",
    "El Carmen": "Gary"
}

# Loop through store list and clean data
for store in stores_list:
    store['state'] = state_dict[store['state']]
    store['city'] = city_dict[store['city']]

    cleaned_stores.append(store)

# Insert cleaned stores into database
for store in cleaned_stores:
    connection.execute(f"""
          INSERT INTO store (city, state, district)
          VALUES ('{store['city']}', '{store['state']}', '{store['cluster']}');
        """)


# Convert transactions csv to list of dictionaries
transactions_list = []
for row in csv.DictReader(transactions):
    transactions_list.append(row)

# Insert transactions into database
for transaction in transactions_list:
    connection.execute(f"""
          INSERT INTO transactions (store_id, transaction_date, amount)
          VALUES ({transaction['store_nbr']}, '{transaction['date']}', {transaction['transactions']});
        """)

# Close database connection
connection.close()
