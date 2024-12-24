from pymongo import MongoClient
from datetime import datetime

# Connect to MongoDB
client = MongoClient('mongodb://mongodb:27017/')
db = client['chess_game_global']
players_collection = db['players']

# Player data to insert
players_data = [
    {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com", "dob": datetime(1990, 1, 1), "is_bot": False},
    {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com", "dob": datetime(1992, 2, 2), "is_bot": False},
    {"first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@example.com", "dob": datetime(1995, 3, 3), "is_bot": False},
    {"first_name": "Bob", "last_name": "Williams", "email": "bob.williams@example.com", "dob": datetime(1988, 4, 4), "is_bot": False},
    {"first_name": "Eve", "last_name": "Jones", "email": "eve.jones@example.com", "dob": datetime(1991, 5, 5), "is_bot": False},
    {"first_name": "Mike", "last_name": "Brown", "email": "mike.brown@example.com", "dob": datetime(1989, 6, 6), "is_bot": False},
    {"first_name": "Sarah", "last_name": "Davis", "email": "sarah.davis@example.com", "dob": datetime(1993, 7, 7), "is_bot": False},
    {"first_name": "Tom", "last_name": "Miller", "email": "tom.miller@example.com", "dob": datetime(1990, 8, 8), "is_bot": False},
    {"first_name": "Emily", "last_name": "Wilson", "email": "emily.wilson@example.com", "dob": datetime(1994, 9, 9), "is_bot": False},
    {"first_name": "David", "last_name": "Moore", "email":"david.moore@example.com" , dob=datetime(1987,10,10) , is_bot=False},
    {"first_name":"Linda" , last_name:"Taylor" , email:"linda.taylor@example.com" , dob=datetime(1996,11,11) , is_bot=False},
    {"first_name":"James" , last_name:"Anderson" , email:"james.anderson@example.com" , dob=datetime(1986,12,12) , is_bot=False},
    {"first_name":"Helen" , last_name:"Thomas" , email:"helen.thomas@example.com" , dob=datetime(1997,1,13) , is_bot=False},
    {"first_name":"Robert" , last_name:"Jackson" , email:"robert.jackson@example.com" , dob=datetime(1985,2,14) , is_bot=False},
    {"first_name":"Margaret" , last_name:"White" , email:"margaret.white@example.com" , dob=datetime(1998,3,15) , is_bot=False},
    {"first_name":"Richard" , last_name:"Harris" , email:"richard.harris@example.com" , dob=datetime(1984,4,16) , is_bot=False},
    {"first_name":"Susan" , last_name:"Martin" , email:"susan.martin@example.com" , dob=datetime(1999,5,17) , is_bot=False},
    {"first_name":"Charles" , last_name:"Thompson" , email:"charles.thompson@example.com" , dob=datetime(1983,6,18) , is_bot=False},
    {"first_name":"Elizabeth" , last_name:"Garcia" , email:"elizabeth.garcia@example.com" , dob=datetime(2000,7,19) , is_bot=False},
    {"first_name":"William" , last_name:"Martinez" , email:"william.martinez@example.com" , dob=datetime(1982,8,20) , is_bot=False},
    {"first_name":"Jessica" , last_name:"Robinson" , email:"jessica.robinson@example.com" , dob=datetime(2001,9,21) , is_bot=False}
]

# Insert data into the collection
players_collection.insert_many(players_data)

print("Data inserted successfully.")

