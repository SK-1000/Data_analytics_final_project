from deta import Deta 

DETA_KEY = "a0c7sguy_sd2Cp3YAUnRFKLHRbWvCeXCeT1QcjTcW"

#initialise a project key

deta=Deta(DETA_KEY)

db = deta.Base("users_db")

def insert_user(username, name, password):
    """Gives back the user on a successful user creation or else there is an error"""
    return db.put({"key": username, "name": name, "password": password})

insert_user("skirwan", "Sheila Kirwan", "abc")

def fetch_all_users():
    """Return a dict of all users"""
    res = db.fetch()
    return res.items

print(fetch_all_users())