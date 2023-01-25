import pickle
from pathlib import Path
import streamlit_authenticator as stauth

names = ["Sheila Kirwan", "Oliver Kirwan"]
usernames = ["skirwan", "okirwan"]
passwords = ["xxxx", "xxx"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pkl.pkl"
with file_path.open("rb") as file:
    pickle.dump(hashed_passwords, file)